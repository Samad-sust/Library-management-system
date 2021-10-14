# Generated by Django 3.2.7 on 2021-09-25 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0006_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library_book_no', models.IntegerField()),
                ('name', models.CharField(max_length=60)),
                ('stock_availability', models.BooleanField(default=True)),
                ('photo', models.CharField(max_length=60)),
                ('edition', models.CharField(max_length=60)),
                ('pages', models.IntegerField()),
                ('publication_date', models.DateField()),
                ('price', models.IntegerField()),
                ('isbn', models.CharField(max_length=60)),
                ('sh_description', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='root.author')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='root.genre')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='root.language')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='root.publisher')),
            ],
        ),
        migrations.RemoveField(
            model_name='books',
            name='book_details_id',
        ),
        migrations.DeleteModel(
            name='Book_details',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]