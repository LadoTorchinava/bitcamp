from django.urls import path
from .views import index

urlpatterns = [
    path("odd_or_even/<int:number>", index),
]
