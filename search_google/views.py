from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
def search(request):
    if request.method == "POST":
        search = request.POST.get("search")

        if search:
            return redirect("search_result", query=search,)


def search_result(request, query, engine):
    if query:
        pass
    return render(request, "search_result.html")


def index(request):
    return render(request, "search.html")


def create_private_link(request):
    if request.method == "POST":
        name = request.POST.get("name")
        first_color = request.POST.get("first_color")
        second_color = request.POST.get("second_color")

        if name and first_color and second_color:
            return redirect("create_link", name=name, first_color=first_color, second_color=second_color)
        elif name:
            return redirect("create_link", name=name, first_color="#000000", second_color="#3b71ca")
        elif first_color and second_color:
            return redirect("create_link", name="Search", first_color=first_color, second_color=second_color)
        else:
            return redirect("index")
    return render(request, "create_private_link.html")
