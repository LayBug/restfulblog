from blog.models import (BlogPost, Category, Comment)

from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'user',
            'title',
            'date',
            'body',
            'category',
            #'image.url'
            ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'category',
            ]




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'name',
            'email',
            'date',
            'comment',
            'post',
            ]


