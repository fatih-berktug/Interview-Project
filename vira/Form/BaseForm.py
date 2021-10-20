from django import forms
class BaseForm(forms.ModelForm):

    def save(self, request, *args, **kwargs):
        print('base log alanı')
        return super().save()
