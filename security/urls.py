from baton.autodiscover import admin
from django.urls import path, include
# from . import views
from security import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('', views.home, name='home'),
    path('form-penerimaan-tamu', views.form_tamu, name='form_tamu'),
    path('buku-tamu', views.buku_tamu, name='buku_tamu'),
    path('selamat-datang', views.selamat_datang, name='selamat_datang'),
    path('form-patroli', views.form_patroli, name='form_patroli'),
    path('laporan-patroli', views.laporan_patroli, name='laporan_patroli'),
    path('laporan-patroli-shift/<str:tanggal>/<int:waktu>', views.laporan_patroli_shift, name='laporan_patroli_shift'),
    path('form-apel', views.form_apel, name='form_apel'),
    path('laporan-apel', views.laporan_apel, name='laporan_apel'),
    path('form-cctv', views.form_cctv, name='form_cctv'),
    path('laporan-cctv', views.laporan_cctv, name='laporan_cctv'),
    path('form-jadwal', views.form_jadwal, name='form_jadwal'),
    path('jadwal-security', views.jadwal_security, name='jadwal_security'),
    path('emergency-call', views.emergency_call, name='emergency_call'),
    path('sop', views.sop, name='sop'),
    path('camera-action', views.camera_action, name='camera_action'),
    
    # path('login', views.loginView, name='login'),
    # path('logout', views.CustomLogoutView.as_view(), name='logout'),
]