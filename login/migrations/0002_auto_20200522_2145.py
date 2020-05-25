# Generated by Django 2.1.4 on 2020-05-22 16:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='Class',
            field=models.CharField(default="3", max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='Email',
            field=models.EmailField(default='example@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='Gender',
            field=models.CharField(default='M/F', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='Percentage',
            field=models.IntegerField(default='00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='Phone',
            field=models.IntegerField(default='1234567890'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='Section',
            field=models.CharField(default='-', max_length=1),
            preserve_default=False,
        ),
    ]
