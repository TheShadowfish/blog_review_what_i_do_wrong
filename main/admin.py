from django.contrib import admin

from main.models import Article
from main.models import Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title',)