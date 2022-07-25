from django.shortcuts import render, redirect
from security.models import Security, Pegawai, Tamu, Foto, Patroli
from security.control import *
from datetime import datetime
from django.conf import settings
import pywhatkit as pw


# Create your views here.

# HALAMAN HOME 
def home(request):

    context={'title':'Beranda'}
    return render(request, 'pages/home.html', context)


# HALAMAN FORM PENERIMAAN TAMU
def form_tamu(request):
    employees = Pegawai.objects.all()

    # Insert Data 
    if request.method == 'POST':
        nama = request.POST['nama']
        instansi = request.POST['instansi']
        nohp = request.POST['nohp']
        tujuan = request.POST['tujuan']
        pegawai = request.POST['pegawai']
        kondisi = request.POST['kondisi']
        foto = request.POST['foto']
        input = Tamu(nama=nama, instansi=instansi, nohp=nohp, tujuan=tujuan, kondisi=kondisi, foto=base64tojpg1(foto,'Tamu',nama), detail_time=datetime.now())
        input.save()
        return redirect('/selamat-datang')
        
    context={
        'title':'Form Penerimaan Tamu',
        'employees': employees
    }
    return render(request, 'pages/form-penerimaan-tamu.html', context)


# HALAMAN FORM PATROLI
def form_patroli(request):
    names = Security.objects.all()

    if request.method == 'POST':
        detail_time = datetime.now()
        lokasi = request.POST['lokasi']
        kondisi = request.POST['kondisi']
        foto = request.POST['foto']
        nama_security_id = request.POST['nama_security_id']
        waktu_jaga = shift(int(detail_time.strftime('%H')))
        waktu = patroli(int(detail_time.strftime('%H')))

        input = Patroli(detail_time=detail_time, lokasi=lokasi, kondisi=kondisi, nama_security_id_id=nama_security_id, shift=waktu_jaga, foto=base64tojpg1(fotobase64=foto,depan='Patroli',tengah=names[int(nama_security_id)-1].nama_security), waktu=waktu)
        input.save()
        return redirect('/')

    context={
        'title':'Form Patroli',
        'names': names
    }
    return render(request, 'pages/form-patroli.html', context)


# LAPORAN PATROLI 
def laporan_patroli(request):
    today = datetime.now().strftime('%Y-%m-%d')

    context={
        'title':'Laporan Patroli',
        'today': today,
        }
    return render(request, 'pages/laporan-patroli.html', context)


# LAPORAN PATROLI SHIFT
def laporan_patroli_shift(request, tanggal, waktu):
    report_patroli = Patroli.objects.filter(tanggal=tanggal) & Patroli.objects.filter(waktu=waktu)
    report_foto = Foto.objects.filter(tanggal=tanggal) & Foto.objects.filter(waktu=waktu)

    print(report_patroli)
    context={
        'title':'Laporan Patroli',
        'patroli': report_patroli,
        'photos': report_foto, 
        }
    return render(request, 'pages/laporan-patroli-shift.html', context)


# HALAMAN FORM APEL
def form_apel(request):
    names = Security.objects.all()

    context={
        'title':'Form Apel',
        'names': names
    }
    return render(request, 'pages/form-apel.html', context)


# HALAMAN FORM CCTV
def form_cctv(request):
    names = Security.objects.all()

    context={
        'title':'Form Apel',
        'names': names
    }
    return render(request, 'pages/form-cctv.html', context)


# HALAMAN EMERGENCY CALL
def emergency_call(request):
    context={'title':'Emergency Call'}
    return render(request, 'pages/emergency-call.html', context)


# HALAMAN SOP
def sop(request):
    context={'title':'S O P'}
    return render(request, 'pages/sop.html', context)


# CAMERA ACTION
def camera_action(request):
    if request.method == 'POST':
        foto = request.POST['foto']
        detail_time = datetime.now()
        waktu = patroli(int(detail_time.strftime('%H')))
        input = Foto(foto=base64tojpg2(fotobase64=foto), detail_time=detail_time, waktu=waktu)
        input.save()

    context={'title':'Camera Action'}
    return render(request, 'pages/camera-action.html', context)


# SELAMAT DATANG
def selamat_datang(request):
    tamu = Tamu.objects.last()
    context={
        'title':'Selamat Datang',
        'tamu': tamu,
        }
    return render(request, 'pages/selamat-datang.html', context)