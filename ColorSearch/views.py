from django.shortcuts import render
from ColorSearch.data import get

def home(request):
    query = request.GET.get("q", "")
    return render(request, "index.html", get(query))

def info(request):
    return render(request, "info.html")
