from importlib.resources import path
from .views import home, student_num
from django.urls import path


urlpatterns = [
    path('', home),
    path('num/', student_num)
]
