from http.client import ImproperConnectionState
from pickletools import read_uint1
from django import views
from django.shortcuts import render
from django.http import HttpResponse
import pyautogui as pg

def test(request):
    pg.moveTo(x=500, y=500)

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def tiktok(request):
    return render(request, 'main/tiktok.html', test(request))
    #return pg.moveTo(x=500, y=500)

def sites(request):
    return render(request, 'main/sites.html')

def cryptowin(request):
    return render(request, 'main/cryptowin.html')

def bitcoin(request):
    return render(request, 'main/bitcoin.html')

def bits(request):
    return render(request, 'main/bits.html')
