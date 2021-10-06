# Generated by Django 3.2.6 on 2021-08-30 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_chats_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='Category',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='Category',
            field=models.CharField(choices=[('Common', 'Common'), ('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold')], max_length=200, null=True),
        ),
    ]