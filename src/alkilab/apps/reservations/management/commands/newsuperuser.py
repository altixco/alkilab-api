from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a new superuser if not exist'

    def add_arguments(self, parser):
        parser.add_argument('user', nargs='+', type=str)
        parser.add_argument('password', nargs='+', type=str)
        
    def handle(self, *args, **options):
        
        superusers = User.objects.filter(is_superuser=True)
        user = options['user']
        if not superusers:
            for user in options['user']:
                for password in options['password']:
                    User.objects.create_superuser(user, "admin@example.com", password)
                    self.stdout.write(self.style.SUCCESS('The superadmin: %s has been created succesfully! ' % user)) 
        self.stdout.write(self.style.SUCCESS('There is a superuser created already! '))
        return