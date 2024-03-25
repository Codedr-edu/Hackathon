from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class blacklist(models.Model):  # Khai báo blacklist
    keyword = models.TextField()  # cột keyword
    status = models.TextField()  # Mức độ chặn


class history(models.Model):  # Khai báo lịch sử search
    url = models.TextField()  # url
    keyword = models.TextField()  # keyword_search
    time = models.DateTimeField(auto_add_now=True)  # thời gian
    user = models.ForeignKey(User)  # Liên kết với người dùng
