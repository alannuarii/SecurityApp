from django.shortcuts import render, redirect
from security.models import Security, Pegawai, Tamu, Foto, Patroli
from security.utils import *
from datetime import datetime
from django.conf import settings
import pywhatkit as pw


# Create your views here.

# HALAMAN HOME 
def home(request):
    jam = datetime.now().strftime('%H')
    tanggal = datetime.now().strftime('%Y-%m-%d')
    report_foto = Foto.objects.filter(waktu=patroli(int(jam))) & Foto.objects.filter(tanggal=tanggal)
    report_patroli = Patroli.objects.filter(waktu=patroli(int(jam))) & Patroli.objects.filter(tanggal=tanggal)

    context={
        'title':'Beranda',
        'photos': report_foto,
        'patrolis': report_patroli,
        }
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
        pw.sendwhatmsg_to_group_instantly("BoqTd9gtvEt9ioXc5RqWee", "LAPORAN PATROLI \n{} \nLokasi: {} \nSecurity Patroli: {} \nKondisi: {} \nDetail Laporan: \nhttp://127.0.0.1:8000/laporan-patroli-shift/{}/{}".format(detail_time.strftime('Tanggal %d-%m-%Y Pukul %H:%M WITA'), lokasi, names[int(nama_security_id) - 1].nama_security, kondisi, detail_time.strftime('%Y-%m-%d'), str(waktu)))
        return redirect('/')

    context={
        'title':'Form Patroli',
        'names': names
    }
    return render(request, 'pages/form-patroli.html', context)


# LAPORAN PATROLI 
def laporan_patroli(request):
    today = datetime.now().strftime('%Y-%m-%d')
    query = request.GET.get('tanggal') 
    
    if query:
        query_trans = tanggal(query)
    else:
        query_trans = ''

    ptrl_11 = Patroli.objects.filter(tanggal=today) & Patroli.objects.filter(waktu=11)
    ptrl_12 = Patroli.objects.filter(tanggal=today) & Patroli.objects.filter(waktu=12)
    ptrl_13 = Patroli.objects.filter(tanggal=today) & Patroli.objects.filter(waktu=13)
    ptrl_21 = Patroli.objects.filter(tanggal=today) & Patroli.objects.filter(waktu=21)
    ptrl_22 = Patroli.objects.filter(tanggal=today) & Patroli.objects.filter(waktu=22)
    ptrl_23 = Patroli.objects.filter(tanggal=today) & Patroli.objects.filter(waktu=23)
    ptrl_31 = Patroli.objects.filter(tanggal=today) & Patroli.objects.filter(waktu=31)
    ptrl_32 = Patroli.objects.filter(tanggal=today) & Patroli.objects.filter(waktu=32)
    ptrl_33 = Patroli.objects.filter(tanggal=today) & Patroli.objects.filter(waktu=33)

    if 'tanggal' in request.GET:
        query_tgl = request.GET.get('tanggal')
        ptrl_11 = Patroli.objects.filter(tanggal=query_tgl) & Patroli.objects.filter(waktu=11)
        ptrl_12 = Patroli.objects.filter(tanggal=query_tgl) & Patroli.objects.filter(waktu=12)
        ptrl_13 = Patroli.objects.filter(tanggal=query_tgl) & Patroli.objects.filter(waktu=13)
        ptrl_21 = Patroli.objects.filter(tanggal=query_tgl) & Patroli.objects.filter(waktu=21)
        ptrl_22 = Patroli.objects.filter(tanggal=query_tgl) & Patroli.objects.filter(waktu=22)
        ptrl_23 = Patroli.objects.filter(tanggal=query_tgl) & Patroli.objects.filter(waktu=23)
        ptrl_31 = Patroli.objects.filter(tanggal=query_tgl) & Patroli.objects.filter(waktu=31)
        ptrl_32 = Patroli.objects.filter(tanggal=query_tgl) & Patroli.objects.filter(waktu=32)
        ptrl_33 = Patroli.objects.filter(tanggal=query_tgl) & Patroli.objects.filter(waktu=33)

    
    context={
        'title':'Laporan Patroli',
        'today': today,
        'query': query or None,
        'date_today': tanggal(today),
        'date_query': query_trans,
        'ptrl_11': ptrl_11,
        'ptrl_12': ptrl_12,
        'ptrl_13': ptrl_13,
        'ptrl_21': ptrl_21,
        'ptrl_22': ptrl_22,
        'ptrl_23': ptrl_23,
        'ptrl_31': ptrl_31,
        'ptrl_32': ptrl_32,
        'ptrl_33': ptrl_33,
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