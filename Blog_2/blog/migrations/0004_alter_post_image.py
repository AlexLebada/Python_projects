# Generated by Django 4.2.16 on 2024-12-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='placeholder.png', upload_to='img'),
        ),
    ]