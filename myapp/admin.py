from django.contrib import admin
from myapp.models import BreakNews, Comment, SpecialNews
# Register your models here.


@admin.register(BreakNews)
class ModelSiplayAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Comment)
class ModelSiplayAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(SpecialNews)
class ModelSpecialAdmin(admin.ModelAdmin):
    list_display = ['id']
