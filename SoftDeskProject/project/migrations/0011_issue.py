# Generated by Django 4.2.2 on 2023-07-09 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_alter_project_project_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('priority', models.CharField(max_length=30)),
                ('tag', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assigned_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_users', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_author', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='project.project')),
            ],
        ),
    ]
