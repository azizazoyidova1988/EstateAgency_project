# Generated by Django 3.2.4 on 2021-06-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210612_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='big_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
