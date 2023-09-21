from django.urls import path
from .views import ArticlesList, PostDetail,CreateArticles, UpdatePost,DeletePost

urlpatterns = [
    path('', ArticlesList.as_view(), name='articles'),
    path('<int:pk>', PostDetail.as_view(), name='single_post'),
    path('create_articles', CreateArticles.as_view(), name='create_articles'),
    path('<int:pk>/update',UpdatePost.as_view(), name='update'),
    path('<int:pk>/delete',DeletePost.as_view(), name='delete'),
]
