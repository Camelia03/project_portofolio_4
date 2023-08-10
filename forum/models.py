from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()

    def __str__(self):
        return self.user.username
