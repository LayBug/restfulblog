from django.db import models
from  project.settings import AUTH_USER_MODEL


class Category(models.Model):
    category = models.CharField(max_length = 60)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class BlogPost(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.CASCADE)
    title = models.CharField(max_length = 60)
    date = models.DateField('Publication Date', )
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    body = models.TextField()
    #image = models.ImageField(upload_to = 'images')

    def __str__(self):
        return self.title



class Comment(models.Model):
    name = models.CharField(max_length = 60)
    date = models.DateTimeField()
    email = models.EmailField()
    post = models.ForeignKey(BlogPost, on_delete = models.CASCADE, related_name = "comments")
    comment = models.TextField()


    def __str__(self):
        return self.comment

