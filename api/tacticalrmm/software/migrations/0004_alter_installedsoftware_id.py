# Generated by Django 4.2.10 on 2024-02-19 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("software", "0003_delete_chocolog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="installedsoftware",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]