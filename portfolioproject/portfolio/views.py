from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def side_project(request):
    return render(request, "side-project.html")
