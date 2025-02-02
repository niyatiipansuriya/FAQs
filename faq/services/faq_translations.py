from faq.models import FAQ
import html


def decode_html_entities(faqs):
    for faq in faqs:
        if isinstance(faq, dict) and 'answer' in faq:
            # Check if the answer contains HTML entities that need decoding
            if any(char in faq['answer'] for char in
                   ['&', '<', '>', '"', "'"]):
                faq['answer'] = html.unescape(faq['answer'])
    return faqs


def get_all_translated_faqs(language_code):
    faqs = FAQ.objects.all()

    translated_faqs = []

    for faq in faqs:
        translated_faq = faq.get_translated_texts(language_code)
        translated_faq['id'] = faq.id

        translated_faqs.append(translated_faq)

    # Decode the HTML entities in the answers
    translated_faqs = decode_html_entities(translated_faqs)

    return translated_faqs
