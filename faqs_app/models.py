from django.conf import settings
from django.db import models
from django.core.cache import cache
from ckeditor.fields import RichTextField
from googletrans import Translator


class FAQ(models.Model):
    """Model for storing Frequently Asked Questions with translations."""

    question = models.TextField(verbose_name="Question (English)")
    answer = RichTextField(verbose_name="Answer (English)")
    question_hi = models.TextField(
        verbose_name="Question (Hindi)",
        blank=True,
        null=True
    )
    answer_hi = RichTextField(
        verbose_name="Answer (Hindi)",
        blank=True,
        null=True
    )
    question_bn = models.TextField(
        verbose_name="Question (Bengali)",
        blank=True,
        null=True
    )
    answer_bn = RichTextField(
        verbose_name="Answer (Bengali)",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )

    def save(self, *args, **kwargs) -> None:
        """
        Override save method to auto-translate empty fields before saving.
        """
        translator = Translator()

        # Translate question to Hindi and Bengali if not provided
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text

        # Translate answer to Hindi and Bengali if not provided
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest='bn').text

        super().save(*args, **kwargs)

    def get_translated_question(self, language_code: str) -> str:
        """
        Get cached translated question for specified language code.

        Args:
            language_code: ISO language code ('hi' for Hindi, 'bn' for Bengali)

        Returns:
            str: Translated question text
        """
        cache_key = f'faq_{self.id}_question_{language_code}'
        cached_question = cache.get(cache_key)
        if cached_question:
            return cached_question

        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
        }
        translated_question = translations.get(language_code, self.question)
        cache.set(cache_key, translated_question, timeout=settings.CACHE_TTL)
        return translated_question

    def get_translated_answer(self, language_code: str) -> str:
        """
        Get cached translated answer for specified language code.

        Args:
            language_code: ISO language code ('hi' for Hindi, 'bn' for Bengali)

        Returns:
            str: Translated answer text
        """
        cache_key = f'faq_{self.id}_answer_{language_code}'
        cached_answer = cache.get(cache_key)
        if cached_answer:
            return cached_answer

        translations = {
            'hi': self.answer_hi,
            'bn': self.answer_bn,
        }
        translated_answer = translations.get(language_code, self.answer)
        cache.set(cache_key, translated_answer, timeout=settings.CACHE_TTL)
        return translated_answer

    def __str__(self) -> str:
        """Return string representation of FAQ."""
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
