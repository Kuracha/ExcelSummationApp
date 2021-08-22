"""Core validators."""
# Standard Library
import os

# Django
from django.core.exceptions import ValidationError


def validate_file_extension(value):  # noqa:D103
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
