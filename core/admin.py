"""Core Admin."""
# Django
from django.contrib import admin

# Project
from core.models import Column
from core.models import ExcelFile


class ColumnInline(admin.TabularInline):  # noqa:D101
    model = Column
    extra = 0
    fields = [
        'column',
        'summary',
        'average',
    ]


@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):  # noqa:D101
    fields = [
        'file',
    ]
    inlines = [ColumnInline]
