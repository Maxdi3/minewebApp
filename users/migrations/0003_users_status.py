# Generated by Django 5.0 on 2024-01-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
