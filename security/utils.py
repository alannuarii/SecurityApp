from datetime import datetime
from django.core.files.base import ContentFile
from googletrans import Translator
import base64

def base64tojpg1(fotobase64, depan:str, tengah):
    new_foto = fotobase64.replace('data:image/jpeg;base64,','')
    image_data = base64.b64decode(new_foto)
    microsecond = datetime.now().strftime('%f')
    filename = depan+'-'+tengah+'-'+microsecond+'.jpg'
    filefoto = ContentFile(image_data, filename)
    return filefoto

def base64tojpg2(fotobase64):
    new_foto = fotobase64.replace('data:image/png;base64,','')
    image_data = base64.b64decode(new_foto)
    nama = datetime.now().strftime('%d%m%Y%H%M%S%f')
    filename = nama+'.jpg'
    filefoto = ContentFile(image_data, filename)
    return filefoto

def shift(jam):
    pagi = list(range(8,16))
    sore = list(range(16,24))
    malam = list(range(0,8))

    if jam in pagi:
        return 'Pagi'
    elif jam in sore:
        return 'Sore'
    elif jam in malam:
        return 'Malam'


def patroli(jam):
    pagi1 = list(range(8,11))
    pagi2 = list(range(11,14))
    pagi3 = list(range(14,16))
    sore1 = list(range(16,19))
    sore2 = list(range(19,22))
    sore3 = list(range(22,24))
    malam1 = list(range(0,3))
    malam2 = list(range(3,6))
    malam3 = list(range(6,8))

    if jam in pagi1:
        return 11
    elif jam in pagi2:
        return 12
    elif jam in pagi3:
        return 13
    elif jam in sore1:
        return 21
    elif jam in sore2:
        return 22
    elif jam in sore3:
        return 23
    elif jam in malam1:
        return 31
    elif jam in malam2:
        return 32
    elif jam in malam3:
        return 33


def tanggal(input): #input berupa string tanggal 'yyyy-mm-dd'
    def bulan(month):
        if month == 'Berbaris':
            month = 'Maret'
            return month
        elif month == 'Mungkin':
            month = 'Mei'
            return month
        else:
            return month

    str_tanggal = datetime.strptime(input, '%Y-%m-%d')
    str_hari = str_tanggal.strftime('%A')
    str_bulan = str_tanggal.strftime('%B')
    trans_hari = Translator().translate(str_hari, src='en', dest='id')
    trans_bulan = Translator().translate(str_bulan, src='en', dest='id')
    result = str_tanggal.strftime('{}, %d {} %Y'.format(trans_hari.text, bulan(trans_bulan.text)))
    
    return result