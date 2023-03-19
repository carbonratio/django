import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','user_project.settings')

import django
django.setup()

from user_app.models import User
from faker import Faker

def populate(N=5):
    f = Faker()
    for _ in range(N):
        User.objects.get_or_create(first_name=f.first_name(), last_name=f.last_name(),email = f.email())

if __name__ == '__main__':
    print('populating users!')
    populate(20)
    print('finished populating users!')