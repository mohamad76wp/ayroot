from django.urls import path
from .views import index, test_view

urlpatterns = [
    path("", index, name="index"),
    path("test", test_view, name="test_view"),
]
