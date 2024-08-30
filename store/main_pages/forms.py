from django import forms
from .models import Comments, Tags, Categories, Brand


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'cols': '3'
            })
        }
        labels = {
            'content': 'Комментарий'
        }


# данный класс формы, не превз
class CreateProductForm(forms.Form):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    price = forms.DecimalField(max_digits=6, decimal_places=2, label='Цена', widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Категории', empty_label='Категории', widget=forms.Select(
        attrs={
            'class': 'form-select'
        }
    ))
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), label='Бренды', empty_label='Бренды', widget=forms.Select(
        attrs={
            'class': 'form-select'
        }
    ))
