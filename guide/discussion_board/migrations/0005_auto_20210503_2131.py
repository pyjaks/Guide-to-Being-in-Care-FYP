# Generated by Django 3.1.7 on 2021-05-03 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussion_board', '0004_auto_20210503_0024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date',
            new_name='datePosted',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='date',
            new_name='datePosted',
        ),
    ]