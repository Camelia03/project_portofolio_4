# Generated by Django 3.2.20 on 2023-08-15 14:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0011_rename_post_thread'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Reply',
        ),
    ]
