# Generated by Django 5.0.4 on 2024-05-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_postnews_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="VideoContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("url_video", models.URLField()),
            ],
        ),
    ]