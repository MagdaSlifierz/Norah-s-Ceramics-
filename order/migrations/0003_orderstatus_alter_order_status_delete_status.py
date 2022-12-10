# Generated by Django 4.0.4 on 2022-06-26 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_total_bill_pence_order_bill_pence_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.orderstatus'),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]