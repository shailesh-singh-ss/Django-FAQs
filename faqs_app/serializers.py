from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    """Serializer for FAQ model.

    This serializer handles the conversion of FAQ model instances
    to and from JSON format.
    """

    class Meta:
        """Meta class for FAQSerializer configuration."""
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at']
