# Generated by Django 3.2.6 on 2021-08-30 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210830_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Description', models.CharField(max_length=200, null=True)),
                ('DateCreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('Donations', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Content', models.CharField(max_length=200, null=True)),
                ('DateCreated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='chatter',
            name='DateCreated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]