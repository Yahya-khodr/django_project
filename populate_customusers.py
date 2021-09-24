import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

import django
django.setup()

from customuser.models import customUser
from faker import Faker
fake = Faker()


def username(num_of_name=10):
    for i in range(num_of_name):
        faker_fname = fake.first_name()
        faker_lname=fake.last_name()
        name= customUser.objects.create(firstName=faker_fname,lastName=faker_lname)
        name.save()
        

if __name__ == "__main__" :
    username(20)