# Generated by Django 2.1.4 on 2020-05-29 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_remove_signup_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeReq', models.DurationField(blank=True, db_index=True, null=True)),
                ('UserName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.SignUp')),
            ],
        ),
    ]
