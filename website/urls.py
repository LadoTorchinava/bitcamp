from django.urls import path
from .views import index, home, about, contact

urlpatterns = [
    path("", index),
    path('home/', home),
    path('about/', about),
    path('contact/', contact),
]