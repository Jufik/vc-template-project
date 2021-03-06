# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


from faq.models import Faq

class FaqForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FaqForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Faq
        fields = ('question', 'answer', 'order', 'is_active', 'category')
