from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('books index')


def info(request):
    return HttpResponse('books info')


def info2(request, n):
    return HttpResponse(f'books {n} info')


def user(request, u1, u2):
    return HttpResponse(f'User页面u1：{u1}, u2：{u2}')

def user2(request, name, pwd):
    return HttpResponse(f'User2页面u1：{name}, u2：{pwd}')
