# Generated by Django 4.0.6 on 2022-08-02 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0008_remove_cctv_nama_security_id_cctv_nama_security'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='foto',
            field=models.ImageField(upload_to='media/static/upload/jadwal', verbose_name='Jadwal Security'),
        ),
    ]