# Generated by Django 2.2.13 on 2021-04-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_board_user_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='image',
            field=models.ImageField(default=0, upload_to='images', verbose_name='投稿画像'),
            preserve_default=False,
        ),
    ]
