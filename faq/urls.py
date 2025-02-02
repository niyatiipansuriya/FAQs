from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path(
        "api/faqs/<str:language_code>/",
        views.translated_faqs_view,
        name="translated_faqs",
    ),
    path(
        "api/faqs/",
        views.english_faqs_view,
        name="english_faqs",
    ),
]
