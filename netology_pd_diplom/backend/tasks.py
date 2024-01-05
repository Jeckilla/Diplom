from backend.celery import app
from django.core.mail import EmailMultiAlternatives

from backend.models import User
from netology_pd_diplom import settings


@app.task
def send_email(user_id, **kwargs):
    # при изменении статуса заказа отправляем письмо
    user = User.objects.get(id=user_id)

    msg = EmailMultiAlternatives(
        # title:
        f"Обновление статуса заказа",
        # message:
        f"Заказ сформирован",
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email]
    )
    msg.send()
