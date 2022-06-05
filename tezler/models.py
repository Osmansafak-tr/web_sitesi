from django.db import models

# Create your models here.
class Tez(models.Model):
    baslik = models.CharField(max_length=300,null=True,blank=True)
    ogrenci1 = models.CharField(max_length=45,null=True,blank=True)
    ogrenci1_no = models.CharField(max_length=45,null=True,blank=True)
    ogrenci1_ogretim = models.CharField(max_length=45,null=True,blank=True)
    ogrenci2 = models.CharField(max_length=45,null=True,blank=True)
    ogrenci2_no = models.CharField(max_length=45,null=True,blank=True)
    ogrenci2_ogretim = models.CharField(max_length=45,null=True,blank=True)
    ogrenci3 = models.CharField(max_length=45,null=True,blank=True)
    ogrenci3_no = models.CharField(max_length=45,null=True,blank=True)
    ogrenci3_ogretim = models.CharField(max_length=45,null=True,blank=True)
    danisman = models.CharField(max_length=45,null=True,blank=True)
    juri1 = models.CharField(max_length=45,null=True,blank=True)
    juri2 = models.CharField(max_length=45,null=True,blank=True)
    anahtar = models.CharField(max_length=1024,null=True,blank=True)
    ozet = models.CharField(max_length=3000,null=True,blank=True)
    ders_adi = models.CharField(max_length=45,null=True,blank=True)
    donem = models.CharField(max_length=45,null=True,blank=True)
    kullanici = models.CharField(max_length=45,null=True,blank=True)
    tez = models.FileField(upload_to='pdfs/',null=True,blank=True)

    def __str__(self):
        return self.baslik



    