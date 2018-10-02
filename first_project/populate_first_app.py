import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django 
django.setup()

## Faker populations script

import random
from first_app.models import Musician, Album, Website, Genre
from faker import Faker

fakegen = Faker()
genres = ['Blues', 'Jazz', 'Rock', 'Pop', 'Heavy Metal', 'Dance', 'Classical']

def add_genre():
    t = Genre.objects.get_or_create(style=random.choice(genres))[0]
    t.save()
    return t

def populate(n=5):
    for entry in range(n):

        #Get Genre for entry 

        gen = add_genre()

        #Create fake data for the entry 

        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_instrument = fakegen.job()
        fake_album_title = fakegen.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        fake_release_date = fakegen.date_this_decade(before_today=True, after_today=False)
        fake_stars = fakegen.random_digit_not_null()
        fake_url = fakegen.url(schemes=None)
        
        #first name, last name, instrument, album title, release date, stars, url, style

        #Create new Musician Entry

        musc = Musician.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, instrument=fake_instrument)[0]

        #create new Album Entry 

        alb = Album.objects.get_or_create(artist=musc, name=fake_album_title, release_date=fake_release_date, num_stars=fake_stars)[0]

        #Create new website

        web = Website.objects.get_or_create(album=alb, url=fake_url)[0]


if __name__ == '__main__':
    print("populating script")

    populate(20)
    
    print("populating complete")



