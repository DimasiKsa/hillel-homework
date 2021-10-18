from django.core.management.base import BaseCommand
from faker import Faker
from students.models import Student


class Command(BaseCommand):

    help = u'Создание случайного пользователя'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        Student.generate_instances(total)
        print("new students")