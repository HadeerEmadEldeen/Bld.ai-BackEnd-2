from django.urls import path
from .views import *

urlpatterns = [
   path("", Courses.as_view()), 
   path("<int:id>/", oneCourse.as_view()),
]