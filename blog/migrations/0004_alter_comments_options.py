# Generated by Django 5.0.1 on 2024-01-25 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-created_on']},
        ),
    ]
