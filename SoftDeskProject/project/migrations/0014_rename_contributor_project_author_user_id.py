# Generated by Django 4.2.2 on 2023-07-17 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_alter_mycustomuser_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='contributor',
            new_name='author_user_id',
        ),
    ]
