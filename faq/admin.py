from django.contrib import admin
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    exclude = (
        'question_hi', 'question_gu', 'question_mr',
        'question_te', 'question_ta', 'question_bn'
    )

    fields = ('question', 'answer')

    list_display = ('question_en', 'question')


if not admin.site.is_registered(FAQ):
    admin.site.register(FAQ, FAQAdmin)
