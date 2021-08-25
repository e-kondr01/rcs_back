from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from io import BytesIO

from rcs_back.containers_app.models import Container
from .utils.qr import generate_sticker


@receiver(post_save, sender=Container)
def check_container_state(sender, instance: Container,
                          created: bool, **kwargs) -> None:
    """Генерируем стикер, если у контейнера его нет"""
    if not instance.sticker:
        sticker_im = generate_sticker(instance.pk)
        sticker_io = BytesIO()
        sticker_im.save(sticker_io, "JPEG", quality=85)
        sticker = File(sticker_io, name=f"sticker_{instance.pk}")
        instance.sticker = sticker
        instance.save()

    """Записываем время активации"""
    if instance.status == Container.ACTIVE and not instance.activated_at:
        instance.activated_at = timezone.now()
        instance.save()
