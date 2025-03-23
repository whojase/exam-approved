from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import *

def index(request):
    return render(request, 'main/index.html')

def main_learn(request):
    main = MainLearn.objects.all()
    context = {
        'main': main
    }
    return render(request, 'main/learn_main.html', context)

def questions_from_exams(request):
    questions_from_exams = QuestionsFromExams.objects.all()
    context = {
        'questions_from_exams': questions_from_exams
    }
    return render(request, 'main/questions_from_exams.html', context)

def video_guides(request):
    video_guides = VideoGuides.objects.all()
    context = {
        'video_guides': video_guides
    }
    return render(request, 'main/video_guides.html', context)
