# Generated by Django 3.2.8 on 2021-12-21 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_rename_post_id_attachment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='user',
        ),
    ]
