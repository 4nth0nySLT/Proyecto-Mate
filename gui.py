#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import *
from triangulos import Maestro
from tkinter import scrolledtext
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from time import time
import threading

"""
##################################
# CODED BY 4nth0nySLT            #
# github.com/4nth0nySLT          #
# t.me/Anth0nySLT                #
#            ECUADOR             #
##################################
"""

Maestro=Maestro()

def textbreak(event):
	return "break"

def solonumeros(event):
	try:
		if event.keysym=='BackSpace' or event.keysym=='period':
			return
		float(event.keysym)
		return
	except:
		return "break"


def dibujar(forma,angulo):
	if forma==-1:
		Maestro.forma=0
	else:
		Maestro.forma=int(forma)
	if angulo=='':
		Maestro.angulo=15
	if angulo=="91179":
		# Easter Egg
		ax.clear()
		for i in range(95,180):
			Maestro.angulo=i
			Maestro.dibujador()
			for i in Maestro.puntos_en_el_grafico:
				ax.plot(i[0],i[1])
				line.draw()
                        
	else:
		Maestro.angulo=float(angulo)
	Maestro.dibujador()
	ax.clear()
	ax.grid(True)
	ax.set_title("π≈"+str(Maestro.pi)+" Ángulo="+str(Maestro.angulo)+Maestro.error)
	if Maestro.forma==0:
		ax.set_xlabel("Polígono de "+str(int(Maestro.numero_de_triangulos))+" lados.")
	else:
		ax.set_xlabel(str(int(Maestro.numero_de_triangulos))+" triángulos.")
	#import pyperclip
	#text=""
	#for i in Maestro.puntos_en_el_grafico:
	#	print(i[0][0],"\t",i[0][1],"\t\r\n",i[1][0],"\t",i[1][1],"\t\r\n")
	#	text=text+str(i[0][0]).replace(".",",")+"\t"+str(i[0][1]).replace(".",",")+"\t"+str(i[1][0]).replace(".",",")+"\t"+str(i[1][1]).replace(".",",")+"\t\r\n"
	#pyperclip.copy(text)
	# Pasar datos a tabla x1, x2, y1, y2. Se almacenan en su portapapeles



	for i in Maestro.puntos_en_el_grafico:
		ax.plot(i[0],i[1])
		line.draw()
	pass

def stop_hilo(hilo):
	hilo.do_run=False
	hilo.join(0.1)
	boton_cancelar.place(x=9999,y=medio-40,width=75,height=23)

def pi_sumatoria(numero_maximo):
	if numero_maximo=="":
		return
	hilo = threading.Thread(target=sumatoria, 
                            args=(1,numero_maximo),
                                    daemon=True)
	hilo.start()
	boton_cancelar.place(x=80,y=medio-40,width=75,height=23)
	boton_cancelar.bind("<Button-1>", lambda x : stop_hilo(hilo))


def conversion(seg): 
    horas=00
    mins=00
    if seg>=3600:
       hrs = seg // 3600
       seg -= 3600*hrs
    if seg>=60:
       mins = seg // 60
       seg -= 60*mins
    if seg<60:
        pass 
    return (str(int(horas))+' horas '+str(int(mins))+ ' minutos '+str(int(seg))+' segundos')  

def sumatoria(uno,numero_maximo):
	hilo = threading.currentThread()
	timeini=time()
	suma=0
	for x in range(1,int(numero_maximo)+1):
		if getattr(hilo, "do_run", True):
			suma+=1/x**2
			pi="π≈"+str((suma*6)**0.5)
			debug.delete("1.0", END)
			debug.insert(INSERT,pi)
		else:
			break
	debug.insert(END," "+conversion((time()-timeini)))
	boton_cancelar.place(x=99999,y=medio-40,width=75,height=23)

def dibujador():
	window.geometry('720x510')
	debug.place(x=9999,y=medio-95,width=691,height=21)
	label_suma.place(x=99910,y=medio-95)
	entrada_suma.place(x=69990,y=medio-95,width=120,height=23)
	boton_suma.place(x=499990,y=medio-70,width=75,height=23)
	label_forma.place(x=10,y=medio-95)
	forma.place(x=60, y=medio-95,width=165)
	label_angulo.place(x=10,y=medio-45)
	angulo.place(x=60,y=medio-45,width=120,height=23)
	Boton_dibujar.place(x=80,y=medio,width=75,height=23)
	label_creditos.place(x=10,y=medio+40)
	debug_creditos.place(x=9999,y=medio-95)
	line.get_tk_widget().pack(side=LEFT, fill=BOTH,expand=1)

def sumador():
	window.geometry('720x150')
	label_forma.place(x=19990,y=medio-95)
	forma.place(x=69990, y=medio-95,width=165)
	label_angulo.place(x=19990,y=medio-45)
	debug_creditos.place(x=180,y=0)
	angulo.place(x=699990,y=medio-45,width=120,height=23)
	Boton_dibujar.place(x=99999,y=medio,width=75,height=23)
	line.get_tk_widget().pack_forget()
	label_suma.place(x=10,y=medio-95)
	entrada_suma.place(x=120,y=medio-95,width=120,height=23)
	boton_suma.place(x=80,y=medio-70,width=75,height=23)
	debug.place(x=10,y=medio-55,width=691,height=21)

medio=150
try:
	window=Tk()
	window.geometry('720x510')
	window.resizable(width=False, height=False)
	window.title("Proyecto Matemáticas")

	label_forma=Label(window,text='Forma:')
	label_forma.place(x=10,y=medio-95)
	forma = Combobox(window, state="readonly")
	forma["values"] = ["Circunferencia", "Triángulos dentro del circulo","Triángulos desde la derecha","Deformación"]
	forma.place(x=60, y=medio-95,width=165)

	label_angulo=Label(window,text='Angulo:')
	label_angulo.place(x=10,y=medio-45)
	angulo=Entry(window)
	angulo.place(x=60,y=medio-45,width=120,height=23)
	angulo.bind("<Key>", lambda e: solonumeros(e))

	label_creditos=Label(window,text="####################\n# CODED BY 4nth0nySLT\n# github.com/4nth0nySLT\n# t.me/Anth0nySLT\n#            ECUADOR                     \n####################")
	label_creditos.place(x=10,y=medio+40)

	cuadro = Frame(window)
	cuadro.place(x=230,y=20,width=460,height=460)
	debug_creditos=Label(cuadro,text="####################\n# CODED BY 4nth0nySLT\n# github.com/4nth0nySLT\n# t.me/Anth0nySLT\n#            ECUADOR                     \n####################")
	
	figure = plt.Figure(figsize=(5,6), dpi=100)
	ax = figure.add_subplot(111)
	ax.grid(True)
	line = FigureCanvasTkAgg(figure, cuadro)
	line.get_tk_widget().pack(side=LEFT, fill=BOTH,expand=1)

	Boton_dibujar= Button(window, text="Dibujar")
	Boton_dibujar.place(x=80,y=medio,width=75,height=23)
	Boton_dibujar.bind("<Button-1>", lambda x : dibujar(forma.current(),angulo.get()))

	debug = scrolledtext.ScrolledText(cuadro,background='#252a2c',foreground='#ffffff')
	label_suma=Label(window,text="Número máximo:")
	entrada_suma=Entry(window)
	entrada_suma.bind("<Key>", lambda e: solonumeros(e))
	boton_suma=Button(window, text="Sumar")
	boton_suma.bind("<Button-1>", lambda x : pi_sumatoria(entrada_suma.get()))
	boton_cancelar=Button(window, text="Cancelar")


	boton_metodo1=Button(window, text="Triángulos")
	boton_metodo1.place(x=40,y=medio-125,width=75,height=23)
	boton_metodo1.bind("<Button-1>", lambda x : dibujador())

	boton_metodo2=Button(window, text="Sumatoria")
	boton_metodo2.place(x=120,y=medio-125,width=75,height=23)
	boton_metodo2.bind("<Button-1>", lambda x : sumador())


	window.mainloop()

except Exception as e:
	print(e)


