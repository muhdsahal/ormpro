# Generated by Django 4.2.1 on 2023-06-30 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_delete_std'),
    ]

    operations = [
        migrations.CreateModel(
            name='std',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('domain', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
            ],
        ),
    ]
