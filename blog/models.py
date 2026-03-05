from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    content = models.TextField()
    featured_image = models.CharField(max_length=512, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
