# Generated by Django 2.2.5 on 2019-09-27 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0003_favorite_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorite',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]