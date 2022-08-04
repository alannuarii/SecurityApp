from django.shortcuts import render, redirect
from security.models import Security, Pegawai, Tamu, Foto, Patroli, Apel, CCTV, Schedule
from security.utils import *
from datetime import datetime, timedelta
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# import pywhatkit as pw



# HALAMAN SIGN-IN 
def sign_in(request):
    
    context={
        'title':'Sign In',
        }

    user = None
    
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'pages/sign-in.html', context)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username atau password Anda tidak tepat')
            return redirect('/sign-in')
    

# Fungsi Sign Out 
def sign_out(request):
    logout(request)
    return redirect('/sign-in')


# HALAMAN HOME 
@login_required(login_url='sign_in')
def home(request):
    _today = datetime.now() - timedelta(hours=-8)
    jam = _today.strftime('%H')
    tanggal = _today.strftime('%Y-%m-%d')
    report_foto = Foto.objects.filter(waktu=patroli(int(jam))) & Foto.objects.filter(tanggal=tanggal)
    report_patroli = Patroli.objects.filter(waktu=patroli(int(jam))) & Patroli.objects.filter(tanggal=tanggal)
    report_apel = Apel.objects.filter(shift=shift(int(jam))) & Apel.objects.filter(tanggal=tanggal)

    context={
        'title':'Beranda',
        'photos': report_foto,
        'patrolis': report_patroli,
        'jadwal': jadwal_shift(),
        'apels': report_apel,
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
        input = Tamu(nama=nama, instansi=instansi, nohp=nohp, tujuan=tujuan, kondisi=kondisi, foto=base64tojpg1(foto,'Tamu',nama), detail_time=datetime.now() - timedelta(hours=-8))
        input.real_date()
        input.save()
        return redirect('/selamat-datang')
        
    context={
        'title':'Form Penerimaan Tamu',
        'jadwal': jadwal_shift(),
        'employees': employees
    }
    return render(request, 'pages/form-penerimaan-tamu.html', context)


# BUKU TAMU 
@login_required(login_url='sign_in')
def buku_tamu(request):
    tamus = Tamu.objects.order_by('-id')
    
    if 'bulan' in request.GET:
        query = request.GET.get('bulan')
        str_date = query+'-01'
        to_datetime = datetime.strptime(str_date, "%Y-%m-%d").date()
        last_datetime = to_datetime + timedelta(days=30)
        
        # guests = Tamu.objects.order_by('-id').filter(tanggal__range=(to_datetime, last_datetime))
        # Setup Pagination
        p = Paginator(Tamu.objects.order_by('-id').filter(tanggal__range=(to_datetime, last_datetime)), 2)
        page = request.GET.get('page')
        tamus = p.get_page(page)

    context={
        'title':'Buku Tamu',
        'jadwal': jadwal_shift(),
        'tamus': tamus,
        }
    return render(request, 'pages/buku-tamu.html', context)


# HALAMAN FORM PATROLI
@login_required(login_url='sign_in')
def form_patroli(request):
    names = Security.objects.all()

    if request.method == 'POST':
        detail_time = datetime.now() - timedelta(hours=-8)
        lokasi = request.POST['lokasi']
        kondisi = request.POST['kondisi']
        foto = request.POST['foto']
        nama_security_id = request.POST['nama_security_id']
        waktu_jaga = shift(int(detail_time.strftime('%H')))
        waktu = patroli(int(detail_time.strftime('%H')))

        input = Patroli(detail_time=detail_time, lokasi=lokasi, kondisi=kondisi, nama_security_id_id=nama_security_id, shift=waktu_jaga, foto=base64tojpg1(fotobase64=foto,depan='Patroli',tengah=names[int(nama_security_id)-1].nama_security), waktu=waktu)
        input.real_date()
        input.save()
        # pw.sendwhatmsg_to_group_instantly("BoqTd9gtvEt9ioXc5RqWee", "LAPORAN PATROLI \n{} \nLokasi: {} \nSecurity Patroli: {} \nKondisi: {} \nDetail Laporan: \nhttp://127.0.0.1:8000/laporan-patroli-shift/{}/{}".format(detail_time.strftime('Tanggal %d-%m-%Y Pukul %H:%M WITA'), lokasi, names[int(nama_security_id) - 1].nama_security, kondisi, detail_time.strftime('%Y-%m-%d'), str(waktu)))
        return redirect('/')

    context={
        'title':'Form Patroli',
        'jadwal': jadwal_shift(),
        'names': names
    }
    return render(request, 'pages/form-patroli.html', context)


# LAPORAN PATROLI 
@login_required(login_url='sign_in')
def laporan_patroli(request):
    _today = datetime.now() - timedelta(hours=-8)
    today = _today.strftime('%Y-%m-%d')
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
        'jadwal': jadwal_shift(),
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

    context={
        'title':'Laporan Patroli',
        'patroli': report_patroli,
        'photos': report_foto, 
        }
    return render(request, 'pages/laporan-patroli-shift.html', context)


# HALAMAN FORM APEL
@login_required(login_url='sign_in')
def form_apel(request):
    names = Security.objects.all()

    if request.method == 'POST':
        nama_security = request.POST.getlist('nama_security_id')
        for i in range(len(nama_security)):
            detail_time = datetime.now() - timedelta(hours=-8)
            atribut = request.POST['atribut']
            foto = request.POST['foto']
            nama_security_id = nama_security[i]
            waktu_jaga = shift(int(detail_time.strftime('%H')))

            input = Apel(detail_time=detail_time, atribut=atribut, nama_security_id_id=nama_security_id, shift=waktu_jaga, foto=base64tojpg1(fotobase64=foto,depan='Apel',tengah=names[int(nama_security_id)-1].nama_security))
            input.real_date()
            input.save()
        return redirect('/')

    context={
        'title':'Form Apel',
        'jadwal': jadwal_shift(),
        'names': names
    }
    return render(request, 'pages/form-apel.html', context)


# LAPORAN APEL
@login_required(login_url='sign_in')
def laporan_apel(request):
    _today = datetime.now() - timedelta(hours=-8)
    today = _today.strftime('%Y-%m-%d')
    query = request.GET.get('tanggal') 
    
    if query:
        query_trans = tanggal(query)
    else:
        query_trans = ''

    shift_malam = Apel.objects.filter(tanggal=today) & Apel.objects.filter(shift='Malam')
    shift_pagi = Apel.objects.filter(tanggal=today) & Apel.objects.filter(shift='Pagi')
    shift_sore = Apel.objects.filter(tanggal=today) & Apel.objects.filter(shift='Sore')
    
    if 'tanggal' in request.GET:
        query_tgl = request.GET.get('tanggal')
        shift_malam = Apel.objects.filter(tanggal=query_tgl) & Apel.objects.filter(shift='Malam')
        shift_pagi = Apel.objects.filter(tanggal=query_tgl) & Apel.objects.filter(shift='Pagi')
        shift_sore = Apel.objects.filter(tanggal=query_tgl) & Apel.objects.filter(shift='Sore')
        
    context={
        'title':'Laporan Apel',
        'jadwal': jadwal_shift(),
        'today': today,
        'query': query or None,
        'date_today': tanggal(today),
        'date_query': query_trans,
        'shift_malam': shift_malam,
        'shift_pagi': shift_pagi,
        'shift_sore': shift_sore,
        }
    return render(request, 'pages/laporan-apel.html', context)


# LAPORAN APEL SHIFT
def laporan_apel_shift(request, tanggal, shift):
    report_apel = Apel.objects.filter(tanggal=tanggal) & Apel.objects.filter(shift=shift)

    context={
        'title':'Laporan Apel',
        'apel': report_apel,
        }
    return render(request, 'pages/laporan-apel-shift.html', context)


# HALAMAN FORM CCTV
@login_required(login_url='sign_in')
def form_cctv(request):
    names = Security.objects.all()

    if request.method == 'POST':
        detail_time = datetime.now() - timedelta(hours=-8)
        nama_security = request.POST.getlist('nama_security_id')
        kondisi = request.POST['kondisi']
        lokasi = request.POST['lokasi']
        waktu_jaga = shift(int(detail_time.strftime('%H')))

        input = CCTV(detail_time=detail_time, kondisi=kondisi, lokasi=lokasi, nama_security=str(nama_security), shift=waktu_jaga)
        input.real_date()
        input.save()
        return redirect('/')

    context={
        'title':'Form CCTV',
        'jadwal': jadwal_shift(),
        'names': names
    }
    return render(request, 'pages/form-cctv.html', context)


# LAPORAN CCTV
@login_required(login_url='sign_in')
def laporan_cctv(request):
    _today = datetime.now() - timedelta(hours=-8)
    today = _today.strftime('%Y-%m-%d')
    query = request.GET.get('tanggal') 
    
    if query:
        query_trans = tanggal(query)
    else:
        query_trans = ''

    shift_malam = CCTV.objects.filter(tanggal=today) & CCTV.objects.filter(shift='Malam')
    shift_pagi = CCTV.objects.filter(tanggal=today) & CCTV.objects.filter(shift='Pagi')
    shift_sore = CCTV.objects.filter(tanggal=today) & CCTV.objects.filter(shift='Sore')
    
    if 'tanggal' in request.GET:
        query_tgl = request.GET.get('tanggal')
        shift_malam = CCTV.objects.filter(tanggal=query_tgl) & CCTV.objects.filter(shift='Malam')
        shift_pagi = CCTV.objects.filter(tanggal=query_tgl) & CCTV.objects.filter(shift='Pagi')
        shift_sore = CCTV.objects.filter(tanggal=query_tgl) & CCTV.objects.filter(shift='Sore')
        
    context={
        'title':'Laporan CCTV',
        'jadwal': jadwal_shift(),
        'today': today,
        'query': query or None,
        'date_today': tanggal(today),
        'date_query': query_trans,
        'shift_malam': shift_malam,
        'shift_pagi': shift_pagi,
        'shift_sore': shift_sore,
        }
    return render(request, 'pages/laporan-cctv.html', context)


# HALAMAN INPUT JADWAL SECURITY
@login_required(login_url='sign_in')
def form_jadwal(request):
    
    if request.method == 'POST':
        foto = request.FILES['foto']
        periode = request.POST['periode']+'-01'
        input = Schedule(foto=foto, periode=periode)
        input.save()
        return redirect('/')

    context={'title':'Form Jadwal Security'}
    return render(request, 'pages/form-jadwal.html', context)


# HALAMAN JADWAL SECURITY
@login_required(login_url='sign_in')
def jadwal_security(request):
    jadwal_security = Schedule.objects.last()

    context={
        'title':'Jadwal Security',
        'jadwal': jadwal_shift(),
        'jadwal_security': jadwal_security,
        }
    return render(request, 'pages/jadwal-security.html', context)


# HALAMAN EMERGENCY CALL
@login_required(login_url='sign_in')
def emergency_call(request):
    context={
        'title':'Emergency Call', 
        'jadwal': jadwal_shift(),
    }
    return render(request, 'pages/emergency-call.html', context)


# HALAMAN SOP
@login_required(login_url='sign_in')
def sop(request):
    context={
        'title':'S O P',
        'jadwal': jadwal_shift(),
        }
    return render(request, 'pages/sop.html', context)


# CAMERA ACTION
@login_required(login_url='sign_in')
def camera_action(request):
    if request.method == 'POST':
        foto = request.POST['foto']
        detail_time = datetime.now() - timedelta(hours=-8)
        waktu = patroli(int(detail_time.strftime('%H')))
        input = Foto(foto=base64tojpg2(fotobase64=foto), detail_time=detail_time, waktu=waktu)
        input.real_date()
        input.save()

    context={
        'title':'Camera Action',
        'jadwal': jadwal_shift(),
        }
    return render(request, 'pages/camera-action.html', context)


# SELAMAT DATANG
def selamat_datang(request):
    tamu = Tamu.objects.last()
    context={
        'title':'Selamat Datang',
        'tamu': tamu,
        }
    return render(request, 'pages/selamat-datang.html', context)