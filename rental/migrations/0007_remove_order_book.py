# Generated by Django 3.2.7 on 2021-10-10 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0006_alter_order_transaction_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='book',
        ),
    ]
