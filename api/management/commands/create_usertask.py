from api.models import UserTask, ActivityPeriod
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from datetime import datetime


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            user_task = UserTask.objects.create(real_name=get_random_string(), tz = get_random_string())
            for j in range(total):
                ActivityPeriod.objects.create(user = user_task, start_time = datetime.now(), end_time = datetime.now())
