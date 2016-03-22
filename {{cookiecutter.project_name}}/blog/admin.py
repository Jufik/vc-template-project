# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from imagekit.admin import AdminThumbnail

from .models import (
    Category,
    Post,
    )

from .forms import (
    PostContentForm,
    CategoryForm
    )


class PostInline(admin.StackedInline):
    '''
    Tabular Inline View for Post
    '''
    model = Post
    extra = 0
    classes = ('grp-collapse ',)
    inline_classes = ('grp-collapse', 'grp-closed')

    form = PostContentForm


class CategoryAdmin(admin.ModelAdmin):
    '''
        Admin View for Category
    '''

    list_display = ('colored_name',)
    # form = CategoryForm
    inlines = [
        PostInline,
    ]

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    '''
        Admin View for Post
    '''
    form = PostContentForm
    readonly_fields = ('slug',)
    pass

admin.site.register(Post, PostAdmin)

