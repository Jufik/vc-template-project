# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.utils.safestring import mark_safe
from utils.markdown_helper import markdown

from django.utils.translation import ugettext_lazy as _
from django.db import models

class FaqCategory(models.Model):
    """
    Define a category for Faqs
    """
    name = models.CharField(verbose_name=_(u"Nom"), max_length=200)
    
    is_active = models.BooleanField(verbose_name=_(u"Actif"), default=True)

    created_at = models.DateTimeField(verbose_name=_(u"Création"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_(u"Mise à jour"), auto_now=True)

    order = models.PositiveIntegerField(verbose_name=_(u"Ordre d'apparition"))

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


class Faq(models.Model):
    """
    Define a question with its answer for the FAQ
    """
    question = models.CharField(verbose_name=_(u"Question"), max_length=200)
    answer = models.TextField(verbose_name=_(u"Réponse"))
    category = models.ForeignKey('faq.FaqCategory', verbose_name=_(u"Catégorie"), related_name="faqs")

    is_active = models.BooleanField(verbose_name=_(u"Actif"), default=True)

    created_at = models.DateTimeField(verbose_name=_(u"Création"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_(u"Mise à jour"), auto_now=True)

    order = models.PositiveIntegerField(verbose_name=_(u"Ordre d'apparition"))

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



    