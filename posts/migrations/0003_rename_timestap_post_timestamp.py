# Generated by Django 3.2.8 on 2021-10-15 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='timestap',
            new_name='timestamp',
        ),
    ]
