# Generated by Django 2.1.4 on 2020-05-24 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20200525_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test1',
            name='score',
            field=models.IntegerField(blank=True, default='1'),
            preserve_default=False,
        ),
    ]
