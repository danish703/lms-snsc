# Generated by Django 3.2.7 on 2021-10-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='classroom/'),
        ),
    ]
