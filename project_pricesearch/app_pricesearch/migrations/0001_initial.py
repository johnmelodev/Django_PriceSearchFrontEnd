# Generated by Django 5.0.3 on 2024-03-19 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('site', models.TextField(max_length=255)),
                ('date_quotation', models.DateField()),
                ('image_link', models.TextField(default='https://via.placeholder.com/150', max_length=500)),
            ],
        ),
    ]
