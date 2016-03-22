from django.conf.urls import patterns, url


urlpatterns = patterns(
    'mails.views',
    url(r'^mail-(?P<mailref>\d+)$', 'preview', name='preview'),
)
