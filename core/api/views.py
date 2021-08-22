"""Core api views."""
# 3rd-party
from rest_framework import generics

# Local
from ..models import ExcelFile
from .serializers import ExcelFileSerializer
from .serializers import GetExcelFileSerializer


class UploadExcelFileView(generics.CreateAPIView):  # noqa:D101
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer


class RetrieveExcelFileView(generics.RetrieveAPIView):  # noqa:D101
    queryset = ExcelFile.objects.all()
    serializer_class = GetExcelFileSerializer
