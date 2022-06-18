from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tiktok', views.tiktok, name='tiktok'),
    path('sites', views.sites, name='sites'),
    path('cryptowin', views.cryptowin, name='cryptowin'),
    path('bitcoin', views.bitcoin, name='bitcoin'),
    path('bits', views.bits, name='bits')
]