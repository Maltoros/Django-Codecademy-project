# Generated by Django 4.1.7 on 2023-04-03 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_ingredient_quantity_alter_ingredient_unit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='price',
            new_name='price_per_unit',
        ),
    ]
