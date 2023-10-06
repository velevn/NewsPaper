from django.contrib import admin
from .models import Author, Post, Comment, Category,Subscription


# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Subscription)
admin.site.register(Category)