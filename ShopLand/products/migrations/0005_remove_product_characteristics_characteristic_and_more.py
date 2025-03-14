# Generated by Django 5.1.6 on 2025-03-09 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_carecteristic_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='characteristics',
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characteristics', to='products.category')),
            ],
            options={
                'verbose_name': 'carecteristic',
                'verbose_name_plural': 'carecteristics',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_characteristics', to='products.characteristic')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_characteristics', to='products.product')),
            ],
        ),
        migrations.DeleteModel(
            name='Carecteristic',
        ),
        migrations.AddIndex(
            model_name='characteristic',
            index=models.Index(fields=['name'], name='products_ch_name_33bcf3_idx'),
        ),
        migrations.AddIndex(
            model_name='characteristic',
            index=models.Index(fields=['category'], name='products_ch_categor_88c4b3_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='productcharacteristic',
            unique_together={('product', 'characteristic')},
        ),
    ]
