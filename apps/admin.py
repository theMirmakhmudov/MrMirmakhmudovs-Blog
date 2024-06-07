from django.contrib import admin
from .models import LatestBlogPost, Owners, Tags


@admin.register(LatestBlogPost)
class LatestBlogPostAdmin(admin.ModelAdmin):
    list_display = ("blog_name", "description", "created_at")


@admin.register(Owners)
class AdminPersonAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("tags",)
