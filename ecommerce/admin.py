from django.contrib import admin
from .models import Products,Categories
# Register your models here.

@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'categories', 'date']
    list_filter = ['categories', 'date']
    search_fields = ['title']
    actions = [make_published]

admin.site.register(Products, ProductsAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Categories, CategoriesAdmin)