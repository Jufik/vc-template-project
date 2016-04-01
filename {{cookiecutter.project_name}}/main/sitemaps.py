# -*- coding: utf-8 -*-
from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap

# Example
# from pages.models import Page

# class PageSiteMap(Sitemap):
#     """
#     docstring for ProjectSiteMap
#     check https://docs.djangoproject.com/en/1.9/ref/contrib/sitemaps/ 
#     for docs
#     """
#     changefreq = "daily"
#     # priority = 1

#     def items(self):
#         return Page.objects.filter(navbar__has_children=False)

#     def name(self, obj):
#         return obj.title

#     def lastmod(self, obj):
#         return obj.updated_at

#     def location(self, obj):
#         return obj.url

#     def priority(self, obj):
#         return obj.index_priority