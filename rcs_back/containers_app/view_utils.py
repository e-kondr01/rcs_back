from django.utils import timezone

from rcs_back.containers_app.models import Container, FullContainerReport
from rcs_back.containers_app.tasks import *


def check_takeout_condition(container: Container) -> bool:
    """Проверяет, выполнены ли условия для сбора после заполнений
    текущего контейнера"""
    if (container.building_part and
            container.building_part.meets_takeout_condition()):
        return True
    elif container.building.meets_takeout_condition():
        return True
    else:
        return False


def takeout_condition_met_notify():
    # TODO
    pass


def handle_repeat_full_report(container: Container) -> None:
    if check_takeout_condition(container):
        takeout_condition_met_notify()


def handle_first_full_report(container: Container) -> None:
    """При заполнении контейнера нужно запомнить время
    и пересчитать среднее время заполнения"""
    FullContainerReport.objects.create(
        container=container
    )
    calc_avg_fill_time.delay(container.pk)
    """Если выполняются условия для вывоза по
    кол-ву бумаги, сообщаем"""
    if check_takeout_condition(container):
        takeout_condition_met_notify()


def handle_empty_container(container: Container) -> None:
    """При опустошении контейнера нужно запомнить время
    и перечитать среднее время выноса"""
    last_full_report = container.last_full_report()
    if last_full_report:
        last_full_report.emptied_at = timezone.now()
        last_full_report.save()
        calc_avg_takeout_wait_time.delay(container.pk)


def public_container_add_notify(container: Container) -> None:
    """Отправляет сообщение с инструкциями для активации
    добавленного контейнера"""
    pass


def send_public_feedback(email: str, msg: str, container_id: int = 0) -> None:
    """Отправляет сообщение с обратной связью на почту экологу"""
    pass
