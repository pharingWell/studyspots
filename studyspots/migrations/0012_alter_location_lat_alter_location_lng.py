# Generated by Django 4.2.6 on 2023-10-31 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyspots', '0001_squashed_0011_rename_studyspot_studyspace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=7, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(decimal_places=7, default=0.0, max_digits=10),
        ),
    ]