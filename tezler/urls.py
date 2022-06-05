from os import name
from django.urls import path
from .views import AnaSayfaView, TezCreateView,UploadPageView,TezListView,Sorgu1ListView,Sorgu2ListView,Sorgu1AdminView,Sorgu2AdminView,metin_isleme,new,sorgula_1

urlpatterns = [
    path('',AnaSayfaView.as_view(),name='home'),
    path('upload/',UploadPageView.as_view(),name='upload'),
    path('tezler/',TezListView.as_view(),name='tez_liste'),
    path('tezler/ekle',TezCreateView.as_view(),name='tez_ekle'),
    path('sorgu1/',Sorgu1ListView.as_view(),name='sorgu1'),
    path('sorgu2/',Sorgu2ListView.as_view(),name='sorgu2'),
    path('admin/sorgu1',Sorgu1AdminView.as_view(),name='sorgu1_admin'),
    path('admin/sorgu2',Sorgu2AdminView.as_view(),name='sorgu2_admin'),
    path('new/',new),
    path('metin_isleme/',metin_isleme),
    path('sorgula_1/',sorgula_1),
]
