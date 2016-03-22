from django.forms import ModelForm
from django.contrib.admin import ModelAdmin

from redactor.widgets import RedactorEditor

from .models import Category, Post


class PostContentForm(ModelForm):
    """
    Form used in admin
    """
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': RedactorEditor()
        }



class CategoryForm(ModelForm):
    pass
    # class Meta:
    #     model = Category
    #     fields = '__all__'
    #     widgets = {
    #         'bg_color': HTML5Input(input_type='color'),
    #         'font_color': HTML5Input(input_type='color'),
    #     }

