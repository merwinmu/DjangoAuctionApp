# Generated by Django 3.2.9 on 2021-12-01 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20211201_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='name',
        ),
    ]