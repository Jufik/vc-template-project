# -*- coding: utf-8 -*-

from django.db import models


class CreatedManager(models.Manager):
    """
    Get all objects with created_at criteria
    """
    def get_queryset(self):
        return super(CreatedManager, self).get_queryset()


    def before(self, datetime):
        return super(CreatedManager, self).get_queryset().filter(created_at__lte=datetime)

    def updated(self, datetime):
        return super(CreatedManager, self).get_queryset().filter(created_at__gte=datetime)


class UpdatedManager(models.Manager):
    """
    Get all objects with Updated at criteria
    """
    def before(self, datetime):
        return super(UpdatedManager, self).get_queryset().filter(updated_at__lte=datetime)

    def updated(self, datetime):
        return super(UpdatedManager, self).get_queryset().filter(updated_at__gte=datetime)


class ActiveManager(models.Manager):
    """
    Get all objects with Activity criteria
    """

    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(is_active=True)


class InactiveManager(models.Manager):
    """
    Get all objects with Activity criteria
    """
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(is_active=False)


class DeletedManager(models.Manager):
    """
    Handle deleted objects
    """
    def get_queryset(self):
        return super(DeletedManager, self).get_queryset().filter(is_deleted=False)

    def deleted(self):
        return super(DeletedManager, self).get_queryset().filter(is_deleted=True)


class ContentManager(models.Manager):
    """
    Handle deleted objects
    """
    def home(self):
        return super(DeletedManager, self).get_queryset().filter(home=True)
    
    def not_home(self):
        return super(DeletedManager, self).get_queryset().filter(home=False)

    def pulished(self):
        return super(DeletedManager, self).get_queryset().filter(is_deleted=True)

    def not_pulished(self):
        return super(DeletedManager, self).get_queryset().filter(is_deleted=False)
