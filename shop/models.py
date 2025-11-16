from django.db import models

# Create your models here.


class Category(models.Model):  # 2. Создаем первую модель
    name = models.CharField(max_length=100, db_index=True)
    # Уникальный параметр, для генерации юрл наших продуктов
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:  # 3. Создание класса мета для раболты на русском языке
        ordering = ('name',)
        verbose_name = 'Категория'              # Отиображение на русском в ед числе
        verbose_name_plural = 'Категории'       # Отображение во вмножественном числе

    def __str__(self):
        return self.name


class Product(models.Model):  # 4. Создаем таблицу для продуктов
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=100)
    # Куда будут загружаться фото продуктов. Второй параметр значит что поле фото мсожет быть пустое
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    # Описание товара, 2 параметр значит что можно не задавать описание товара
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Доступность товара т.е. есть товар или его нет
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
