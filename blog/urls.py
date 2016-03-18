# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from . import views

urlpatterns = [
    # Error handling
    url(_(r'^$'), views.posts, name='posts'),
    url(_(r'^/categories/(?P<category_slug>[a-zA-Z0-9_-]+)$'), views.category, name='category'),
    url(_(r'^/articles/(?P<article_slug>[a-zA-Z0-9_-]+)$'), views.article, name='article'),
]

# 