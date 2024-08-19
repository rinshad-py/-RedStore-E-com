# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Customer

class EditAccountForm(forms.ModelForm):
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        customer_instance = kwargs.pop('customer_instance', None)
        super(EditAccountForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        if customer_instance:
            self.fields['phone'].initial = customer_instance.phone
            self.fields['address'].initial = customer_instance.address

    def save(self, commit=True):
        user = super(EditAccountForm, self).save(commit=False)
        if commit:
            user.save()
            customer_instance = self.instance.customer  # Fix the relationship access
            customer_instance.phone = self.cleaned_data['phone']
            customer_instance.address = self.cleaned_data['address']
            customer_instance.save()
        return user


    