from django import forms
from .models import Board, Profile


class PostForm(forms.ModelForm):
    """
    Tett作成投稿機能のフォーム
    """

    class Meta:
        model = Board
        fields = ('user_num', 'title', 'body', 'image')
        widgets = {
                'user_num': forms.TextInput(attrs={
                'class': 'form-control'
            }),
                'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
                'body': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'user_num': 'ユーザーNo',
            'title': 'タイトル',
            'body': '本文',
            'image': '画像',
        }

    def clean(self):
        data = super().clean()
        title = data.get('title')
        body = data.get('body')
        image = data.get('')
        if len(title) > 20:
            msg = "タイトルの最大文字数は20文字です"
            self.add_error('title', msg)
        if len(body) > 100:
            msg = "本文の最大文字数は1000文字です"
            self.add_error('body', msg)



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'golfriend_id', 'header_image', 'thumbnail', 'introduction')
        widgets = {
                'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
                'golfrined_id': forms.TextInput(attrs={
                'class': 'form-control'
            }),
                'introduction': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'name': 'ニックネーム',
            'golfrined_id': 'ゴルフレID',
            'header_image': 'ヘッダー画像',
            'thumbnail': 'プロフィール画像',
            'introduction': '自己紹介',
        }

    def clean(self):
        data = super().clean()
        name = data.get('name')
        golfriend_id = data.get('golfriend_id')
        header_image = data.get('')
        thumbnail = data.get('')
        introduction = data.get('introduction')
        if len(name) > 20:
            msg = "ニックネームの最大文字数は20文字です"
            self.add_error('name', msg)
        if len(golfriend_id) > 20:
            msg = "ゴルフレIDの最大文字数は20文字です"
            self.add_error('golfriend_id', msg)
        if len(introduction) > 200:
            msg = "ゴルフレIDの最大文字数は200文字です"
            self.add_error('introduction', msg)
        