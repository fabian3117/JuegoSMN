import requests;
import os;
def DiaVaria(dirBase,aaaa,mmBase):

    for i in range(1,31,1):
        
        dd=str(i)
    
        if i<10:
            dd='0'+str(i)
        
        STRINGDIIR=aaaa+mmBase+dd
        
        url = 'https://ssl.smn.gob.ar/dpd/descarga_opendata.php?file=observaciones/datohorario'+STRINGDIIR+'.txt'
        myfile = requests.get(url)
        os.makedirs(dirBase+aaaa,exist_ok=True)
        open(dirBase+aaaa+"/"+STRINGDIIR+".txt", 'wb').write(myfile.content)
        print("Dia",url)
    


def VariaMes(dirBase,aaaa):
    for m in range(1,13,1):
    #Genera la variacion de los meses Deseada   <--
        
        
        if m<10:
            #print("meS : ",m)
            DiaVaria(dirBase,str(aaaa),"0"+str(m))
        else:
            #print("meS : ",m)
            DiaVaria(dirBase,str(aaaa),str(m))
   # 
    
    

def VariaAnio(dirBase):
    #Tomo como base 2018 Puesto que es el que vi que esta como minimo   <--
    for a in range(2021,2022,1):
        #print("ANIO : ",a)
        VariaMes(dirBase,a)

    #Variaciones del anio lista <--
    #VariaAnio(a);
