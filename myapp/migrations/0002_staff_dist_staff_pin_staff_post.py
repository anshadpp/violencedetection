# Generated by Django 4.2.6 on 2024-02-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='dist',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='pin',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='post',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]