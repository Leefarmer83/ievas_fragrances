# Generated by Django 3.2 on 2021-05-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0003_rename_subscriber_join"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscriber",
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
                ("email", models.EmailField(max_length=255)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Join",
        ),
    ]
