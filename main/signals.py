from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Booking
from django.core.mail import send_mail
from django.conf import settings

@receiver(pre_save, sender=Booking)
def notify_user_on_date_change(sender, instance, **kwargs):
    if not instance.pk:
        return  # Новое бронирование, не отправляем письмо

    try:
        old_instance = Booking.objects.get(pk=instance.pk)
    except Booking.DoesNotExist:
        return

    if old_instance.start_date != instance.start_date or old_instance.end_date != instance.end_date:
        user_email = instance.user.email
        send_mail(
            subject='Изменение даты бронирования',
            message='Администратор изменил дату вашего бронирования. Если новое время вас не устраивает, пожалуйста, зайдите в аккаунт и измените его.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user_email],
            fail_silently=False,
        )