from .models import Blog
from django.forms import ModelForm, TextInput, Textarea

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['site_name', 'site_phone','site_time', 'site_day']

        widgets = {
            "site_name":TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите заголовок",
            }),
            "site_phone": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите телефон",
            }),
            "site_time": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите время",
            }),
            "site_day": TextInput(attrs={
                "type": "date",
            })
        }