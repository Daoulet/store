# Generated by Django 3.0.5 on 2020-04-20 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
