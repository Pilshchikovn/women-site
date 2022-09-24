from django import forms

from .models import *


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255,label='Заголовок')
#     slug = forms.SlugField(max_length=255, label='Слаг')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),label='Текст')
#     is_published = forms.BooleanField(label='опубликовать',required=False,initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(),label='Категория',empty_label='Категория не выбрана')

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Women
        # fields = '__all__'
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'contant': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
