# Generated by Django 3.2.6 on 2021-08-30 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210830_2313'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chats',
            new_name='Chat',
        ),
    ]