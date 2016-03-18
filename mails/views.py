from django.http import HttpResponse
from .models import MailTemplate


def preview(request, mailref):
    mail = MailTemplate.objects.get(ref=mailref)
    return HttpResponse(mail.render({})['body'])
