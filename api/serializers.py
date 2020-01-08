from blog.models import (BlogPost, Category, Comment)

from rest_framework import serializers


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



class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only = True)
    class Meta:
        model = BlogPost
        fields = [
            'user',
            'title',
            'date',
            'body',
            'category',
            #'image.url'
            'comments',
            ]
        depth = 1

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'category',
            ]


