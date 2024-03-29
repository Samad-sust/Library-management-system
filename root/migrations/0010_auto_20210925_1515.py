# Generated by Django 3.2.7 on 2021-09-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0009_alter_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='sh_description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
