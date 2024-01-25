from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Post(models.Model):
    # Check if a post is published on not
    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    body = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.CharField(max_length=55)

    # Order by when the post was created

    class Meta:
        ordering = ['-created_on']

    # for posts to appear with the title rather than objects
    def __str__(self):
        return self.title
    

class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'