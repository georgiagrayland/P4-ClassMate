# Generated by Django 3.2.19 on 2023-05-25 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_remove_school_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
    ]
