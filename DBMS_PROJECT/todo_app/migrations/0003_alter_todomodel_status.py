# Generated by Django 4.0.5 on 2022-06-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todomodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
