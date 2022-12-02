# Generated by Django 4.1.3 on 2022-12-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0001_initial"),
        ("traits", "0004_trait_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trait",
            name="pets",
            field=models.ManyToManyField(related_name="traits", to="pets.pet"),
        ),
    ]