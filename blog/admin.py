from django.contrib import admin
from django.db import models

from .models import Article

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_title', 'is_published', 'blog_author', 'blog_url')
    list_display_links = ('id', 'blog_title')
    list_filter = ("blog_author","is_published")
    list_editable = ('is_published',)
    search_fields = ('blog_title', 'blog_content')
    list_per_page = 25

    fieldsets = [
        ("Who wrote this Blog?", {'fields': ["blog_author"]}),
        ("What is the title of this Blog?", {'fields': ["blog_title"]}),
        ("Include a photo for the Blog", {'fields': ["blog_photo"]}),
        ("Write the URL of the blog e.g rhonas-first-blog ", {'fields': ["blog_url"]}),
        ("Do you want to publish this blog? Tick for Yes", {'fields': ["is_published","blog_time"]}),
        ("Short Description of the blog", {"fields": ["short_description"]}),
        ("Content of Blog", {"fields": ["blog_content"]})
    ]

        
admin.site.register(Article,BlogAdmin)
