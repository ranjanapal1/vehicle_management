# Generated by Django 4.1.6 on 2023-02-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0002_users_options_vehicle"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="options",
            field=models.CharField(
                choices=[("SA", "Super admin"), ("A", "Admin"), ("U", "user")],
                default="U",
                max_length=2,
            ),
        ),
    ]
