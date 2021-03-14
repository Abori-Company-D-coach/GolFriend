# Generated by Django 2.2.13 on 2021-03-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('snsimage', models.ImageField(upload_to='')),
                ('good', models.IntegerField(blank=True, default=1, null=True)),
                ('read', models.IntegerField(blank=True, default=1, null=True)),
                ('readtext', models.TextField(blank=True, default='a', null=True)),
            ],
        ),
    ]
