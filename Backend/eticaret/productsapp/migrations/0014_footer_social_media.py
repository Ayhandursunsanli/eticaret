# Generated by Django 4.2 on 2023-07-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0013_footer_socialmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='social_media',
            field=models.ManyToManyField(blank=True, to='productsapp.socialmedia'),
        ),
    ]