# Generated by Django 3.1.6 on 2021-02-18 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_delete_profileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.CharField(default='room', max_length=100),
            preserve_default=False,
        ),
    ]
