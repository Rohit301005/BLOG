from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_content = models.TextField()
    published_date = models.DateField(auto_now = True)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.post_title
    

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.comment

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name