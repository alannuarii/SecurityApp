# Generated by Django 4.0.6 on 2022-08-08 07:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0017_alter_patroli_kondisi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apel',
            name='nama_security_id',
        ),
        migrations.AddField(
            model_name='apel',
            name='nama_security',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Nama Secuirty'),
            preserve_default=False,
        ),
    ]
