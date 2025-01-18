from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Posts.POST_STATUS.PUBLISHED)
        )


class Owners(models.Model):
    image = models.ImageField(upload_to="images/owners", null=True, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Owners"


class Posts(models.Model):
    class POST_STATUS(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    image = models.ImageField(upload_to="images/post/%Y/%m/%d/", null=True, blank=True)
    image_alt = models.CharField(max_length=255, default="Image")
    topic = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey('apps.Owners', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=POST_STATUS.choices, default='draft')
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
        verbose_name = "Post"


class Tags(models.Model):
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.tags

    class Meta:
        verbose_name_plural = "Tags"

