from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """Admin configuration for FAQ model."""

    # Display fields in the list view
    list_display = (
        'question',
        'question_hi',
        'question_bn',
        'created_at',
    )

    # Filter options in the admin interface
    list_filter = ('created_at',)

    # Fields that can be searched in the admin interface
    search_fields = (
        'question',
        'question_hi',
        'question_bn',
    )

    # Organize fields into logical sections
    fieldsets = (
        (_('English Content'), {
            'fields': ('question', 'answer'),
        }),
        (_('Hindi Translation'), {
            'fields': ('question_hi',),
        }),
        (_('Bengali Translation'), {
            'fields': ('question_bn',),
        }),
    )

    # Enable date-based navigation
    date_hierarchy = 'created_at'
