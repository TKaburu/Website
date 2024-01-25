# Generated by Django 5.0.1 on 2024-01-18 11:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.CharField(default=django.utils.timezone.now, max_length=55),
            preserve_default=False,
        ),
    ]