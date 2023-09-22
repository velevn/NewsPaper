from collections.abc import Sequence
from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


# Выводим список всех новостей
class NewsList(ListView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'posts_list'
    paginate_by = 2
    
    def get_queryset(self):
        category_type = Post.objects.filter(categoryType='NW')
        return category_type
    

# Вывод отдельной новости
class NewsDetail(DetailView):
    model = Post
    template_name = 'news/single_post.html'
    context_object_name = 'post_list'

    def news_detail(request, pk):
        post_id = Post.objects.get(pk=pk)
        if post_id.categoryType == 'NW':
            return render(request, 'news/single_post.html',context={'post_list':post_id})
        else:
            return render(request, 'news/404.html')


# Создание новости
class CreateNews(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/create_post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)
    
    
# Выводим список всех статей
class ArticlesList(ListView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'posts_list'
    paginate_by = 2

    def get_queryset(self):
        category_type = Post.objects.filter(categoryType='AR')
        return category_type

# Вывод отдельной статьи
class ArticlesDetail(DetailView):
    model = Post
    template_name = 'news/single_post.html'
    context_object_name = 'post_list'

    def articles_detail(request, pk):
        post_id = Post.objects.get(pk=pk)
        if post_id.categoryType == 'AR':
            return render(request, 'news/single_post.html',context={'post_list':post_id})
        else:
            return render(request, 'news/404.html')


# Создание статьи
class CreateArticles(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/create_post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)
    

# Вывод отдельной записи
class PostDetail(DetailView):
    model = Post
    template_name = 'news/single_post.html'
    context_object_name = 'post_list'


# Поиск записи
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

# Обновление записи
class UpdatePost(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/create_post.html'

# Удаление записи
class DeletePost(DeleteView):
    model = Post
    template_name = 'news/delete_post.html'
    success_url = reverse_lazy('home')


def show_home(request):
    return render(request, 'news/index.html')
