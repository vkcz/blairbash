# Generated by Django 2.1 on 2018-08-26 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qdb', '0002_auto_20180817_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='ip',
            field=models.GenericIPAddressField(default='0.0.0.0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='useragent',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
