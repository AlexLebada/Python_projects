# Generated by Django 4.2.16 on 2024-12-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='placeholder.png', upload_to='img'),
        ),
    ]
