import json

from django.core.management.base import BaseCommand, CommandError
from diet_plan_generator import settings
from recipes.models import Receipt, ReceiptComponent, Ingredients

class Command(BaseCommand):
    help = 'Load data'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file_path', type=str, help='Get file path', )

    def handle(self, *args, **options):
        file_path = options["file_path"]
        if not file_path:
            raise CommandError("Missing file path")
        print(settings.BASE_DIR)
        with open(settings.BASE_DIR/file_path) as f:
            data = json.load(f)
            print(data)
        print(file_path)