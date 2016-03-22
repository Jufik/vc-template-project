# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import (
    render,
    get_object_or_404,
    get_list_or_404)
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count

from .models import Post, Category
# Create your views here.


def posts(request):
    title = _(u"Journal - MyWine")
    posts = Post.objects.filter(state=1)
    categories = Category.objects.annotate(count_posts=Count('posts')).filter(count_posts__gt=0)
    return render(request, 'blog/news.html',
                  {'title': title,
                   'posts': posts,
                   'categories': categories
                   })


def category(request, category_slug):
    title = _(u"Journal - Catégorie")

    categories = Category.objects.annotate(count_posts=Count('posts')).filter(count_posts__gt=0)
    posts = get_list_or_404(Post, category__slug=category_slug, state=1)
    return render(request, 'blog/news.html',
                  {'title': title,
                   'posts': posts,
                   'categories': categories
                   })


def article(request, article_slug):
    title = _(u"Journal - Catégorie")

    categories = Category.objects.annotate(count_posts=Count('posts')).filter(count_posts__gt=0)
    post = get_object_or_404(Post, slug=article_slug, state=1)
    related_posts = post.related_articles.filter(state=1)[:2]
    
    return render(request, 'blog/post.html',
                  {'title': title,
                   'post': post,
                   'categories': categories,
                   'related_posts':related_posts
                   })
