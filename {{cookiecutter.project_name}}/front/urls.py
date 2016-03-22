from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from . import views


urlpatterns = [
    # Error handling
    url(r'^404$', views.handler404, name='404'),
    url(r'^500$', views.handler500, name='500'),

    # Static pages
    url(r'^$', views.home, name='home'),
]
