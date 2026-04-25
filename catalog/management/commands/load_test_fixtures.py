from django.core.management import call_command
from django.core.management.base import BaseCommand
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalog.settings')
django.setup()

class Command(BaseCommand):
    help = 'Создаёт тестовые данные через фикстуры после удаления существующих'

    def handle(self, *args, **options):
        self.stdout.write('Удаление существующих данных...')
        from catalog.models import Product, Category
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Существующие данные удалены'))

        self.stdout.write('Загрузка тестовых данных из фикстур...')
        call_command('loaddata', 'test_fixtures')
        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно загружены из фикстур'))