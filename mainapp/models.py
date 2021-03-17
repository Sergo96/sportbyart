from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Name', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    subname = models.CharField('subname', max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subname

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategory'


class Article(models.Model):
    title = models.CharField('Title', max_length=30)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField('Image', upload_to="article")
    short_desc = models.CharField("Short description", max_length=200)
    content = models.TextField('Content')
    publication = models.DateTimeField('Publication', auto_now_add=True)
    ratings = models.PositiveIntegerField('ratings', default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-publication']


class Comment(models.Model):
    user_name = models.CharField('user name', max_length=20)
    email = models.EmailField('Email')
    comment_content = models.TextField('Comment content')
    publication_date = models.DateTimeField('publication date', auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class AboutUs(models.Model):
    header = models.CharField('header', max_length=200)
    about_us_content = models.TextField()

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUs'


class Subscribe(models.Model):
    subscriber_name = models.CharField('subscriber name', max_length=70)
    subscriber_email = models.EmailField('subscriber email')

    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribe'

    def __str__(self):
        return self.subscriber_email
