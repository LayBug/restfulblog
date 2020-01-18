from .serializers import (BlogPostSerializer, CategorySerializer, CommentSerializer, UserModelSerializer)
from users.models import CustomUser
from rest_framework import generics
from rest_framework.permissions import (IsAdminUser, IsAuthenticatedOrReadOnly)
from blog.models import (BlogPost, Category, Comment)


class BlogPostListAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminUser]

class BlogPostRudAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_class = [IsAdminUser]
    lookup_field = 'pk'



class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryRudAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_class = [IsAdminUser]
    lookup_field = 'pk'



class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []

class CommentRudAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'


class UserListAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = []

class UserRudAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
    permission_class = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'


