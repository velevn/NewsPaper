from django.urls import path
from .views import PostList, PostDetail, create_post,SearchNews

urlpatterns = [
    path('', PostList.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name='single_news'),
    path('create_post', create_post, name='create_post'),
    path('search_news', SearchNews.as_view(), name='search_news')
]
