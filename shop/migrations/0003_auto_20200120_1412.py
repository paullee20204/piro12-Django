# Generated by Django 2.2.9 on 2020-01-20 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item_is_publish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['id']},
        ),
    ]
