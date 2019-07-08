from django.db import models
from django.utils import timezone
# Create your models here.

class Post (models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    text = models.TextField()
    created_date = models.DateTimeField(default= timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def summary(self):
        if self.title[6:]:
            return self.title[ :6]+ "..."
        else:
            return self.title

class Comment(models.Model):
    post=models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text