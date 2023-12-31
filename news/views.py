from typing import Any
from django.db.models import Exists, OuterRef
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Post,Subscription,Category
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
class CreateNews(LoginRequiredMixin, CreateView):
    # raise_exception = True
    permission_required = ('news.create_news',)
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
class CreateArticles(LoginRequiredMixin, CreateView):
    # raise_exception = True
    permissions_required = ('news.create_articles',)
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
class UpdatePost(LoginRequiredMixin, UpdateView):
    permissions_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'news/create_post.html'

# Удаление записи
class DeletePost(LoginRequiredMixin, DeleteView):
    permissions_required = ('news.delete_post',)
    model = Post
    template_name = 'news/delete_post.html'
    success_url = reverse_lazy('home')


@login_required
@csrf_protect
def subscriptions(request):
    
    #POST-запрос
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(user=request.user, category=category).delete()

    # GET-запрос
    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed = Exists(
            Subscription.objects.filter(user = request.user, category = OuterRef('pk'))))
    
    return render(
        request, 'news/subscriptions.html', {'categories':categories_with_subscriptions})
    

def show_home(request):
    return render(request, 'news/index.html')
