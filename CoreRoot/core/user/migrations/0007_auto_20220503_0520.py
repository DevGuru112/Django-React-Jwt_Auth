# Generated by Django 3.1.6 on 2022-05-03 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0006_auto_20220503_0518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated',
        ),
    ]