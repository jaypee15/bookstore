# Generated by Django 4.2.5 on 2023-09-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
