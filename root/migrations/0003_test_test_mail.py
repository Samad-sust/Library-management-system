# Generated by Django 3.2.7 on 2021-09-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_test_test_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_mail',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]