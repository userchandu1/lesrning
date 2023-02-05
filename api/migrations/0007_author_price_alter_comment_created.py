# Generated by Django 4.1.5 on 2023-01-27 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_author_blog_alter_comment_created_entry"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="price",
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name="comment",
            name="created",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(2023, 1, 27, 3, 13, 44, 993098)
            ),
        ),
    ]