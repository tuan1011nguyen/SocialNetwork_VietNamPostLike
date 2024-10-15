from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    date_post = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_likes = models.IntegerField(default=0)  # Rename this field

    def __str__(self):
        return f'{self.title} by {self.author.username} on {self.date_post.strftime("%Y-%m-%d")}'

    
class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')  # Add related_name

    def __str__(self):
        return f'{self.author} likes {self.post.title}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content_cmt = models.TextField()
    date_cmt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author} comment on {self.post.title}'
