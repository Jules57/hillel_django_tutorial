from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from faker import Faker


class Command(BaseCommand):
    help = 'Creates the specified number of random users'

    def add_arguments(self, parser):
        parser.add_argument('user_count', type=int)

    def handle(self, *args, **options):
        faker = Faker()
        user_count = options['user_count']
        if user_count < 1 or user_count > 10:
            raise CommandError('The valid number is from 1 to 10. Enter a valid number.')
        for user in range(user_count):
            user_name = faker.user_name()
            user_email = faker.email()
            user_password = faker.password()
            user, created = User.objects.update_or_create(username=user_name, email=user_email, password=user_password)
            # self.stdout.write(f'Username: {user_name}, email: {user_email}, password: {user_password}')
            self.stdout.write(str(user))
