# Generated by Django 3.0.5 on 2020-04-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200426_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='images.png', upload_to='users/'),
        ),
    ]
