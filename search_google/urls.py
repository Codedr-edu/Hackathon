# Khai báo url (by Khánh)
# Khai báo các url theo cú pháp như hướng dẫn cho các chức năng bên views.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/result/<query>/", views.search_result, name="search_result"),
    path("search/", views.search, name="search"),
]
