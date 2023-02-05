# Generated by Django 3.2.13 on 2023-02-01 19:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', editable=False, length=8, max_length=8, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('subtitle', models.CharField(default='subtitle', max_length=50)),
                ('images', models.JSONField(default=dict)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', editable=False, length=8, max_length=8, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField(default=0)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('images', models.JSONField(default=dict)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.greenieuser')),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]
