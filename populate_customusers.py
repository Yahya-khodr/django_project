import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

import django
django.setup()

from customuser.models import customUser
from faker import Faker
fake = Faker()


def username(num_of_name=5):
    
    for i in range(num_of_name):
        fake_fname = fake.first_name()
        fake_lname=fake.last_name()
        fake_email = fake.ascii_free_email()
        user= customUser.objects.create(
            firstName=fake_fname,
            lastName=fake_lname,
            email=fake_email)
        user.save()
       
        

if __name__ == "__main__" :
    username(5)