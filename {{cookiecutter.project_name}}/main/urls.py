"""{{ cookiecutter.project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^redactor/', include('redactor.urls')),
    {% if cookiecutter.api %}
    url(r'^api/', include('api.urls')),
    {% endif %}
    url(r'^mails/', include('mails.urls', namespace='mails')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})

]


urlpatterns += i18n_patterns(
    url(r'^', include('front.urls', namespace='front')),
    {% if cookiecutter.blog %}
    url(r'^{{ cookiecutter.blog_url }}', include('blog.urls', namespace='blog')),
    {% endif %}

)

handler404 = 'front.views.error404'
handler500 = 'front.views.error500'
