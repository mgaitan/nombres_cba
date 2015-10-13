from django import forms

import re

CHOICES = [('apellido', 'Apellidos'),
           ('primer_nombre', '1º nombre'),
           ('segundo_nombre', '2º nombre')]

class SearchForm(forms.Form):
    options = forms.ChoiceField(choices=CHOICES)
    terms = forms.CharField()
    tipo = forms.ChoiceField(choices=[('count', 'Votantes/por clase'), ('cumsum', 'Acumulado')], initial='count')

    def clean_terminos(self):
        terms = self.cleaned_data['terminos']
        if not re.match(r'[A-Za-z\', ]*', terms):
            raise forms.ValueError('Caracteres inválidos. Separe por coma.')
        return terms