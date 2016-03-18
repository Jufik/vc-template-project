# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.translation import ugettext as _


# Static views
def home(request):
    return render(request, 'front/home.html')


# Error views
def handler404(request):
    return render(request, 'front/errors/handler404.html', status=404)


def handler500(request):
    return render(request, 'front/errors/handler500.html', status=500)