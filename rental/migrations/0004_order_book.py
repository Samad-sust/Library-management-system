# Generated by Django 3.2.7 on 2021-10-09 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0012_auto_20211006_1020'),
        ('rental', '0003_auto_20211009_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='root.book'),
        ),
    ]
