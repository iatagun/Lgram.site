from . import views
from django.urls import path


urlpatterns = [
    path('blog/', views.blog_list, name='blog'),
    path('blog/<slug:slug>/', views.single_post, name='single_post'),
    path('projects/', views.project_list, name='projects'),
    path('projects/<slug:slug>/', views.single_project, name='single_project'),
]