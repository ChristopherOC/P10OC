# Generated by Django 4.2.2 on 2023-06-28 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_project_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('FE', 'Front-end'), ('BE', 'Back-end'), ('Android', 'Android'), ('IOS', 'IOS')], max_length=7),
        ),
    ]
