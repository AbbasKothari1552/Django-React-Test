from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser
import random


def send_otp_via_mail(email):

    subject = 'Your account Verification email'
    otp = random.randint(100001,999999)
    message = f'Your otp is : {otp} .'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    user_obj = CustomUser.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()