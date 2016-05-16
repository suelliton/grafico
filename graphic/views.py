from django.shortcuts import render
import csv

def index(request):
     post = 3
     return render(request, 'grafico/index.html',{'post':post})

def grafico(request):
#aqui tenho que receber o arquivo de texto em estado bruto
    x = []
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    #aqui em vez de abri o arq seeds.csv tenho que abrir o arquivo que veio do index
    #with open('seeds.csv') as csvfile:
     #reader = csv.reader(csvfile, delimiter='	')
     #for row in reader:
    #    x.append(float(row[0]))

    '''for i in range(0,len(x)-1):
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
    dados = [a,b,c,d,e]'''
    return render(request,'grafico/grafico.html')
