from blog.models import (BlogPost, Category, Comment)
from django.contrib.auth import get_user_model
from users.models import UserProfile
from rest_framework import serializers


CustomUser = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
                'user',
                'first_name',
                'last_name',
                'email',
                ]


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
                'pk',
                'username',
                'first_name',
                'last_name',
                'email',
                'password',
                ]
        read_only_fields = ['is_staff', 'is_superuser',]
        write_only_fields = ['password']

    
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")
        email = validated_data.pop("email")
        profile = UserProfile.objects.create(user = user, first_name = first_name, last_name = last_name, email = email)
        return user

    def update(self, instance, validated_data):
            for attr, value in validated_data.items():
                if attr == 'password':
                    instance.set_password(value)
                else:
                    setattr(instance, attr, value)
            instance.save()
            return instance

    def delete(self, instance):
        instance.delete()
        return 

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
    profile = UserProfileSerializer(read_only = True)
    class Meta:
        model = BlogPost
        fields = [
            'user',
            'profile',
            'title',
            'date',
            'category',
            'body',
            #'image.url'
            'comments',
            ]
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'category',
            ]


