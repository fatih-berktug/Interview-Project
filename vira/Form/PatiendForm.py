from django import forms
from vira.Form.BaseForm import BaseForm
from vira.Model.Patient import Patient
class PatiendForm(BaseForm):
    class Meta:
        model = Patient
        fields = ('name',  'surname', 'tc','cancerType')
        labels = {'name': 'İsim ',
                  'surname': 'Soyisim',
                  'tc': 'T.C. Kimlik Numarası',
                  'cancerType': 'Kanse Türü'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text', 'required': 'required'}),
            'surname': forms.TextInput(attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text ', 'required': 'required'}),
            'tc': forms.NumberInput(attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text', 'required': 'required'}),
            'cancerType':  forms.Select(attrs={'class': 'woocommerce-Input woocommerce-Input--text input-text select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; '}),
        }