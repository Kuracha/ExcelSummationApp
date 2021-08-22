"""Core api urls."""
# Django
from django.urls import path

# Local
from .views import RetrieveExcelFileView
from .views import UploadExcelFileView

urlpatterns = [
    path('upload_file/', UploadExcelFileView.as_view()),
    path('get_file/<pk>/', RetrieveExcelFileView.as_view()),
]
