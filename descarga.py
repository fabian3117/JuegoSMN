import requests;
import os;

from funciones import *


dirBase='C:/Users/fede/Desktop/asysTP/datos/'
aaaaBase    =   2018

ddBase  = 1

mmBase  =   1

STRINGDIIR=str(aaaaBase)+"0"+str(mmBase)+"0"+str(ddBase)




url = 'https://ssl.smn.gob.ar/dpd/descarga_opendata.php?file=observaciones/datohorario'+STRINGDIIR+'.txt'

#print(url)

#myfile = requests.get(url)

#print(myfile.content)

#open('C:/Users/fede/Desktop/asysTP/datos/prueba,txt', 'wb').write(myfile.content)
it=2
#Con esto puedo generar las variaciones de dia para descargar mis registros <--

mm=mmBase
aaaa=aaaaBase
dd=ddBase
ddp=dd
mmp=mm
aaap=aaaa

aaaa=str(aaap)
mm=str(mmp)
aaaa="2019"
VariaAnio(dirBase)
#if mmp<10:
 #       mm='0'+str(mmp)

  

 # 

#Faltan Variaciones del mes <--
#for m in range(12):



#Esto genera las variaciones del dia 01 al 31   <--
