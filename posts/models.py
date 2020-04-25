from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title

    @property
    def num_like(self):
        return self.liked.all().count()


LIKE_CHOICES = (
    ('like', 'like'),
    ('unlike', 'unlike')
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=150)

    def __str__(self):
        return f'{self.post.title}, {self.username}'

