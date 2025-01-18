from django.contrib import admin
from django.utils.html import format_html

from .models import Posts, Owners, Tags

@admin.action(description='Mark selected posts as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='published')



@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at", "show_owner_name", "status", "image_tag")
    list_per_page = 8
    actions = [make_published]


    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')

    def show_owner_name(self, obj):
        return obj.owner.name


@admin.register(Owners)
class AdminPersonAdmin(admin.ModelAdmin):
    list_display = ("name","image_tag")

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("tags",)
