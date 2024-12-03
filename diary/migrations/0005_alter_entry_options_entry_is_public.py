# Generated by Django 5.1.3 on 2024-11-28 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diary", "0004_alter_entry_text_alter_entry_title"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="entry",
            options={
                "ordering": ("created_at",),
                "verbose_name": "entry",
                "verbose_name_plural": "entries",
            },
        ),
        migrations.AddField(
            model_name="entry",
            name="is_public",
            field=models.BooleanField(default=False, verbose_name="Public"),
        ),
    ]
