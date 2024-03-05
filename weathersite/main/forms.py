from django.core.exceptions import ValidationError

from django import forms


class CityForm(forms.Form):
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='')

# class EncryptionForm(forms.ModelForm):
#     class Meta:
#         model = Encryption
#         fields = ['key', 'text']
#         widgets = {
#             'key': forms.TextInput(attrs={'class': 'key-input'}),
#             'text': forms.Textarea(attrs={'class': 'text-input', 'cols': 60, 'rows': 10})
#         }
#
#     def clean_key(self):
#         key = self.cleaned_data['key']
#         if type(key) != int:
#             raise ValidationError('Key should be integer')
#         return key
