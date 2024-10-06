# Generated by Django 3.2.13 on 2023-02-04 18:11

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', editable=False, length=8, max_length=8, prefix='', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='txn',
            name='id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', editable=False, length=8, max_length=8, prefix='', primary_key=True, serialize=False),
        ),
    ]