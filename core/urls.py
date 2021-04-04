from django.urls import path
from django.views.generic import TemplateView

from .views import *

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

