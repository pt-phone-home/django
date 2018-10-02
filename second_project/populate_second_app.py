import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django 
django.setup()

#Faker Population Script

import random 
from second_app.models import Users
from faker import Faker

fakegen = Faker()

def populate(n=50):
    for entry in range(n):

        #Create fake data 

        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.ascii_email()

        #Create User Entry

        prof = Users.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print("Populating Script")

    populate(50)

    print("Populating complete!")