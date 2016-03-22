# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.mail import send_mail as django_send_mail
from django.core.exceptions import ImproperlyConfigured
from django.template import Context
from django.template import Template
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.conf  import settings

class MailTemplate(models.Model):
    """
    Define a template in html and txt for sending mails
    """
    MAIL_CHOICES = (
        ('SIGN', _(u"Création d'un compte")),
        ('MAIL', _(u"Confirmation d'adresse e-mail")),
        (3, _(u"Order Credit card")),
        # (4, "Contact"),
        # (5, "Partner contact"),
        # (6, "Order EFT"),
    )


    MAIL_CONTEXT = {
        1: ['user', 'link'],
        2: ['user', 'link'],
        3: ['user', 'order', 'payments'],
        4: ['contact'],
        5: ['partner']
    }
    ref = models.CharField(verbose_name=_(u"Gabarit"), choices=MAIL_CHOICES, max_length=4, unique=True)

    created_at = models.DateTimeField(verbose_name=_(u"Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_(u"Updated at"), auto_now=True)

    updated_at = models.DateTimeField(verbose_name=_(u"Updated at"), auto_now=True)
    subject = models.CharField(max_length=255, verbose_name=_(u"Objet"))
    html = models.TextField(
        verbose_name='Contenu HTML',
        help_text='Use <a href="http://templates.mailchimp.com/resources/inline-css/">CSS Inliner</a>')
    txt = models.TextField(
        verbose_name='Contenu TXT',
        help_text='Use <a href="http://templates.mailchimp.com/resources/html-to-text/">HTML to Text</a>')

    def __unicode__(self):
        return self.subject

    @property
    def context(self):
        """
        display the context for info use only
        """
        return self.MAIL_CONTEXT[self.ref]

    def render(self, context):
        """
        Add up template's extension and relevant tags.
        """
        context.update({
            'site_url': settings.SITE_URL
        })
        self.html = """
        {%% extends 'mails/_layout.html' %%}
        {%% block body %%}
        %s
        {%% endblock body %%}
        """ % self.html

        response = {
            # 'body': transform(Template(self.html).render(Context(context))),
            'body': Template(self.html).render(Context(context)),
            'text': Template(self.txt).render(Context(context)),
            'subject': Template(self.subject).render(Context(context))
        }

        return response

    def send(self, receivers, context):
        """
        Send the email
        """
        try:
            sender = settings.EMAIL_SENDER
        except AttributeError:
            raise ImproperlyConfigured('EMAIL_SENDER Should be configured')
        email_content = self.render(context)

        subject = email_content['subject']
        html_body = email_content['body']
        text_body = email_content['text']
        return django_send_mail(
            subject=subject,
            from_email=sender,
            recipient_list=receivers,
            message=text_body,
            html_message=html_body)


def send_mail(ref, receivers, context):
    mail = MailTemplate.objects.get(ref=ref)
    return mail.send(receivers, context)
