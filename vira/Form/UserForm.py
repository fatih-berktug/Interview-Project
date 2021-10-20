from django import forms
from django.contrib.auth.models import User
from vira.Form.BaseForm import BaseForm
class UserForm(BaseForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {'first_name': 'İsim *', 'last_name': 'Soyisim *', 'email': 'Email *'}
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text ', 'value': '', "style": "text-transform:uppercase",'required': 'required'
                       }),
            'last_name': forms.TextInput(
                attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text ',  "style": "text-transform:uppercase",'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text ', 'required': 'required'}),

        }