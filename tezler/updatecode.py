from tika import parser
import sys

file_url = sys.argv[1]
x=[];
raw = parser.from_file('.'+file_url)
output=raw['content']

output=output.lower()
output=output.replace("i̇","i")
output=output.replace("\n ","")
output=output.replace("\n\n\n","\n")
output=output.replace("\n\n","\n")
output=output.replace("\n\n\n","")
#output=output.replace("\n\n","\n")
output=output.split(" \n")

    





ogrencisayı=1
Pb_1=0
cümle=0
if "\n" not in output[5]:
    cümle=1
    Pb_1=1
    v1=output[4]+" "+output[5]
    v1=v1.strip("\n")
    if "\n" not in output[6]:
        cümle=2
        Pb_1=2
        v1=output[4]+" "+output[5]+" "+output[6]
        v1=v1.strip("\n")
        if "\n" not in output[7]:
            cümle=2
            Pb_1=3
            v1=output[4]+" "+output[5]+" "+output[6]+" "+output[7]
            v1=v1.strip("\n")
    

else:
    v1=output[4].strip("\n")
print("-----Başlık-----")
print(v1)

baslik=v1

ogrenci3=""
ogrenci2=""

print("-----isim1-----")
v2=output[5+Pb_1].strip("\n")
print(v2)
ogrenci1=v2

öğrenci=1;
if "2" not in output[6+Pb_1]:
    print("-----isim2-----")
    print(output[6+Pb_1])
    ogrenci2=output[6+Pb_1]
    ogrencisayı+=1
    Pb_1=Pb_1+1
    
    if "2" not in output[6+Pb_1]:
        print("-----isim33-----")
        print(output[6+Pb_1])
        ogrenci3=output[6+Pb_1]
        ogrencisayı+=1
        Pb_1=Pb_1+1#--------------------------------------- 3 satır artma ihtimali var

        
        
        
        
        
        
v3=output[10+Pb_1].strip("\n")
print("-----proje türü-----")
print(v3)
tur=v3





x=0
for i in output:
    
    if "danışman," in i:
        hoca1=x
    x=x+1

    
print("-----hocalar-----")
h1=output[hoca1-1].strip("\n")

h2=output[hoca1+1].strip("\n")

h3=output[hoca1+3].strip("\n")

listehoca=[]
listehoca.append(h1)
listehoca.append(h2)
listehoca.append(h3)
parcahoca1=[]
parcahoca2=[]
for i in listehoca:
    if "üyesi" not in i:
        
        gec1=i.split(". ")
        gec1[0]+="."
        parcahoca1.append(gec1)
        
    else:
        gec2=i.split("üyesi ")
        gec2[0]+="üyesi"
        parcahoca2.append(gec2)

for i in parcahoca2:     
        parcahoca1.append(i)      

        
danışman_unvan=parcahoca1[0][0]
danışman_ad=parcahoca1[0][1]
print("-----danışman-----")
print(danışman_unvan)
print(danışman_ad)


juri1_unvan=parcahoca1[1][0]
juri1_ad=parcahoca1[1][1]
print("-----juri1-----")
print(juri1_unvan)
print(juri1_ad)


juri2_unvan=parcahoca1[2][0]
juri2_ad=parcahoca1[2][1]
print("-----juri2-----")
print(juri2_unvan)
print(juri2_ad)

danışman=danışman_unvan+" "+danışman_ad
juri1=juri1_unvan+" "+juri1_ad
juri2=juri2_unvan+" "+juri2_ad




donem=""
tarih=output[hoca1+5]
tarih=tarih.split(": ")
yıl=tarih[1][6]+tarih[1][7]+tarih[1][8]+tarih[1][9]
yıl=str(int(yıl))+"-"+str(int(yıl)+1)
print("-----tarih-----")
print(yıl)

if tarih[1][4]=="4" or tarih[1][4]=="5" or tarih[1][4]=="6" or tarih[1][4]=="7" or tarih[1][4]=="8" :
    print("bahar")
    donem="bahar"

if tarih[1][4]=="1" or tarih[1][4]=="2" :
    print("güz")
    donem="güz"
    
yıl+=" "
yıl+=donem    
    
    
 
x=0
for i in output:
    
    if "öğrenci no" in i:
        y=x
        break
    x=x+1    
    
ogr3_no=0
ogr2_no=0
ogr2_ogrenim=""
ogr3_ogrenim=""
    
    
print("-----öğrenci no-----")
ogr1=output[y].split(": ")
ogr1=ogr1[1]
print(ogr1)
ogr1_no=ogr1

if ogr1_no[5]=="1":
    ogr1_ogrenim="1.öğretim"
    print(ogr1_ogrenim)
else:
    ogr1_ogrenim="2.öğretim"
    print(ogr1_ogrenim)




if 1<ogrencisayı:  
    ogr2=output[y+3].split(": ")
    ogr2=ogr2[1]
    print(ogr2)
    ogr2_no=ogr2

    if ogr2_no[5]=="1":
        ogr2_ogrenim="1.öğretim"
        print(ogr2_ogrenim)
    else:
        ogr2_ogrenim="2.öğretim"
        print(ogr2_ogrenim)





if 2<ogrencisayı:  
    ogr3=output[y+6].split(": ")
    ogr3=ogr3[1]
    print(ogr3)
    ogr3_no=ogr3
    
    if ogr3_no[5]=="1":
        ogr3_ogrenim="1.öğretim"
        print(ogr3_ogrenim)
    else:
        ogr3_ogrenim="2.öğretim"
        print(ogr3_ogrenim)



x=0
for i in output:
    
    if "anahtar kelimeler" in i:
        y=x
    x=x+1

ozett=""
say=output.index("özet")
while(say<y-1):
    say=say+1
    ozett+=str(output[say].replace("'"," "))+" "
print("-----özet-----")
print(ozett)   
    
    
    
    

x=0
for i in output:
    
    if "anahtar kelimeler" in i:
        y=x
    x=x+1

    
anahtar=""    
anahtarsatır=0
say2=y
while(say2<y+5):
    
    if "\n" not in output[say2]:
        anahtarsatır+=1
        anahtar+=output[say2]
        anahtar+=" "
    else:
        break
    say2+=1

anahtar=anahtar.rstrip()
anahtar=anahtar.split(".")
anahtar=anahtar[0]
anahtar=anahtar.split(", ")
xxx=anahtar[0].split(": ")
xx=xxx[1]
xx

anahtar.append(xx)
anahtar.pop(0)
anahtar_kelme=""
for i in anahtar:
    anahtar_kelme+=str(i)+","
anahtar_kelme=anahtar_kelme.rstrip(",")    
print("-----anahtar kelimeler-----")
print(anahtar_kelme)


import mysql.connector
 
mysqldb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="django_websitesi2"
)
cursor = mysqldb.cursor()


ogrenci1=ogrenci1
ogrenci1_no=ogr1_no
ogrenci1_ogretim=ogr1_ogrenim
ogrenci2=ogrenci2
ogrenci2_no=ogr2_no
ogrenci2_ogretim=ogr2_ogrenim
ogrenci3=ogrenci3
ogrenci3_no=ogr3_no
ogrenci3_ogretim=ogr3_ogrenim
danisman=danışman
juri1=juri1
juri2=juri2
anahtar=anahtar_kelme
ozet=ozett
ders_adi=tur
donem=yıl
baslik=baslik



sql2 = "UPDATE tezler_tez SET ogrenci1='{}',ogrenci1_no='{}',ogrenci2='{}',ogrenci2_no='{}',ogrenci3='{}',ogrenci3_no='{}',danisman='{}',juri1='{}',juri2='{}',anahtar='{}',ozet='{}',ders_adi='{}',donem='{}',baslik='{}',ogrenci1_ogretim='{}',ogrenci2_ogretim='{}',ogrenci3_ogretim='{}' Where tez='{}'".format(ogrenci1,ogrenci1_no,ogrenci2,ogrenci2_no,ogrenci3,ogrenci3_no,danisman,juri1,juri2,anahtar,ozet,ders_adi,donem,baslik,ogrenci1_ogretim,ogrenci2_ogretim,ogrenci3_ogretim,file_url)
print(sql2)
cursor.execute(sql2)
mysqldb.commit()   
print("[+] Veri Eklendi")