# Generated by Django 4.0.6 on 2022-08-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0011_alter_schedule_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='foto',
            field=models.ImageField(upload_to='upload/patroli', verbose_name='Foto Patroli'),
        ),
        migrations.AlterField(
            model_name='patroli',
            name='foto',
            field=models.ImageField(upload_to='upload/security patroli', verbose_name='Foto Security'),
        ),
    ]
