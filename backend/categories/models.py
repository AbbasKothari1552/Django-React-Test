from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='category_avatars/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    SubCategory_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='subcategory_avatars/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


