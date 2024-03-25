from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("search/result/<query>/<engine>/",views.search_result,name="search_result"),
    path("search/",views.search,name="search"),
    path("create/private/link",views.create_private_link,name="create_private_link"),
    path("private/link/<name>/<first_color>/<second_color>/",views.private_link,name="private_link"),
    path("create/private/link/copy/<name>/<first_color>/<second_color>/",views.create_link,name="create_link"),
]