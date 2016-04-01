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
from django.contrib.sitemaps.views import sitemap

# Sitemaps example
# from .sitemaps import PageSiteMap, BlogSiteMap

# sitemaps = {'sitemaps':
#             {'projects': PageSiteMap,
#             'articles':BlogSiteMap,
#              }
sitemaps = {'sitemap': {}}

        }
            urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^redactor/', include('redactor.urls')),
    {% if cookiecutter.api %}
    url(r'^api/', include('api.urls')),
    {% endif %}
    url(r'^mails/', include('mails.urls', namespace='mails')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^sitemap\.xml$', sitemap, sitemaps, name='django.contrib.sitemaps.views.sitemap'),


]


urlpatterns += i18n_patterns(
    url(r'^', include('front.urls', namespace='front')),
    {% if cookiecutter.blog %} url(r'^{{ cookiecutter.blog_url }}', include('blog.urls', namespace='blog')),{% endif %}
    {% if cookiecutter.faq %} url(r'^{{ cookiecutter.faq_url }}', include('faq.urls', namespace='faq')),{% endif %}

)

handler404 = 'front.views.error404'
handler500 = 'front.views.error500'

