from django.shortcuts import render
from basicapp import forms

# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #Do something
            print("Validation Succcess")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})


def user_form_view(request):
    user_form = forms.UserDetails()

    if request.method == 'POST':
        user_form = forms.UserDetails(request.POST)

        if user_form.is_valid():

            #Do Something
            print("Accessing User data")
            print("Username: "+user_form.cleaned_data['username'])
            print("Password: "+user_form.cleaned_data['password'])

    return render(request, 'basicapp/user_page.html', {'user_form': user_form})

def blog_post_view(request):
    blog_post = forms.BlogPost()

    if request.method == 'POST':
        blog_post = forms.BlogPost(request.POST)

        if blog_post.is_valid():

            #Do Something

            print("Gathering Blog Post information")
            print("The title of your blog is: "+blog_post.cleaned_data['title'])
            print("The content of your blog is: "+blog_post.cleaned_data['text'])
    
    return render(request, 'basicapp/blog_post.html', {'blog_post': blog_post})