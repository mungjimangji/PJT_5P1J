# Generated by Django 3.2.18 on 2023-05-15 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_big_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='big_tags',
        ),
    ]