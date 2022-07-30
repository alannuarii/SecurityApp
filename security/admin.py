from django.contrib import admin
from security.models import Security, Pegawai, Tamu, Foto, Patroli, Apel, CCTV, Schedule

# Register your models here.
class SecurityAdmin(admin.ModelAdmin):
    list_display = ('id','nama_security')

class PegawaiAdmin(admin.ModelAdmin):
    list_display = ('id','nama_pegawai','jabatan','nohp')

class TamuAdmin(admin.ModelAdmin):
    list_display = ('id','tanggal','detail_time','nama','instansi','nohp','tujuan','kondisi','foto')

class FotoAdmin(admin.ModelAdmin):
    list_display = ('id','tanggal','detail_time','waktu','foto')

class PatroliAdmin(admin.ModelAdmin):
    list_display = ('id','tanggal','detail_time','nama_security_id','shift','waktu','lokasi','kondisi','foto')

class ApelAdmin(admin.ModelAdmin):
    list_display = ('id','tanggal','detail_time','nama_security_id','shift','atribut','foto')

class CCTVAdmin(admin.ModelAdmin):
    list_display = ('id','tanggal','detail_time','nama_security_id','shift','lokasi','kondisi')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id','periode','foto')



admin.site.register(Security, SecurityAdmin)
admin.site.register(Pegawai, PegawaiAdmin)
admin.site.register(Tamu, TamuAdmin)
admin.site.register(Foto, FotoAdmin)
admin.site.register(Patroli, PatroliAdmin)
admin.site.register(Apel, ApelAdmin)
admin.site.register(CCTV, CCTVAdmin)
admin.site.register(Schedule, ScheduleAdmin)

