# Generated by Django 4.0.6 on 2022-07-25 12:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0002_foto_detail_time_tamu_detail_time_alter_foto_tanggal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patroli',
            name='detail_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Timestamp'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patroli',
            name='tanggal',
            field=models.DateField(auto_now=True, verbose_name='Tanggal'),
        ),
    ]
