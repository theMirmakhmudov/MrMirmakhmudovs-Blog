# Generated by Django 5.0.6 on 2024-06-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestblogpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='latestblogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='owners',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='person'),
        ),
    ]
