# Generated by Django 5.1.1 on 2024-10-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, upload_to="post_images/"),
        ),
    ]