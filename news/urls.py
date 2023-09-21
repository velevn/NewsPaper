from django.urls import path
from .views import NewsList, PostDetail,SearchNews, CreateNews, UpdatePost,DeletePost

urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name='single_post'),
    path('create_news', CreateNews.as_view(), name='create_news'),
    path('search_post', SearchNews.as_view(), name='search_post'),
    path('<int:pk>/update',UpdatePost.as_view(), name='update'),
    path('<int:pk>/delete',DeletePost.as_view(), name='delete'),
]
