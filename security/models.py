from django.db import models
from googletrans import Translator
from datetime import datetime


# Create your models here.

# Model Security 
class Security(models.Model):
    nama_security = models.CharField(verbose_name='Nama Security', max_length=30)

    def __str__(self):
        return '<{}>'.format(self.nama_security)


# Model Pegawai
class Pegawai(models.Model):
    nama_pegawai = models.CharField(verbose_name='Nama Pegawai', max_length=30)
    jabatan = models.CharField(verbose_name='Jabatan', max_length=50)
    nohp = models.CharField(verbose_name='No. Handphone', max_length=20)

    def __str__(self):
        return '<{}>'.format(self.nama_pegawai)


# Model Buku Tamu 
class Tamu(models.Model):
    tanggal = models.DateField(verbose_name='Tanggal')
    detail_time = models.DateTimeField(verbose_name='Timestamp')
    nama = models.CharField(verbose_name='Nama Lengkap', max_length=30)
    instansi = models.CharField(verbose_name='Instansi', max_length=50)
    nohp = models.CharField(verbose_name='No. HP', max_length=20)
    tujuan = models.CharField(verbose_name='Tujuan Berkunjung', max_length=150)
    kondisi = models.CharField(verbose_name='Kondisi Kesehatan', max_length=90)
    foto = models.ImageField(verbose_name='Foto Tamu', upload_to='static/upload/tamu')

    def fulldatetime(self): 
        def bulan(month):
            if month == 'Berbaris':
                month = 'Maret'
                return month
            elif month == 'Mungkin':
                month = 'Mei'
                return month
            else:
                return month
        
        str_tanggal = self.detail_time
        str_hari = str_tanggal.strftime('%A')
        str_bulan = str_tanggal.strftime('%B')
        trans_hari = Translator().translate(str_hari, src='en', dest='id')
        trans_bulan = Translator().translate(str_bulan, src='en', dest='id')
        result = str_tanggal.strftime('{}, %d {} %Y %H:%M WITA'.format(trans_hari.text, bulan(trans_bulan.text)))
        return result

    def real_date(self):
        self.tanggal = self.detail_time.date()

    def __str__(self):
        return '<{} - {}>'.format(self.nama, self.tanggal)


# Model Foto Patroli
class Foto(models.Model):
    tanggal = models.DateField(verbose_name='Tanggal')
    detail_time = models.DateTimeField(verbose_name='Timestamp')
    waktu = models.IntegerField(verbose_name='Waktu Patroli')
    foto = models.ImageField(verbose_name='Foto Patroli', upload_to='static/upload/patroli')

    def real_date(self):
        self.tanggal = self.detail_time.date()

    def __str__(self):
        return '<Shift {} : {}>'.format(self.waktu, self.tanggal)


# Model Patroli
class Patroli(models.Model):
    tanggal = models.DateField(verbose_name='Tanggal')
    detail_time = models.DateTimeField(verbose_name='Timestamp')
    shift = models.CharField(verbose_name='Shift', max_length=10)
    waktu = models.IntegerField(verbose_name='Waktu Patroli')
    lokasi = models.CharField(verbose_name='Lokasi', max_length=200)
    kondisi = models.CharField(verbose_name='Kondisi', max_length=200)
    foto = models.ImageField(verbose_name='Foto Security', upload_to='static/upload/security_patroli')
    nama_security_id = models.ForeignKey(Security, on_delete=models.CASCADE, verbose_name='Nama Security')

    def fulldatetime(self): 
        def bulan(month):
            if month == 'Berbaris':
                month = 'Maret'
                return month
            elif month == 'Mungkin':
                month = 'Mei'
                return month
            else:
                return month
        
        str_tanggal = self.detail_time
        str_hari = str_tanggal.strftime('%A')
        str_bulan = str_tanggal.strftime('%B')
        trans_hari = Translator().translate(str_hari, src='en', dest='id')
        trans_bulan = Translator().translate(str_bulan, src='en', dest='id')
        result = str_tanggal.strftime('{}, %d {} %Y %H:%M WITA'.format(trans_hari.text, bulan(trans_bulan.text)))
        return result

    def transmonth(self):
        month = self.detail_time
        str_month = month.strftime('%m')
        if str_month == '01':
            return 'Januari'
        elif str_month == '02':
            return 'Februari'
        elif str_month == '03':
            return 'Maret'
        elif str_month == '04':
            return 'April'
        elif str_month == '05':
            return 'Mei'
        elif str_month == '06':
            return 'Juni'
        elif str_month == '07':
            return 'Juli'
        elif str_month == '08':
            return 'Agustus'
        elif str_month == '09':
            return 'September'
        elif str_month == '10':
            return 'Oktober'
        elif str_month == '11':
            return 'November'
        elif str_month == '12':
            return 'Desember'

    def real_date(self):
        self.tanggal = self.detail_time.date()

    def __str__(self):
        return '<Shift {} : {}>'.format(self.shift, self.tanggal)


# Model Apel
class Apel(models.Model):
    tanggal = models.DateField(verbose_name='Tanggal')
    detail_time = models.DateTimeField(verbose_name='Timestamp')
    shift = models.CharField(verbose_name='Shift', max_length=10)
    atribut = models.CharField(verbose_name='Atribut', max_length=200)
    foto = models.ImageField(verbose_name='Foto Apel', upload_to='static/upload/apel')
    nama_security = models.CharField(verbose_name='Nama Secuirty', max_length=100)

    def fulldatetime(self): 
        def bulan(month):
            if month == 'Berbaris':
                month = 'Maret'
                return month
            elif month == 'Mungkin':
                month = 'Mei'
                return month
            else:
                return month
        
        str_tanggal = self.detail_time
        str_hari = str_tanggal.strftime('%A')
        str_bulan = str_tanggal.strftime('%B')
        trans_hari = Translator().translate(str_hari, src='en', dest='id')
        trans_bulan = Translator().translate(str_bulan, src='en', dest='id')
        result = str_tanggal.strftime('{}, %d {} %Y %H:%M WITA'.format(trans_hari.text, bulan(trans_bulan.text)))
        return result

    def real_date(self):
        self.tanggal = self.detail_time.date()

    def __str__(self):
        return '<Shift {} : {}>'.format(self.shift, self.tanggal)


# Model CCTV 
class CCTV(models.Model):
    tanggal = models.DateField(verbose_name='Tanggal')
    detail_time = models.DateTimeField(verbose_name='Timestamp')
    nama_security = models.CharField(verbose_name='Nama Secuirty', max_length=100)
    shift = models.CharField(verbose_name='Shift', max_length=10)
    kondisi = models.CharField(verbose_name='Kondisi', max_length=200)
    lokasi = models.CharField(verbose_name='Lokasi', max_length=100)
    
    def fulldatetime(self): 
        def bulan(month):
            if month == 'Berbaris':
                month = 'Maret'
                return month
            elif month == 'Mungkin':
                month = 'Mei'
                return month
            else:
                return month
        
        str_tanggal = self.detail_time
        str_hari = str_tanggal.strftime('%A')
        str_bulan = str_tanggal.strftime('%B')
        trans_hari = Translator().translate(str_hari, src='en', dest='id')
        trans_bulan = Translator().translate(str_bulan, src='en', dest='id')
        result = str_tanggal.strftime('{}, %d {} %Y %H:%M WITA'.format(trans_hari.text, bulan(trans_bulan.text)))
        return result

    def real_date(self):
        self.tanggal = self.detail_time.date()

    def __str__(self):
        return '<Shift {} : {}>'.format(self.shift, self.tanggal)


# Model Jadwal Secuirty 
class Schedule(models.Model):
    foto = models.ImageField(verbose_name='Jadwal Security', upload_to='static/upload/jadwal')
    periode = models.DateField(verbose_name='Periode')

    def __str__(self):
        return '<{}>'.format(self.periode)