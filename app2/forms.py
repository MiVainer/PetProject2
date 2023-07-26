from .models import Artiles
from django.forms import ModelForm, TextInput, Textarea


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['skill', 'opisanie', 'full_text']

        widgets = {
            'skill': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название навыка'
            }),
            'opisanie': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание навыка'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание применения'
            })

        }
