from django.db import models

from account.models import User

class Post(models.Model):
    title = models.CharField("제목", max_length=50)
    content = models.TextField("내용")
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField("내용")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
