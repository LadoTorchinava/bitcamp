from django.urls import path
from .views import index

urlpatterns = [
    path("website/<str:name>",index),
]