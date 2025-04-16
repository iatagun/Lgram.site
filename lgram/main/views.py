from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Project
from django.contrib.auth.decorators import user_passes_test
from .models import ContentView
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.utils import timezone
import datetime
from .utils import log_content_view

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
    session_key = f"viewed_post_{post.id}"
    log_content_view(request, "blog", post.id)
    if not request.session.get(session_key, False):
        post.views += 1
        post.save()
        request.session[session_key] = True
    return render(request, 'single_post.html', {'post': post})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def single_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    log_content_view(request, "project", project.id)
    return render(request, 'single_project.html', {'project': project})

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    today = timezone.now()
    last_week = today - datetime.timedelta(days=6)

    base_qs = ContentView.objects.filter(timestamp__gte=last_week)

    blog_views = base_qs.filter(content_type="blog").annotate(
        day=TruncDate('timestamp')
    ).values('day').annotate(count=Count('id')).order_by('day')

    project_views = base_qs.filter(content_type="project").annotate(
        day=TruncDate('timestamp')
    ).values('day').annotate(count=Count('id')).order_by('day')

    def extract_chart(view_data):
        return {
            'labels': [entry['day'].strftime('%Y-%m-%d') for entry in view_data],
            'counts': [entry['count'] for entry in view_data]
        }

    blog_data = extract_chart(blog_views)
    project_data = extract_chart(project_views)

    total_blog = sum(blog_data['counts'])
    total_project = sum(project_data['counts'])
    total_all = total_blog + total_project

    return render(request, 'dashboard.html', {
        'blog_labels': blog_data['labels'],
        'blog_counts': blog_data['counts'],
        'project_counts': project_data['counts'],
        'total_blog': total_blog,
        'total_project': total_project,
        'total_all': total_all,
    })
def log_content_view(request, content_type, object_id):
    ip = request.META.get('REMOTE_ADDR', '')
    ContentView.objects.create(content_type=content_type, object_id=object_id, ip_address=ip)