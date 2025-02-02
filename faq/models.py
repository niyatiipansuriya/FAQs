import redis
from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

# Initialize Redis
redis_client = redis.Redis(
    host='localhost',
    port=6380,
    db=0,
    decode_responses=True
)


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Predefined languages (each represented by its own field)
    question_en = models.BooleanField(default=True)  # English (Default)
    question_hi = models.BooleanField(default=True)  # Hindi
    question_gu = models.BooleanField(default=True)  # Gujarati
    question_mr = models.BooleanField(default=True)  # Marathi
    question_te = models.BooleanField(default=True)  # Telugu
    question_ta = models.BooleanField(default=True)  # Tamil
    question_bn = models.BooleanField(default=True)  # Bengali

    LANGUAGE_CHOICES = {
        'en': 'question_en',
        'hi': 'question_hi',
        'gu': 'question_gu',
        'mr': 'question_mr',
        'te': 'question_te',
        'ta': 'question_ta',
        'bn': 'question_bn',
    }

    def translate_text(self, text, target_language):
        """Helper function to translate text using googletrans."""
        translator = Translator()
        translated = translator.translate(text, dest=target_language)
        return translated.text

    def get_translated_texts(self, language_code):

        if language_code not in self.LANGUAGE_CHOICES:
            return {
                "question": self.question,
                "answer": self.answer
            }

        # Check if the question_... field for the selected language is True
        question_field = f"question_{language_code}"

        # Define a dictionary to hold translated texts
        translated_texts = {}

        # Check Redis first for cached translation of question and answer
        cache_key_question = f"faq:{self.id}:question:{language_code}"
        cache_key_answer = f"faq:{self.id}:answer:{language_code}"

        # Debugging Redis Cache: Check if it's a cache hit or miss
        cached_question = redis_client.get(cache_key_question)
        cached_answer = redis_client.get(cache_key_answer)

        if cached_question and cached_answer:
            translated_texts["question"] = cached_question
            translated_texts["answer"] = cached_answer
        else:
            if getattr(self, question_field, False):
                translated_question = self.translate_text(
                    self.question,
                    language_code
                )
                translated_answer = self.translate_text(
                    self.answer, language_code)

                redis_client.setex(
                    cache_key_question, 86400, translated_question)
                redis_client.setex(cache_key_answer, 86400, translated_answer)

                translated_texts["question"] = translated_question
                translated_texts["answer"] = translated_answer
            else:
                translated_texts["question"] = self.question
                translated_texts["answer"] = self.answer

        return translated_texts

    def __str__(self):
        return self.question
