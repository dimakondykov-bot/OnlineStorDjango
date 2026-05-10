from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание товара"
    )
    image = models.ImageField(
        upload_to="products/photo",
        verbose_name="Фото",
        help_text="Приложите фото товара",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Категория",
        related_name="products",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена",
        help_text="Введите цену товара",)
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "created_at", "updated_at"]

    def __str__(self):
        return self.name
