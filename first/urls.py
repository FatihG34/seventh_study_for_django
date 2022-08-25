from importlib.resources import path
from .views import home, student_page
from django.urls import path


urlpatterns = [
    path('', home),
    path('num/', student_page)
]
