# Generated by Django 3.0 on 2019-12-13 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='image',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]