# Generated by Django 3.2.7 on 2021-12-05 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0009_image_posted_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='posted_on',
        ),
    ]