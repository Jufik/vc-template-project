# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

# Create your models here.
from django.utils.html import format_html

STATES = [
    (0, _(u"Draft")),
    (1, _(u"Published"))
]


class Category(models.Model):
    """
    Define a category for a Blog post

    Available template tag: 
    {% category_badge category %} will return "badge stuff"


    ##TODO: 
    -Need to build our own custom widget for colorfield (based on a library right now)
    -Need to create a relevant Icon class to allow icon selection (from another app?)
    """

    name = models.CharField(verbose_name=_(u"Nom"), max_length=200)

    slug = models.SlugField(_(u"Adresse"), unique=True, editable=False, default=None)
    order = models.IntegerField(_(u"Ordre d'apparition"))
    description = models.TextField(_(u"Meta description"), help_text=_(u"Description (pour référencement)"))

    created_at = models.DateTimeField(verbose_name=_(u"Création"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_(u"Mise à jour"), auto_now=True)

    class Meta:
        verbose_name = _(u"Categorie d'une actualié")
        verbose_name_plural = _(u"Categories des actualités")
        ordering = ['order']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        for child in self.__class__.objects.filter(order=self.order).exclude(id=self.id):
            child.order += 1
            child.save()
        if self.slug is None:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    @property
    def colored_name(self):
        """
        return colored label
        """
        return format_html('<span style="background-color:%s;">%s</span>' % (self.bg_color, self.name))


class PostManager(models.Manager):
    """
    Manager for post model
    """

    def published(self):
        return self.filter(state=1)

    def current(self):
        return self.published().order_by("-published_at")


class Post(models.Model):
    """
    Define a Blog (news)
    """
    category = models.ForeignKey('blog.Category', related_name='posts')

    title = models.CharField(_(u"Titre"), max_length=90, unique=True)
    subtitle = models.CharField(_(u"Titre second niveau"), max_length=150)
    slug = models.SlugField(_(u"Adresse"), unique=True, editable=False, default=None)

    short_content = models.CharField(_(u"Résumé"), max_length=300)
    content = models.TextField(_(u"Contenu"))
    description = models.TextField(_(u"Meta description"), help_text=_(u"Description (pour référencement)"))

    created_at = models.DateTimeField(verbose_name=_(u"Création"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_(u"Mise à jour"), auto_now=True)
    published_at = models.DateTimeField(_(u"Publication"),
                                        null=True, blank=True)
    state = models.SmallIntegerField(_(u"Publication"), choices=STATES)

    # image_upload = models.ManyToManyField('images.Image', verbose_name=_(u"Photo de l'article"), related_name='posts')
    cover = models.ForeignKey('images.Image', verbose_name=_(
        u"Image Vignette"), related_name='cover', blank=True, null=True)
    picture = models.ForeignKey('images.Image', verbose_name=_(u"Image Article"), related_name='posts')

    related_articles = models.ManyToManyField(
        'blog.Post', verbose_name=_(u"Artciles associés"), related_name='referenced_articles', blank=True)

    objects = PostManager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"Actualié")
        verbose_name_plural = _(u"Actualités")
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        """
        Update published_at
        """
        if self.is_published and self.published_at is None:
            self.published_at = timezone.now()

        if self.slug is None:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

    @property
    def is_published(self):
        return self.state == 1

    @property
    def suggestions(self):
        return self.related_articles.filter(state=1)
