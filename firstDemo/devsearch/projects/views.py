from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return HttpResponse('Hello world')

def projects(request):
    return HttpResponse('Here are projects')

def project(request,pk):
    return HttpResponse('this is single project ' + pk)