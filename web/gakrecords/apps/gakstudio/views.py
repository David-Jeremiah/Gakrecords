from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "gakstudio/index.html")


def about(request):
    return render(request, "gakstudio/about.html")


def track(request):
    return render(request, "gakstudio/track.html")


def contact(request):
    return render(request, "gakstudio/contact.html")
