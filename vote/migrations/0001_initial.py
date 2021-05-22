# Generated by Django 3.1.6 on 2021-05-22 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.candidateinfo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='user.dummycitizeninfo')),
            ],
        ),
    ]