from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post 
from datetime import datetime

class PostList(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts_list'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_public'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/single_news.html'
    context_object_name = 'post_list'



# def news(request):
#     return render(request, 'news/news.html')
