# Generated by Django 5.2.1 on 2025-05-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crew', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crew',
            name='hourly_wage',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='crew',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='crew',
            name='is_tasked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='crew',
            name='role',
            field=models.CharField(choices=[('carpenter', 'Carpenter'), ('plumber', 'Plumber'), ('electrician', 'Electrician'), ('mason', 'Mason')], null=True),
        ),
    ]
