# Generated by Django 4.0.5 on 2022-08-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(max_length=255),
        ),
    ]