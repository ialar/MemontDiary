# Generated by Django 5.1.3 on 2024-11-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diary", "0003_alter_entry_created_at_alter_entry_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="text",
            field=models.TextField(verbose_name="Text"),
        ),
        migrations.AlterField(
            model_name="entry",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Title"),
        ),
    ]
