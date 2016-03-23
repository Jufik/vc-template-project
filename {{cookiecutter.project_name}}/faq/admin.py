from django.contrib import admin
from faq.models import Faq, FaqCategory 

# Register your models here.
class FaqAdmin(admin.ModelAdmin):
    '''
        Admin View for Faq
    '''
    list_display = ('category', 'question', 'order')
    list_filter = ('category',)


# admin.site.register(Faq, FaqAdmin)


class FaqInline(admin.TabularInline):
    '''
    Tabular Inline View for Faq
    '''
    model = Faq
    max_num = 20
    extra = 0


class FaqCategoryAdmin(admin.ModelAdmin):
    '''
        Admin View for FaqCategory
    '''
    list_display = ('order','name')

    inlines = [
        FaqInline,
    ]

admin.site.register(FaqCategory, FaqCategoryAdmin)