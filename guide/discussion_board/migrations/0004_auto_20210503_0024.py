# Generated by Django 3.1.7 on 2021-05-03 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussion_board', '0003_comment_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_on',
            new_name='original_post',
        ),
    ]
