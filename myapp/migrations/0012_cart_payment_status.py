# Generated by Django 4.1 on 2022-09-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='payment_status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
