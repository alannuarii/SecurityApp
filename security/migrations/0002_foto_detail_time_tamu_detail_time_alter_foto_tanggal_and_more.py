# Generated by Django 4.0.6 on 2022-07-25 11:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='detail_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Timestamp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tamu',
            name='detail_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Timestamp'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foto',
            name='tanggal',
            field=models.DateField(auto_now=True, verbose_name='Tanggal'),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='tanggal',
            field=models.DateField(auto_now=True, verbose_name='Tanggal'),
        ),
    ]
