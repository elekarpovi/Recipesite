# Generated by Django 5.0.3 on 2024-03-31 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0002_rename_time_for_cooking_recipe_время_приготовления_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Фото',
            new_name='photo',
        ),
    ]
