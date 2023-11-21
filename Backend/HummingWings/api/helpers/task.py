""" This module contains all the tasks that are used in the project. """
from huey.contrib.djhuey import task
from django.utils import timezone

from ..helpers.email import send_template_email

from ..models.auth import Auth
from ..models.card import Card
from ..models.constants import CLIENT
from ..models.email_template import CARD_EXPIRED


@task()
def delete_diseble_auth():
    """ Delete all disabled auths. """
    disabled_auths = Auth.objects.filter(is_disabled=True).all()
    for auth in disabled_auths:
        auth.delete()

@task()
def delete_expired_cards():
    """ Delete all expired cards. """
    expired_cards = Card.objects.filter(date_expire__lt=timezone.now()).all()
    for card in expired_cards:
        send_template_email(
            email_id=CARD_EXPIRED,
            params={
                "full_name": card.owner.get_full_name(),
                "card_number": card.number,
                "date_expire": card.date_expire.strftime("%Y-%m-%d"),
            },
            receivers=card.owner.email,
            tracking_dict={
                "id_module": card.owner.pk,
                "type_module": CLIENT
            }
        )
        card.delete()
