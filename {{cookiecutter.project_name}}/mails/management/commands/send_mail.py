# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from emailauth.models import User

class Command(BaseCommand):
    """
    Command used to populate Faq model
    """

    def handle(self, **options):
        m = User.objects.get(email="julien@vingtcinq.io")
        m.send_sign_up_mail()


