import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from faqs_app.models import FAQ


@pytest.mark.django_db
def test_faq_api_with_language():
    # Create a FAQ object with translations
    FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
        question_hi="Django क्या है?",
        question_bn="ডজ্যাঙ্গো কি?",
        answer_hi="Django एक वेब फ्रेमवर्क है।",
        answer_bn="ডজ্যাঙ্গো একটি ওয়েব ফ্রেমওয়ার্ক।",
    )
    client = APIClient()

    # Test Hindi response
    response = client.get(reverse('faq-list') + '?lang=hi')
    assert response.status_code == 200
    assert response.data[0]['question'] == "Django क्या है?"
    assert response.data[0]['answer'] == "Django एक वेब फ्रेमवर्क है।"

    # Test Bengali response
    response = client.get(reverse('faq-list') + '?lang=bn')
    assert response.status_code == 200
    assert response.data[0]['question'] == "ডজ্যাঙ্গো কি?"
    assert response.data[0]['answer'] == "ডজ্যাঙ্গো একটি ওয়েব ফ্রেমওয়ার্ক।"

    # Test default (English) response
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
    assert response.data[0]['question'] == "What is Django?"
    assert response.data[0]['answer'] == "Django is a web framework."
