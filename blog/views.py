from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Comments


# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # filter only published posts
    queryset = Post.objects.filter(status='publish')
    ordering = ['-created_on'] # newest posts first
    paginate_by = 5


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Tk Codes'
        return context


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'



class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

