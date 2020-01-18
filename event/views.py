from django.shortcuts import render


def index(request):
    return render(request, "event/index.html", {})


def table(request):
    return render(request, "event/table.html", {})
