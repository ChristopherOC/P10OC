# Generated by Django 4.2.2 on 2023-06-28 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_rename_descritpion_project_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='p_type',
            new_name='project_type',
        ),
    ]