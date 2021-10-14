# Generated by Django 3.2.7 on 2021-09-25 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_test_test_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('date_of_birth', models.DateField()),
                ('biography', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Natinality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AddField(
            model_name='author',
            name='natinality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='root.natinality'),
        ),
    ]
