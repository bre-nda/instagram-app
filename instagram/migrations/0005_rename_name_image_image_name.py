# Generated by Django 3.2.7 on 2021-12-05 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20211205_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='image_name',
        ),
    ]