from django.db import models


class Board(models.Model):
    """Tett作成掲示板モデル
    Written by Tett
    """
    # posted_by = models.CharField(max_length=20)
    user_num = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images', verbose_name='投稿画像')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "board"



class Profile(models.Model):
    """プロフィール用モデル
    Written by Tett
    """
    name = models.CharField('ニックネーム', max_length=100)
    golfriend_id = models.CharField('ゴルフレID', max_length=20)
    header_image = models.ImageField(upload_to='images', verbose_name='ヘッダー画像')
    thumbnail = models.ImageField(upload_to='images', verbose_name='サムネイル')
    introduction = models.TextField('自己紹介', max_length=100, null=True, blank=True)    
    
    class Meta:
        db_table = "profile"


# "Koo作成掲示板"
# class BoardModel(models.Model):
#     "Koo作成掲示板Model"
#     "Written by Koo"
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     author = models.CharField(max_length=50)
#     snsimage = models.ImageField(upload_to='')
#     good = models.IntegerField(null=True, blank=True, default=1)
#     read = models.IntegerField(null=True, blank=True, default=1)
#     readtext = models.TextField(null=True, blank=True, default='a')