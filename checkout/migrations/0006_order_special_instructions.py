# Generated by Django 3.2 on 2021-06-06 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0005_order_user_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="special_instructions",
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
