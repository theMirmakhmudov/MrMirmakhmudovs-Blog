from django.db import models


class Owners(models.Model):
    image = models.ImageField(upload_to="person", null=True, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Owners"


class LatestBlogPost(models.Model):
    image = models.ImageField(upload_to="images", null=True, blank=True)
    image_alt = models.CharField(max_length=255)
    blog_name = models.CharField(max_length=50)
    blog_topic = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey('apps.Owners', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_name

    class Meta:
        verbose_name_plural = "LatestBlogPost"


class Tags(models.Model):
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.tags

    class Meta:
        verbose_name_plural = "Tags"

