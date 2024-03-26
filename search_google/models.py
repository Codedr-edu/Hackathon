# Khai báo các database kiểu ORM (by Duy Tùng)
# khai báo các bảng như ví dụ dưới

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class blacklist(models.Model):  # Khai báo blacklist
    keyword = models.TextField()  # cột keyword
    status = models.TextField()  # Mức độ chặn
