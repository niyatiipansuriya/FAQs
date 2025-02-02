import pytest
from django.test import TestCase
from faq.models import FAQ
from unittest.mock import patch


@pytest.mark.django_db
class TestFAQModel(TestCase):
    def setUp(self):
        # Create an FAQ instance for testing
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python web framework.",
            question_en=True
        )

    def test_faq_creation(self):
        """Test FAQ object creation"""
        assert self.faq.question == "What is Django?"
        assert self.faq.answer == "Django is a Python web framework."

    @patch('faq.models.Translator')  # Mocking the Translator class
    def test_translation_method(self, mock_translator):
        """Test the translation method of FAQ model"""
        # Mock the translator's translate method
        mock_translator.return_value.translate.return_value.text = (
    "Django क्या है?"
)

      
        # Call translate method
        translated_question = self.faq.translate_text(self.faq.question, 'hi')
     
        assert translated_question == "Django क्या है?"
      
    def test_get_translated_texts_cache_miss(self):
        """Test the cache miss scenario for translations"""
        # Here we test that the translations get saved to the Redis cache
        result = self.faq.get_translated_texts('hi')
        assert result['question'] == "Django क्या है?"
