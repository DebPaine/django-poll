from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello world, from polls app!")


def detail(request, question_id):
    return HttpResponse(f"You are looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You are looking at the results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")
