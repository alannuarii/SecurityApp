# Generated by Django 4.0.6 on 2022-08-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0015_alter_apel_tanggal_alter_cctv_tanggal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patroli',
            name='foto',
            field=models.ImageField(upload_to='static/upload/security_patroli', verbose_name='Foto Security'),
        ),
    ]
