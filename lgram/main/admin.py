from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogPost, Project

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}