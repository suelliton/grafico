from django.shortcuts import render
import os
import csv
from forms import FormArquivo
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
# Funcao imaginaria para manipular um upload de arquivo.
from django.core.files.uploadedfile import UploadedFile
"""
def index(request):
    form = FormArquivo(request.POST, request.FILES)
    if request.method == "POST":

        if form.is_valid():
            arq = request.FILES['arq']
            grafico(arq)
            return render_to_response('grafico/grafico.html/',{'form':form})
    else:

        form = FormArquivo()
        return render_to_response('grafico/index.html/', {'form': form})



def grafico(arquivo):
#aqui tenho que receber o arquivo de texto em estado bruto





    x =[]
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0


    with open(arquivo) as csvfile:
        reader = csv.reader(csvfile, delimiter='	')
    for row in reader:
        x.append(float(row[0]))

    for i in range(0,len(x)-1):
	    if(x[i] >10.0  and x[i] <= 12.2):
		    a +=1
	    elif( x[i] <= 14.4):
		    b +=1
	    elif( x[i] <= 16.6):
		    c +=1
	    elif( x[i] <= 18.8):
		    d +=1
	    else:
		    e +=1
    dados = [a,b,c,d,e]
    return render_to_response('grafico/grafico.html',{})
"""

def  index ( request ): 
    if request.method  ==  'POST' : 
        form = FormArquivo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return grafico(request,request.FILES['arq'].read())
            
    else : 
        form = FormArquivo() 
    return  render ( request ,'grafico/index.html' ,  { 'form' :  form })




def grafico(request,arq):
    x =[]
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    data = []
    with open('/home/suelliton/projetos/grafico/graphic/media/seeds.csv')  as destination:        
        reader=csv.reader(destination, delimiter = '\t')
        for row in reader:                            
            x.append(float(row[0]))

    for i in range(0,len(x)-1):
        if(x[i] >10.0  and x[i] <= 12.2):
            a +=1
        elif( x[i] <= 14.4):
            b +=1
        elif( x[i] <= 16.6):
            c +=1
        elif( x[i] <= 18.8):
            d +=1
        else:
            e +=1

    

    def bubble_sort(lista):
        for i in range(0, len(lista)-1):
            for j in range(0, len(lista)-1-i):
                if lista[ j ] > lista[j + 1]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
                return lista

    ordenado = bubble_sort(x)


    frequenciaAcumulada=[]
 
    for i in range(0,len(ordenado)-1):
        acumulo = 1 
        vp=1
        sair = False
        if i==0:
            anterior = 0


        while sair == False:    
            if ordenado[i] == ordenado[i+vp]:
                acumulo = acumulo+1
                vp = vp+1
            
            else:
                sair = True

        acumuloFinal = acumulo + anterior
        anterior = acumuloFinal
        frequenciaAcumulada.append(acumuloFinal)
        
        if vp >= 2:
            i=i+vp            

    os.remove('/home/suelliton/projetos/grafico/graphic/media/seeds.csv')
    
    dados = [a,b,c,d,e]
    d={'dados':dados,'freq':frequenciaAcumulada}
    return render(request,'grafico/grafico.html/',d)    
