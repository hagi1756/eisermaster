# Generated by Django 5.0.1 on 2024-04-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
