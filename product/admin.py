from django.contrib import admin

from .models import Product, Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'active']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'star', 'active']

