# Generated by Django 4.1.6 on 2023-02-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]