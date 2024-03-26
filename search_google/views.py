# Controller (by Robo)
# Tạo ra phần xử lý back-end cho các chức năng
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .google import search


# Create your views here.
def search(request):
    if request.method == "POST":
        search = request.POST.get("search")

        if search:
            return redirect("search_result", query=search,)


def search_result(request, query, ai_check):
    black = blacklist.objects.filter(keyword=query).first()
    if query and (not black or black.status != "Chặn" or black.status != "Đang điều tra"):
        if "?" not in query and ai_check == 0:
            result = search.search_query(query)
            context = {"results": result}
        else:
            return redirect("ai_result", query)
    else:
        return redirect("block", query)
    return render(request, "search_result.html", context)


def index(request):
    return render(request, "search.html")


"""
Những chức năng phải làm tiếp theo (làm ngay):
- search hình ảnh
- search AI
- search file
- search nhiều ngôn ngữ
- search nhiều vùng
- đóng góp từ khóa bẩn
- xóa lịch sử
- trang trả về khi tìm kiếm từ khóa bẩn
"""
