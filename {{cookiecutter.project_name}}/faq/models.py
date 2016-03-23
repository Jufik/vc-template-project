# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.utils.safestring import mark_safe
from utils.markdown_helper import markdown

from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import TimeStampModel
from utils.models import ActiveModel
from utils.models import OrderModel


class FaqCategory(TimeStampModel, ActiveModel, OrderModel):
    """
    Define a category for Faqs
    """
    name = models.CharField(verbose_name=_(u"Nom"), max_length=200)

    class Meta:
        verbose_name = _(u"Categorie de Faq")
        verbose_name_plural = _(u"Categories de Faq")
        ordering = ['order']
    def __unicode__(self):
        return self.name

    def save(self):
        super(FaqCategory, self).save()       
    
    @property
    def get_name(self):
        return self.name


class Faq(TimeStampModel, ActiveModel, OrderModel):
    """
    Define a question with its answer for the FAQ
    """
    question = models.CharField(verbose_name=_(u"Question"), max_length=200)
    answer = models.TextField(verbose_name=_(u"Réponse"))
    category = models.ForeignKey('faq.FaqCategory', verbose_name=_(u"Catégorie"), related_name="faqs")
    
    class Meta:
        verbose_name = _(u"Question")
        verbose_name_plural = _(u"Questions")
        ordering = ['order']

    def __unicode__(self):
        return self.question

    @property
    def get_question(self):
        return self.question
    
    @property
    def get_answer(self):
        return markdown(self.answer)



    