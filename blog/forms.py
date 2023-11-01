from django.forms import ModelForm
from django import forms
from .models import Subscriber

class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100, widget=forms.TextInput)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)