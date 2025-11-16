from django.contrib import admin
from .models import Category, Product       # 5. добавляем модели в админку
# Register your models here.


# 6. То как будут отображаться поля в админке
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Параметры которые будут отображаться админке
    list_display = ['name', 'slug']
    # Поля которые будут заполнены автоматически
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)                    # 7.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
