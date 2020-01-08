from django.urls import path
from . import views

urlpatterns = [
        path('api/blogposts', views.BlogPostListAPIView.as_view(), name = 'blogpostsListAPIView'),
        path('api/blogposts/<int:pk>/', views.BlogPostRudAPIView.as_view(), name = 'blogpostsRudView'),
        path('api/categories/', views.CategoryListAPIView.as_view(), name = 'categoriesListAPIView'),
        path('api/categories/<int:pk>/', views.CategoryRudAPIView.as_view(), name = 'categoryRudView'),
        path('api/comments/', views.CommentListAPIView.as_view(), name = 'commentsListAPIView'),
        path('api/comments/<int:pk>/', views.CommentRudAPIView.as_view(), name = 'commentRudView'),

        ]

