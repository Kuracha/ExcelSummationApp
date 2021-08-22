"""Core models."""
# Django
from django.db import models


class ExcelFile(models.Model):  # noqa:D101
    file = models.FileField('Uploaded file', upload_to='excel_files')

    class Meta:  # noqa:D106
        verbose_name = 'Excel File'
        verbose_name_plural = 'Excel Files'

    def __str__(self):  # noqa:D105
        return str(self.id)


class Column(models.Model):  # noqa:D101
    column = models.CharField('Column name', max_length=60)
    summary = models.DecimalField('Summary value', decimal_places=2, max_digits=10)
    average = models.DecimalField('Average value', decimal_places=2, max_digits=10)
    excel_file = models.ForeignKey(
        ExcelFile,
        on_delete=models.CASCADE,
        related_name='summary',
        verbose_name='Excel File',
    )

    class Meta:  # noqa:D106
        verbose_name = 'Column'
        verbose_name_plural = 'Columns'

    def __str__(self):  # noqa:D105
        return str(self.id)
