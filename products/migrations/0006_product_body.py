# Generated by Django 3.0.5 on 2020-04-21 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200421_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
