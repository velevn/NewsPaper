from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts_list'
    paginate_by = 2

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/single_news.html'
    context_object_name = 'post_list'


def show_home(request):
    return render(request,'news/index.html')


def create_post(request):
    form = PostForm()
    return render(request,'news/create_post.html', {'form':form})
