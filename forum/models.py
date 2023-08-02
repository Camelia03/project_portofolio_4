from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
