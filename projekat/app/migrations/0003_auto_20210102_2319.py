# Generated by Django 3.1.4 on 2021-01-02 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210102_2310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='content',
            new_name='review',
        ),
    ]