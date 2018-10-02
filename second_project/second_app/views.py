from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import Users, Sign_up
from second_app.forms import NewUserForm, DrinksForm
# Create your views here.

def list(request):
    user_list = Users.objects.order_by('last_name')

    user_list_dict = { 'user_list': user_list }

    return render(request, 'second_app/list.html', context=user_list_dict)

def index(request):
    return render(request, 'second_app/index.html')

def sign_up(request):

    form = NewUserForm()

    if request.method == 'POST':

        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else: 
            print("ERROR FORM INVALID")
    
    return render(request, 'second_app/sign_up.html', {'form': form})

def drinks(request):

    drinks_form = DrinksForm()

    if request.method == 'POST':
        drinks_form = DrinksForm(request.POST)

        if drinks_form.is_valid():
            drinks_form.save(commit=True)
            return index(request)
        else:
            print("Error processing your form")

    return render(request, 'second_app/drinks.html', {'drinks_form': drinks_form})