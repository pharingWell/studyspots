# Generated by Django 4.2.5 on 2023-10-24 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("studyspots", "0005_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studyspace",
            old_name="crookedness_ratings",
            new_name="crowdedness_ratings",
        ),
    ]
