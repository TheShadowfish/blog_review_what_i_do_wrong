from django.contrib import admin

from main.models import Article
from main.models import Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('pk', 'title',)

@admin.register(Category)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title',)