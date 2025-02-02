from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer


class FAQViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling FAQ operations.

    Provides CRUD operations for FAQ model with language-specific translations.
    """

    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        """
        Get FAQ queryset with translated content based on language parameter.

        Args:
            self: ViewSet instance

        Returns:
            QuerySet[FAQ]: Translated FAQ objects

        Note:
            Translations are based on 'lang' query parameter (defaults to 'en')
        """
        # Get language from query params, default to English if not specified
        lang: str = self.request.query_params.get('lang', 'en')
        queryset = super().get_queryset()

        # Update each FAQ object with translations for the specified language
        for faq in queryset:
            faq.question = faq.get_translated_question(lang)
            faq.answer = faq.get_translated_answer(lang)

        return queryset
