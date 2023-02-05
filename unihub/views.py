import os

from django.shortcuts import render
from django.http import Http404


def home(request):
    return render(request, "unihub/home.html")


def custom_handler404(request, exception):
    return render(request, "unihub/404.html", status=404)  # not found


def custom_handler500(request):
    return render(request, "unihub/500.html", status=500)  # internal server error


def custom_handler403(request, exception):
    return render(request, "unihub/403.html", status=403)  # forbidden


def custom_handler400(request, exception):
    return render(request, "unihub/400.html", status=400)  # bad request
