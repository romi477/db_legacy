from django.forms import ModelForm
from .models import Customer, Cinema



class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'



class CinemaForm(ModelForm):

    class Meta:
        model = Cinema
        fields = '__all__'
        # exclude = ['notation']
