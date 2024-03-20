import logging

#from celery import shared_task
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from app.models import CustomToken as Token

# from celery.utils.log import get_task_logger

from app.models import User, CustomToken
#from utils.celery import celery_email_task_kwargs

# from urllib.parse import urljoin

from .utils import Util

logger = logging.getLogger(__name__)


#@shared_task(**celery_email_task_kwargs)
def send_activation_email(user_pk: int):
    if user := User.objects.filter(pk=user_pk).first():
        CustomToken.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        url = f"{settings.FRONTEND_URL}/register/verify/{token.token}/"
        data = {
            "template_name": "accounts/email/email_verification.html",
            "context": {"user": user, "verification_url": url},
            "email_subject": _("Verify your email"),
            "to_email": user.email,
            "from_email": settings.DEFAULT_FROM_EMAIL,
        }
        res = Util.send_email(data)
        print(res)
        logger.info(
            f"send_activation_email: Successfully sent message to user {user.pk}"
        )
    else:
        logger.warning(f"send_activation_email: User: {user.pk} not found")


#@shared_task(**celery_email_task_kwargs)
def send_reset_password_email(user_pk: int):
    if user := User.objects.filter(pk=user_pk).first():
        CustomToken.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        url = f"{settings.FRONTEND_URL}/forgot-password/{token.token}/"
        Util.send_email(
            data={
                "template_name": "accounts/email/reset_password.html",
                "context": {"user": user, "reset_password_url": url},
                "email_subject": _("Reset Your Password"),
                "to_email": user.email,
                "from_email": settings.DEFAULT_FROM_EMAIL,
            }
        )
        logger.info(
            f"send_reset_password_email: Successfully sent message to user {user.pk}"
        )
    else:
        logger.warning(f"send_reset_password_email: User: {user.pk} not found")


# @shared_task(**celery_email_task_kwargs)
# def send_reset_username_email(user_pk: int):
#     if user := User.objects.filter(pk=user_pk).first():
#         to = [user.email]
#         djoser_settings.EMAIL.username_reset(context={"user": user}).send(to)
#         logger.info(
#             f"send_reset_username_email: Successfully sent message to user {user.pk} {to}"
#         )
#     else:
#         logger.warning(
#             f"send_reset_username_email: User: {user_pk} not found",
#         )
