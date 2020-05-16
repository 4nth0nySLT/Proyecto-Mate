from random import randint
import numpy as np
from math import asin, acos, sin, cos, sqrt
"""
##################################
# CODED BY 4nth0nySLT            #
# github.com/4nth0nySLT          #
# t.me/Anth0nySLT                #
#            ECUADOR             #
##################################
"""

class Maestro():
	def __init__(self):
		self.radio=1
		self.angulo=1
		self.forma=1
		"""
0 -> Circunferencia
1 -> Triangulos dentro del circulo
2 -> Triangulos desde la derecha
3 -> Deformacion
		"""
		self.vueltas=1
		self.pi=0
		self.altura_y=0
#	Creacion de datos base, el diametro
		self.centro=0

#	Lista donde se guardaran los puntos del grafico
		self.puntos_en_el_grafico=[]


	def dibujador(self):
		self.puntos_en_el_grafico=[]
		self.radio_derecha=self.centro+self.radio
		self.radio_izquierda=self.centro-self.radio
		if self.forma!=0:
			self.puntos_en_el_grafico.append([[self.centro,self.radio_derecha],[self.altura_y,self.altura_y]])
		alfa=self.angulo
		b=float((180-alfa)/2)
		self.medida_del_cateto=float((sin(np.radians(alfa))*self.radio)/sin(np.radians(b)))
		print(self.medida_del_cateto)
		
		self.numero_de_triangulos=float((360*self.vueltas)//alfa)
		suma2=self.numero_de_triangulos
		print(self.numero_de_triangulos)

		self.pi=(self.medida_del_cateto*self.numero_de_triangulos)/(2*self.radio)

		if (360*self.vueltas)%alfa!=0:
			# ARREGLO SI NO ES MULTIPLO
			self.numero_de_triangulos+=1
		contador_de_triangulos=1
		h2=self.altura_y
		f2=self.radio_derecha
		while self.numero_de_triangulos>=contador_de_triangulos:
			try:
				print(alfa)
				b=(180-alfa)/2
				self.medida_del_cateto=float((sin(np.radians(alfa))*self.radio)/sin(np.radians(b)))
				print(self.medida_del_cateto)
				xN=float(self.radio_derecha-cos(np.radians(b))*self.medida_del_cateto)
				yN=self.altura_y+sin(np.radians(b))*self.medida_del_cateto
				if self.numero_de_triangulos>suma2:
					self.error='\nError, 360/'+str(self.angulo)+', no es exacto'
				else:
					self.error=""

				if self.forma==0:
					# Circunferencia
					self.puntos_en_el_grafico.append([[xN,f2],[yN,h2]])
					f2=xN
					h2=yN
				elif self.forma==1:
					#Triangulos dentro del circulo
					self.puntos_en_el_grafico.append([[self.altura_y,self.centro,xN,f2],[self.altura_y,self.altura_y,yN,h2]])
					f2=xN
					h2=yN
				elif self.forma==2:
					#Triangulos desde la derecha
					self.puntos_en_el_grafico.append([[self.centro,self.radio_derecha,xN,self.centro],[self.altura_y,h2,yN,self.altura_y]])
				else:
					#Deformacion
					self.puntos_en_el_grafico.append([[self.centro,self.radio_derecha,xN,self.centro],[self.altura_y,h2,yN,self.altura_y]])
					f=xN
					h2=yN

				contador_de_triangulos+=1
				alfa=self.angulo*contador_de_triangulos
			except:
				## Calculando el ultimo triangulo donde algunos valores se convierten en 0
				## y tambien se modifican los valores permitidos, forzandolos a colocarse correctamente
				if self.forma==0:
					self.puntos_en_el_grafico.append([[self.radio_izquierda,f2],[self.altura_y,h2]])
				else:
					self.puntos_en_el_grafico.append([[self.altura_y,self.radio_izquierda,self.radio_izquierda,f2],[self.altura_y,self.altura_y,self.altura_y,h2]])
				f2=self.radio_izquierda
				h2=self.altura_y
				contador_de_triangulos+=1
				alfa=self.angulo*contador_de_triangulos
				pass  



