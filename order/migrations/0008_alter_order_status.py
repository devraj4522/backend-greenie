# Generated by Django 4.0.8 on 2023-02-12 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20230205_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('VIEWED', 'VIEWED'), ('ADDED_TO_CART', 'ADDED_TO_CART'), ('PAYMENT_PENDING', 'PAYMENT_PENDING'), ('PAYMENT_DONE', 'PAYMENT_DONE'), ('RETURNED', 'RETURNED'), ('REFUNDED', 'REFUNDED'), ('REFUNDED_DESPUTED', 'REFUNDED_DESPUTED')], default='ADDED_TO_CART', max_length=30),
        ),
    ]
