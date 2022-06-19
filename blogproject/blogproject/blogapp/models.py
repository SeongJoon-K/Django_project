from tkinter import CASCADE
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)  # 최대 타이틀의 글자 수를 제한
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True)  # 자동으로 지금 시간을 추가 하겠다.

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)  # 자동으로 지금 시간을 추가 하겠다.
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
