from django.db import models
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from announcement.models import Post 

class AnnouncementPageView(ListView):
    model = Post
    template_name = 'buletin.html'
    context_object_name = 'all_posts_list'

class AnnouncementDetailView(DetailView):
    model = Post
    template_name = 'single-blog.html'

class AnnouncementCreate(CreateView):
    model = Post
    template_name = 'announcement_new.html'
    fields = '__all__'