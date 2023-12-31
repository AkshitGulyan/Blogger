from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    def __str__(self) -> str:
        return self.title + ' - by - ' + str(self.author)
    def get_absolute_url(self):
        return reverse('postdetails', args=(str(self.id)))