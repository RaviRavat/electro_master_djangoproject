# Generated by Django 4.1 on 2022-09-07 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('checksum', models.CharField(blank=True, max_length=100, null=True)),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='myapp.user')),
            ],
        ),
    ]
