from django import forms
from .models import Customer, Cinema



class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'



class CinemaForm(forms.ModelForm):

    class Meta:
        model = Cinema
        fields = '__all__'
        # exclude = ['notation']
