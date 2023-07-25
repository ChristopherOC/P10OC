# Generated by Django 4.2.2 on 2023-06-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_rename_p_type_project_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('FE', 'Front-end'), ('BE', 'Back-end'), ('Android', 'Android'), ('IOS', 'IOS')], db_column='type', max_length=7),
        ),
    ]