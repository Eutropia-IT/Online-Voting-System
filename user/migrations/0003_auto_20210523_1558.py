# Generated by Django 3.1.7 on 2021-05-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_dummycitizeninfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummycitizeninfo',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pictures/'),
        ),
    ]