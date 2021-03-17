from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.renderers import JSONRenderer
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import *


class ArticlesView(APIView):
    def get(self, request, count="all"):
        if count == 'all':
            article = Article.objects.all()
            serializer_data = ArticleSerializer(article, many=True)
            # json = JSONRenderer().render(serializer_data.data)
            return Response(serializer_data.data, status=status.HTTP_200_OK)
        else:
            count = int(count)
            article = Article.objects.all()[:count]
            serializer_data = ArticleSerializer(article, many=True)
            # json = JSONRenderer().render(serializer_data.data)
            return Response(serializer_data.data, status=status.HTTP_200_OK)


class ArticleView(APIView):
    def get(self, request, id):
        id = int(id)
        article = Article.objects.filter(id=id)
        serializer_data = ArticleSerializer(article, many=True)
        # json = JSONRenderer().render(serializer_data.data)
        return Response(serializer_data.data, status=status.HTTP_200_OK)


class CommentsView(APIView):
    def get(self, request, article_id):
        article_id = int(article_id)
        comments = Comment.objects.filter(article=article_id)
        serializer_data = CommentSerializer(comments, many=True)
        # json = JSONRenderer().render(serializer_data.data)
        return Response(serializer_data.data, status=status.HTTP_200_OK)


class AddCommentView(APIView):
    def post(self, request):
        comment = CommentSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer_data = CategorySerializer(categories, many=True)
        # json = JSONRenderer().render(serializer_data.data)
        return Response(serializer_data.data, status=status.HTTP_200_OK)


class CategoryView(APIView):
    def get(self, request, category_id, page):
        article_list = Article.objects.filter(category=category_id)

        paginator = Paginator(article_list, 10)

        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        serializer_data = CategoryArticlesSerializer(articles, many=True)

        return Response(serializer_data.data, status=status.HTTP_200_OK)


class AboutUsView(APIView):
    def get(self, request):
        aboutus = AboutUs.objects.all()[:1]
        serializer_data = AboutUsSerializer(aboutus, many=True)
        return Response(serializer_data.data, status=status.HTTP_200_OK)


class SubscribeView(APIView):
    def post(self, request):
        sub_serializer = SubscribeSerializer(data=request.data)
        if sub_serializer.is_valid():
            sub_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(sub_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
