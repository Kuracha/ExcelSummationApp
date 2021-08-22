"""Core api serializers."""
# 3rd-party
import pandas as pd
from rest_framework import serializers

# Local
from ..models import Column
from ..models import ExcelFile
from ..validators import validate_file_extension


class ExcelFileSerializer(serializers.ModelSerializer):  # noqa:D101
    file = serializers.FileField(validators=[validate_file_extension])
    fields = serializers.ListField(child=serializers.CharField(max_length=100, default=''), write_only=True)
    header_row = serializers.IntegerField(write_only=True)
    nrows = serializers.IntegerField(write_only=True)

    def create(self, validated_data):  # noqa:D102
        pop_fields = validated_data.pop('fields')
        pop_header_row = validated_data.pop('header_row')-1
        pop_nrows = validated_data.pop('nrows')
        excel_file = super().create(validated_data)
        excel = pd.read_excel(excel_file.file.path, header=pop_header_row, nrows=pop_nrows)
        excel.columns = excel.columns.str.strip()
        for field in pop_fields:
            summary = excel[field].sum()
            average = excel[field].mean()
            Column.objects.create(column=field, summary=summary, average=average, excel_file=excel_file)
        return excel_file

    class Meta:  # noqa:D106
        model = ExcelFile
        fields = [
            'file',
            'fields',
            'header_row',
            'nrows',
        ]


class ColumnSerializer(serializers.ModelSerializer):  # noqa:D101

    class Meta:  # noqa:D106
        model = Column
        fields = [
            'column',
            'summary',
            'average',
        ]


class GetExcelFileSerializer(serializers.ModelSerializer):  # noqa:D101
    summary = ColumnSerializer(many=True)

    class Meta:  # noqa:D106
        model = ExcelFile
        fields = [
            'file',
            'summary',
        ]
