# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from faq.models import Faq

class Command(BaseCommand):
    """
    Command used to populate Faq model
    """
    def handle(self, **options):
        # print faq.__file__
        for i in range(1, 10):
            f = Faq()
            f.question = u"Hey méc, ça va?"
            f.answer = u"Yo dude%s, grave" % i
            f.order=i
            f.category_id=1
            print "Yup, it's saved"
            f.save()
