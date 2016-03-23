from django.shortcuts import render

from faq.models import FaqCategory
from faq.forms import FaqForm


def faq(request):
    title='Questions frequentes'
    faq_categories = FaqCategory.objects.select_related().all()
    faq_form = FaqForm()

    return render(request, 'faq/faq.html', {
        'title':title, 
        'faq_categories': faq_categories,
        'faq_form' : faq_form
        })
