from django.urls import path
from .views import PostList, PostDetail, create_post

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('create_post', create_post),
]
