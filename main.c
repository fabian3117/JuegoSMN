#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define DIRBASE "C:/Users/fede/Desktop/asysTP/datos/"
#define ModoTex "t"

#define AnioBase 2018

//-->   Formato de las carpetas es ./Anio/aaaaddmm.txt 
//dirBase=''

int main (void) {

//-->   Primero abro el archivo de .txt <---
FILE* f;
char directorio[45]={DIRBASE};
char subdir[8]={""};
char med[4];
int anio=AnioBase;
int mes=1;
int dia=1;
//strcat
sprintf(subdir,"%s%s%s",anio,mes,dia);
sprintf(directorio,"%s%d",DIRBASE,anio);
sprintf(directorio,"%s%d",DIRBASE,anio);

if(mes<10){
    //strcat(subdir,"0");
    sprintf(subdir,"%d0%d",anio,mes);    
}
else{
    sprintf(subdir,"%d%d",anio,mes);    
}

if(dia<10){
    sprintf(subdir,"%s0%d",subdir,dia);    
}
else{
    sprintf(subdir,"%s%d",subdir,dia);    
}



sprintf(med,"%d/",anio);
strcat(directorio,med);
//sprintf(directorio,"%s%d",cosa,anio);
//printf("%s",directorio);

printf("\n\r%s",directorio);
//-->   Ahora tnego que abrir el archivo en si  <--
//-->   /AAAAMMDD   <--

//strcat(directorio,"")
//-->   Formato de mi nuevo string es anio-mes-dia
f=fopen(directorio, "r");

    
}