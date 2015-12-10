from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.


def index(request):
    return render_to_response("index.html")


def groups(request):
    return render_to_response('groups.html')


def members(request):
    return render_to_response('members.html')


def photos(request):
    return render_to_response('photos.html')


def profile(request):
    return render_to_response('profile.html')