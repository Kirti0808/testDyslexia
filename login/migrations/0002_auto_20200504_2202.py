# Generated by Django 2.1.4 on 2020-05-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=264)),
                ('Age', models.IntegerField()),
                ('Password', models.CharField(max_length=264)),
            ],
        ),
        migrations.DeleteModel(
            name='LoginForm',
        ),
    ]
