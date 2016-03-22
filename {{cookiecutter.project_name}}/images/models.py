# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from imagekit.admin import AdminThumbnail

from django.db import models
from django.utils.translation import ugettext_lazy as _

from imagekit import ImageSpec, register
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to="images/%Y/%m/%d/%h %i %s")
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 100)],
                                      format='JPEG',
                                      options={'quality': 60})
    description = models.CharField(_(u"Description"), max_length=50)

    class Meta:
        verbose_name = _(u"Image")
        verbose_name_plural = _(u"Images")

    def __unicode__(self):
        return self.description


class WinePicture(models.Model):
    image = models.ImageField(upload_to="images/%Y/%m/%d/%h %i %s")
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 100)],
                                      format='JPEG',
                                      options={'quality': 60})
    description = models.CharField(_(u"Description"), max_length=50)

    class Meta:
        verbose_name = _(u"Image")
        verbose_name_plural = _(u"Images")

    def __unicode__(self):
        return self.description


class Thumbnail(ImageSpec):
    processors = [ResizeToFill(100, 100)]
    format = 'JPEG'
    options = {'quality': 60}

register.generator('images:thumbnail', Thumbnail)
