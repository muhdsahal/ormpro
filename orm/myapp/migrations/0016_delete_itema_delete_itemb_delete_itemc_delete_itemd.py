# Generated by Django 4.2.1 on 2023-07-03 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_itema_itemb_itemc_itemd'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemA',
        ),
        migrations.DeleteModel(
            name='itemB',
        ),
        migrations.DeleteModel(
            name='itemC',
        ),
        migrations.DeleteModel(
            name='itemD',
        ),
    ]
