from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Project

# Create your views here.
def index(request):
    blog_posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')[:3]
    projects = Project.objects.order_by('-created_at')[:4]
    return render(request, 'index.html', {
        'blog_posts': blog_posts,
        'projects': projects
    })

def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True)
    return render(request, 'blog_list.html', {'posts': posts})

def single_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'single_post.html', {'post': post})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def single_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'single_project.html', {'project': project})