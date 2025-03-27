from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'codehigh/index.html')


def courses(request):
    return render(request, "codehigh/courses.html")


def about(request):
    return render(request, "codehigh/about.html")


def events(request):
    return render(request, "codehigh/events.html")


def contact(request):
    return render(request, "codehigh/contact.html")


def teacher(request):
    return render(request, "codehigh/teacher.html")


def scholarship(request):
    return render(request, "codehigh/scholarship.html")


def notice(request):
    return render(request, "codehigh/notice.html")


def research(request):
    return render(request, "codehigh/research.html")
