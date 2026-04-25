import os
import django
from django.core.management import call_command
from django.core.management.base import BaseCommand



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalog.settings')  # Замените на ваш путь
django.setup()

class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур'

    def add_arguments(self, parser):
        parser.add_argument(
            '--fixture',
            type=str,
            default='test_products',
            help='Имя фикстуры для загрузки (без расширения)'
        )
        parser.add_argument(
            '--no-delete',
            action='store_true',
            help='Не удалять существующие данные перед загрузкой'
        )

    def handle(self, *args, **options):
        fixture_name = options['fixture']


        self.stdout.write()


        self.stdout.write()
        call_command('loaddata', fixture_name)
        self.stdout.write(
            self.style.SUCCESS('Фикстура загружена')
        )
