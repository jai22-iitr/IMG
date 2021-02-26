# Generated by Django 3.1.6 on 2021-02-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_message_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='myimage')),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='photo',
        ),
    ]
