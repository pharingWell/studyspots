# Generated by Django 4.2.6 on 2023-11-09 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("studyspots", "0026_alter_studyspace_capacity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pendingstudyspace",
            name="capacity",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="studyspace",
            name="capacity",
            field=models.PositiveIntegerField(),
        ),
    ]
