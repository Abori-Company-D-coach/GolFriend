from django.db import models


class BoardModel(models.Model):
    "Koo作成掲示板Model"
    "Written by Koo"
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    snsimage = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=1)
    read = models.IntegerField(null=True, blank=True, default=1)
    readtext = models.TextField(null=True, blank=True, default='a')



class Board(models.Model):
    "Tett作成掲示板Model"
    "Written by Tett"
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "board"




# class Users(models.Model):
#     name = models.CharField(max_length=255)
#     kana = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     tel = models.CharField(max_length=13, null=True)
#     password = models.CharField(max_length=255, null=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField(null=True)

#     class Meta:
#         db_table = "users"

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# class PhotoModel(models.Model):
#     image = models.ImageField(upload_to='images')

#     def __str__(self):
#         return self.image.url

# #Referencse English Document
# class Document(models.Model):
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     upload = models.FileField()
