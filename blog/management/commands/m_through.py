# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from pages.models import Page, PageRelation


class Command(BaseCommand):
    """
    Command used to populate PageRelation model
    """

    def handle(self, **options):
        for p in Page.objects.all():
            for r in p.related.all():
                rp = PageRelation(page=p, related=r, order=0)
                rp.save()
