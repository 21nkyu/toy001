# Generated by Django 3.2.8 on 2021-10-27 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='datetime',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='datetime',
            new_name='create_date',
        ),
    ]