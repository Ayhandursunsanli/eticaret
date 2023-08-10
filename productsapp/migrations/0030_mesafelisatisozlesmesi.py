# Generated by Django 4.2.3 on 2023-08-03 10:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0029_kvkkmetni_uyelikmetni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesafelisatisozlesmesi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesafeliBaslik', models.CharField(max_length=150, null=True)),
                ('mesafelimetni', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='KVKK Metni')),
            ],
            options={
                'verbose_name_plural': 'Mesafeli Satış Sözleşmesi',
            },
        ),
    ]