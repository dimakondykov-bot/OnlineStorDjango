from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = " add test catalog to the database"

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(
        name="Элетроника",
        description="Умная техника",
        )

        Product.objects.create(
            name="ноутбук",
            description="Игровой ноутбук",
            price="95000",
            category=category,
        )

        self.stdout.write(self.style.SUCCESS("БД успешно заполнена"))

