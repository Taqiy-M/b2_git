# Generated by Django 4.1.1 on 2022-09-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talaba',
            name='yosh',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
