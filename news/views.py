from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts_list'
    paginate_by = 2


class PostDetail(DetailView):
    model = Post
    template_name = 'news/single_news.html'
    context_object_name = 'post_list'
    paginate_by = 2


class SearchNews(ListView):
    model = Post
    template_name = 'news/search_post.html'
    context_object_name = 'filter_list'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class CreatePost(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/create_post.html'


class UpdatePost(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/create_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'news/delete_post.html'
    success_url = reverse_lazy('news')

def show_home(request):
    return render(request, 'news/index.html')
