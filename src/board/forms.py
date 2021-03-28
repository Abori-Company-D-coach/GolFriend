from django import forms
from .models import Board


class PostForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title', 'body')
        widgets = {
                'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
                'body': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'title': 'タイトル',
            'body': '本文',
        }

    def clean(self):
        data = super().clean()
        title = data.get('title')
        body = data.get('body')
        if len(title) > 20:
            msg = "タイトルの最大文字数は20文字です"
            self.add_error('title', msg)
        if len(body) > 100:
            msg = "本文の最大文字数は1000文字です"
            self.add_error('body', msg)
        


# from .models import PhotoModel

# class PhotoForm(forms.ModelForm):
#     class Meta:
#         model = PhotoModel
#         fields = '__all__'