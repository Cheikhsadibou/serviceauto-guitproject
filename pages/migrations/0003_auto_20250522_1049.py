# Generated by Django 3.0.7 on 2025-05-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20250520_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='photo/%Y/%m/%d/'),
        ),
    ]
