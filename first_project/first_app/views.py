from django.shortcuts import render
from django.http import HttpResponse 
from first_app.models import Musician, Website, Album, Genre
# Create your views here.

def index(request):

    webpages_list = Musician.objects.order_by('last_name')

    last_name_dict = {'musician_list': webpages_list}

   # my_dict = {'insert_me': "Hello I am from views.py", 
    #            'also_me' : "I am a second variable", 
     #           'one_more' : "and one more for good measure"
      #          }
    return render(request, 'first_app/index.html', context=last_name_dict)


