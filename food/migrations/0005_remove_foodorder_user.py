# Generated by Django 3.2.3 on 2021-06-03 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_foodorder_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodorder',
            name='user',
        ),
    ]
