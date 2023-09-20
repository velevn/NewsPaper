from django.urls import path
from .views import PostList, PostDetail,SearchNews, CreatePost, UpdatePost,DeletePost

urlpatterns = [
    path('', PostList.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name='single_news'),
    path('create_post', CreatePost.as_view(), name='create_post'),
    path('search_news', SearchNews.as_view(), name='search_post'),
    path('<int:pk>/update',UpdatePost.as_view(), name='update_post'),
    path('<int:pk>/delete_post',DeletePost.as_view(), name='delete_post'),
]
