from django.contrib import admin
from .models import MailTemplate
from redactor.widgets import RedactorEditor
from django import forms


class MailTemplateForm(forms.ModelForm):
    class Meta:
        model = MailTemplate
        exclude = []
        widgets = {
           'html': RedactorEditor(),
        }


class MailTemplateAdmin(admin.ModelAdmin):
    '''
        Admin View for Mail
    '''
    list_display = ('ref', 'subject',)
    form = MailTemplateForm
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)

admin.site.register(MailTemplate, MailTemplateAdmin)
