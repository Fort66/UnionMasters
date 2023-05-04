from .models import News
from django.forms import ModelForm, TextInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['NewsTitle', 'NewsAnonce', 'NewsBody', 'NewsPhoto']
        labels = {
            'NewsTitle': 'Заголовок',
            'NewsBody': 'Текст',
            'NewsPhoto': 'Фото',
        }

        widgets = {
            'NewsTitle': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок новости',
                }),
            'NewsAnonce': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс новости',
                }),
            'NewsBody': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст новости',
                }),
            # 'NewsPhoto': ImageField(attrs={
            #     'class': 'form-control-file',
            #     'placeholder': 'Фото',
            #     }),
        }

        