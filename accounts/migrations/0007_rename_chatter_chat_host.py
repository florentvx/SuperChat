# Generated by Django 3.2.6 on 2021-08-31 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210830_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='Chatter',
            new_name='Host',
        ),
    ]
