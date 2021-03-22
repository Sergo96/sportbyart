from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class CommentSerializer(serializers.ModelSerializer):
    # article = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ["user_name", "email", "comment_content", "article"]


class CategoryArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['content']


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ["header", "about_us_content"]


class SubscribeSerializer(serializers.ModelSerializer):
    subscriber_name = serializers.CharField(max_length=20)
    subscriber_email = serializers.EmailField()

    class Meta:
        model = Subscribe
        fields = "__all__"


class SearchSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
