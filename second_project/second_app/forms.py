from django import forms
from second_app.models import Users, Sign_up, Drinks


class NewUserForm(forms.ModelForm):
    class Meta: 
        model = Sign_up
        fields = '__all__'

class DrinksForm(forms.ModelForm):
    class Meta:
        model = Drinks
        fields = '__all__'