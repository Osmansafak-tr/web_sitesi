from django.shortcuts import render

from django.views.generic import TemplateView,ListView,CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .models import Tez
from .forms import TezForm
from subprocess import run,PIPE
import sys
 
# Create your views here.

class AnaSayfaView(TemplateView):
    template_name = 'home.html'

class UploadPageView(TemplateView):
    template_name = 'upload.html'

class TezListView(ListView):
    model = Tez
    context_object_name = 'tezler'
    template_name = 'tez_liste.html'

class TezCreateView(CreateView):
    model = Tez
    template_name = "tez_ekle.html"
    form_class = TezForm
    success_url = reverse_lazy('home')

class Sorgu1ListView(ListView):
    model = Tez
    template_name = 'sorgu1.html'
    context_object_name = 'tezler'

class Sorgu2ListView(ListView):
    model = Tez
    template_name = 'sorgu2.html'
    context_object_name = 'tezler'

class Sorgu1AdminView(ListView):
    model = Tez
    template_name = 'sorgu1_admin.html'
    context_object_name = 'tezler'

class Sorgu2AdminView(ListView):
    model = Tez
    template_name = 'sorgu2_admin.html'
    context_object_name = 'tezler'

def new(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        print(uploaded_file)
        print(uploaded_file.name)
        
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        uploaded_file_url = fs.url(uploaded_file.name)

        _kullanici = request.user.username
        _tez = uploaded_file_url

        o_ref  = Tez(kullanici = _kullanici,tez = _tez)
        o_ref.save()
    
    return render(request,'metin_isleme.html',{'data_file_url':uploaded_file_url})

def metin_isleme(request):
    file_url = request.POST.get('file_url')
    out = run([sys.executable,'.//tezler//updatecode.py',file_url],shell=False,stdout=PIPE)

    return render(request,'home.html')

def sorgula_1(request):
    input = request.POST.get('input')
    out = run([sys.executable,'.//tezler//sorgu1.py',input],shell=False,stdout=PIPE)
    print(out)
    print(type(out))
    print(type(out.stdout))
    dizi = out.stdout.split()

    return render(request,'sorgu1.html',{'data_baslik':dizi[0]})


