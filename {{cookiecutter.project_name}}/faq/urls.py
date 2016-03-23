from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from . import views

urlpatterns = [
    # Error handling
    url(_(r'^$'), views.faq, name='faq'),

]