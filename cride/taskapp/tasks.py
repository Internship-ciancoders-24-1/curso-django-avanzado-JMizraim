""""""

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from celery.decorators import task, periodic_task

from datetime import datetime, timedelta

#Utilities
import jwt
import time


#Models
from cride.users.models import User
# from cride..models import Ride


@task(name="send_confirmation_email_task", max_retries=3)
def send_confirmation_email(user_pk):
    """Send account verification link to given user."""
    
    for i in range(30):
        print("Sleeping for 1 second")
        time.sleep(1)
    
    user = User.objects.get(pk=user_pk)
    
    verification_token = gen_verification_token(user)
    subject = "Welcome @{}! Verify your account to start using Comparte Ride".format(
        user.username
    )
    from_email = "Comparte Ride <noreply@comparteride.com>"
    content = render_to_string(
        "emails/users/account_verification.html",
        {"token": verification_token, "user": user},
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()


def gen_verification_token(user):
    """Create JWT token that the user can use to verify its account."""
    exp_date = datetime.now() + timedelta(days=3)
    payload = {
        "user": user.username,
        "exp": int(exp_date.timestamp()),
        "type": "email_confirmation",
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

    return token

# El curso termina antes de que se pueda implementar el siguiente código
# @periodic_task(name="disabled_finished_rides", run_every=timedelta(days=1))
# def disable_finished_rides():
#     """Disable finished rides."""
#     now = datetime.now()

#     rides = Ride.objects.filter(
#         arrival_date__gte=now, is_active=True
#     )

#     for ride in rides:
#         if ride.arrival_date <= now:
#             ride.is_active = False
#             ride.save()