from django.shortcuts import render
from faq.services.faq_translations import get_all_translated_faqs
from django.shortcuts import redirect
from faq.models import FAQ


# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html")


def translated_faqs_view(request, language_code):
    translated_faqs = get_all_translated_faqs(language_code)

    return render(request, 'dashboard.html', {'faqs': translated_faqs})


def english_faqs_view(request):
    return render(request, 'dashboard.html', {'faqs': FAQ.objects.all()})