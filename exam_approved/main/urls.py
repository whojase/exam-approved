from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'main'

urlpatterns = [
    path('/', main_learn, name = 'main'),
    path('/questions_from_exams', questions_from_exams, name = 'questions_from_exams'),
    path('/video_guides', video_guides, name = 'video_guides'),
]