# Generated by Django 3.2.15 on 2022-08-20 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220820_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
