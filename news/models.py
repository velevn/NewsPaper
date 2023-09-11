from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_user = models.IntegerField(default=0)

    def update_rating(self):
        postRating = self.post_set.aggregate(postRat=Sum('rating'))
        postRat = 0
        postRat += postRating.get('postRat')

        commentRating = self.author.comment_set.aggregate(
            commRat=Sum('rating'))
        commRat = 0
        commRat += commentRating.get('commRat')

        self.rating_user = postRat*3 + commRat
        self.save()


class Category(models.Model):
    name_category = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'

    CHOICE_CATEGORY = [
        (NEWS, 'Новости'),
        (ARTICLE, 'Статья')
    ]

    categoryType = models.CharField(
        max_length=2, choices=CHOICE_CATEGORY, default=ARTICLE)
    dateCreate = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    titlePost = models.CharField(max_length=128)
    textPost = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return "{%s}" % (self.textPost[0:124])


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    authorComment = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
