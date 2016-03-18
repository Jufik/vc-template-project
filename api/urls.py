from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    # Error handling
    url(r'^v1/', include('api.v1.urls')),

]