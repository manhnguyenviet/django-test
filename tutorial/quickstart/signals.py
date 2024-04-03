from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Blog


@receiver(pre_save, sender=Blog)
def pre_save_handler(sender, instance, **kwargs):
    print(f"pre_save signal for {instance}")


@receiver(post_save, sender=Blog)
def post_save_handler(sender, instance, **kwargs):
    print(f"post_save signal for {instance}")
