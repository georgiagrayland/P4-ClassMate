# Generated by Django 3.2.19 on 2023-05-16 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20230516_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='avg_english_grade',
            new_name='avg_gcse_english_grade',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='avg_maths_grade',
            new_name='avg_gcse_maths_grade',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='percentage_gcse_5',
            new_name='percentage_gcse_5_above',
        ),
    ]
