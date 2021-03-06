from rest_framework import serializers

from rcs_back.containers_app.models import Container
from rcs_back.containers_app.serializers import (
    BuildingPartSerializer,
    BuildingShortSerializer,
    ContainerSerializer,
)
from rcs_back.takeouts_app.models import (
    ContainersTakeoutRequest,
    TakeoutCondition,
    TankTakeoutRequest,
)


class AddContainersTakeoutSerializer(serializers.ModelSerializer):
    """Для создания заявки на вынос контейнера"""

    containers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Container.objects.filter(status=Container.ACTIVE),
        required=False
    )
    emptied_containers = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )

    class Meta:
        model = ContainersTakeoutRequest
        fields = [
            "id",
            "created_at",
            "building",
            "building_part",
            "containers",
            "confirmed_at",
            "emptied_containers",
            "worker_info",
            "mass",
            "requesting_worker_name",
            "requesting_worker_phone",
            "archive_room",
            "archive_mass",
            "archive_description"
        ]
        read_only_fields = [
            "created_at",
            "confirmed_at",
            "emptied_containers",
            "worker_info"
        ]


class ArchiveTakeoutSerializer(serializers.ModelSerializer):
    """Для создания сбора архива неавторизированным пользователем"""

    class Meta:
        model = ContainersTakeoutRequest
        fields = [
            "id",
            "building",
            "requesting_worker_phone",
            "requesting_worker_email",
            "archive_room",
            "archive_description"
        ]


class ContainersTakeoutConfirmationSerializer(serializers.ModelSerializer):
    """Для подтверждения выноса контейнеров"""

    containers = ContainerSerializer(
        many=True, read_only=True
    )

    emptied_containers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Container.objects.filter(status=Container.ACTIVE),
        required=False
    )

    already_empty_containers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Container.objects.filter(status=Container.ACTIVE),
        required=False
    )

    unavailable_containers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Container.objects.filter(status=Container.ACTIVE),
        required=False
    )

    class Meta:
        model = ContainersTakeoutRequest
        fields = [
            "id",
            "created_at",
            "building",
            "containers",
            "confirmed_at",
            "emptied_containers",
            "already_empty_containers",
            "unavailable_containers",
            "worker_info",
            "mass",
            "requesting_worker_name",
            "requesting_worker_phone",
            "archive_room",
            "archive_mass",
            "archive_description"
        ]
        read_only_fields = [
            "created_at",
            "building",
            "building_part"
            "containers",
            "confirmed_at"
        ]


class TankTakeoutRequestSerializer(serializers.ModelSerializer):
    """Для создания заявки на вывоз бака"""

    class Meta:
        model = TankTakeoutRequest
        fields = [
            "id",
            "created_at",
            "building",
            "confirmed_at",
            "confirmed_mass",
            "wait_time",
            "fill_time",
            "mass"
        ]
        read_only_fields = [
            "created_at",
            "confirmed_at",
            "confirmed_mass"
        ]


class TankTakeoutConfirmationSerializer(serializers.ModelSerializer):
    """Для подтверждения вывоза бака"""

    class Meta:
        model = TankTakeoutRequest
        fields = [
            "id",
            "created_at",
            "building",
            "confirmed_at",
            "confirmed_mass",
            "wait_time",
            "fill_time",
            "mass"
        ]
        read_only_fields = [
            "building",
            "created_at",
            "confirmed_at"
        ]


class TakeoutConditionSerializer(serializers.ModelSerializer):
    building = BuildingShortSerializer()
    building_part = BuildingPartSerializer()

    class Meta:
        model = TakeoutCondition
        fields = [
            "id",
            "building",
            "building_part",
            "office_days",
            "public_days",
            "mass",
            "ignore_reports"
        ]


class AddTakeoutConditionSerializer(serializers.ModelSerializer):
    """Сериализатор с id здания и корпуса"""

    class Meta:
        model = TakeoutCondition
        fields = [
            "id",
            "building",
            "building_part",
            "office_days",
            "public_days",
            "mass",
            "ignore_reports"
        ]
