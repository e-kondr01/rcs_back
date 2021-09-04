from django.http.response import HttpResponse
from django.utils import timezone
from rest_framework import generics, permissions, views, status
from rest_framework.response import Response
from tempfile import NamedTemporaryFile

from rcs_back.utils.mixins import UpdateThenRetrieveModelMixin
from rcs_back.containers_app.models import BuildingPart, Container
from .utils.email import *
from .utils.excel import get_container_stats_xl
from .serializers import *
from .tasks import *


class FullContainerReportView(generics.CreateAPIView):
    """View для заполнения контейнера"""
    permission_classes = [permissions.AllowAny]
    serializer_class = FullContainerReportSerializer

    def perform_create(self, serializer) -> None:
        if "container" in serializer.validated_data:
            container = serializer.validated_data["container"]
            by_staff = self.request.user.is_authenticated
            if container.last_full_report():
                # Повторное сообщение о заполнении
                handle_repeat_full_report.delay(
                    container.pk,
                    by_staff
                )
            else:
                # Первое сообщение
                handle_first_full_report.delay(
                    container.pk,
                    by_staff
                )


class ContainerDetailView(UpdateThenRetrieveModelMixin,
                          generics.RetrieveUpdateDestroyAPIView):
    """ View для CRUD-операций с контейнерами """
    queryset = Container.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    retrieve_serializer = ContainerSerializer
    update_serializer = ChangeContainerSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return self.retrieve_serializer
        else:
            return self.update_serializer


class ContainerListView(generics.ListCreateAPIView):
    """ View для CRUD-операций с контейнерами """

    queryset = Container.objects.all()

    filterset_fields = [
        "building",
        "building_part",
        "floor",
        "status"
    ]

    allowed_sorts = [
        "building",
        "building_part",
        "floor",
        "status"
    ]

    def get_queryset(self):
        """Сортировка"""
        queryset = Container.objects.all()
        if "is_full" in self.request.query_params:
            is_full_param = self.request.query_params.get("is_full")
            is_full = False if is_full_param == "false" else True
            queryset = Container.objects.filter(
                _is_full=is_full
            )

        if "sort_by" in self.request.query_params:
            sort = self.request.query_params.get("sort_by")

            if sort not in self.allowed_sorts:
                return queryset

            if sort == "is_full":
                sort = "_is_full"  # Чтобы не путать фронт

            if "order_by" in self.request.query_params:
                order_by = self.request.query_params.get("order_by")
                if order_by == "desc":
                    sort = "-" + sort

            return queryset.order_by(sort)

        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ContainerSerializer
        else:
            return ChangeContainerSerializer


class BuildingListView(generics.ListAPIView):
    """Списко зданий (для опций при создании контейнера)"""
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()
    permission_classes = [permissions.AllowAny]


class ContainerPublicAddView(generics.CreateAPIView):
    """Добавление своего контейнера с главной страницы"""
    queryset = Container.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ContainerPublicAddSerializer

    def perform_create(self, serializer):
        instance = serializer.save(status=Container.WAITING)
        public_container_add_notify.delay(instance.pk)


class ActivateContainerView(generics.UpdateAPIView):
    """ View для активации контейнера """
    permission_classes = [permissions.AllowAny]
    serializer_class = ActivateContainerSerializer
    queryset = Container.objects.filter(status=Container.WAITING)


class PublicFeedbackView(views.APIView):
    """View для обратной связи на главной странице"""
    serializer_class = PublicFeedbackSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        container_id = 0
        if "container_id" in serializer.validated_data:
            container_id = serializer.validated_data["container_id"]
        msg = serializer.validated_data["msg"]
        send_public_feedback(email, msg, container_id)
        resp = {
            "status": "email sent"
        }
        return Response(resp)


class BuildingPartView(generics.ListAPIView):
    """View списка корпусов"""
    serializer_class = BuildingPartSerializer
    queryset = BuildingPart.objects.all()
    filterset_fields = ["building"]
    permission_classes = [permissions.AllowAny]


class EmptyContainerView(views.APIView):
    """View для отметки контейнера пустым
    экоотделом"""

    def post(self, request, *args, **kwargs):
        if "pk" in self.kwargs:
            container = Container.objects.filter(
                pk=self.kwargs["pk"]
            ).first()
            if container:
                last_report = container.last_full_report()
                if last_report:
                    """Этот view используется для корректировки
                    ошибок, поэтому не вызываем handle_empty_container
                    (там устанавливается время опустошения)"""
                    last_report.delete()
                    container._is_full = False  # Для сортировки
                    container.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ContainerStatsExcelView(views.APIView):
    """Возвращает .xlsx файл со статистикой по контейнерам"""

    def get(self, request, *args, **kwargs):
        wb = get_container_stats_xl()
        with NamedTemporaryFile() as tmp:
            fname = "recycle-starter-container-stats-"
            fname += timezone.now().strftime("%d.%m.%Y")
            fname += ".xlsx"
            wb.save(tmp.name)
            file_data = tmp.read()
            response = HttpResponse(
                file_data,
                headers={
                    "Content-Type": "application/vnd.ms-excel",
                    "Content-Disposition":
                    f'attachment; filename={fname}',
                    "Content-Language": "ru-RU"
                }
            )
            return response
