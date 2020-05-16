import matplotlib.pyplot as plt
import random
import numpy as np
from pylab import *
lista=[]

    
buen_rend=[['0,17','0,17','0,18','0,18','0,18','0,17','0,19','0,12','0,14','0,15'],['green']]
no_deporte=[['0,17','0,18','0,16','0,18','0,19','0,24','0,23','0,21','0,14','0,15'],['blue']]
deporte=[['0,17','0,17','0,18','0,16','0,19','0,12','0,12','0,14','0,15','0,15'],['yellow']]
bajo_rend=[['0,17','0,17','0,16','0,17','0,17','0,19','0,14','0,14','0,15','0,15'],['red']]
mala_alim=[['0,16','0,17','0,17','0,17','0,16','0,2','0,19','0,15','0,15','0,15'],['pink']]
buena_alim=[['0,16','0,16','0,17','0,12','0,13','0,14','0,15','0,15','0,15','0,15'],['orange']]

matriz=[[['0,17','0,17','0,18','0,18','0,18','0,17','0,19','0,12','0,14','0,15'],['green'],['BUEN RENDIMIENTO ACADÉMICO']],
        [['0,17','0,17','0,16','0,17','0,17','0,19','0,14','0,14','0,15','0,15'],['red'],['BAJO RENDIMIENTO ACADÉMICO']],
        [['0,17','0,17','0,18','0,16','0,19','0,12','0,12','0,14','0,15','0,15'],['blue'],['PRACTICA DEPORTE']],
        [['0,17','0,18','0,16','0,18','0,19','0,24','0,23','0,21','0,14','0,15'],['yellow'],['NO PRACTICA DEPORTE']],
        [['0,16','0,16','0,17','0,12','0,13','0,14','0,15','0,15','0,15','0,15'],['pink'],['BUENA ALIMENTACIÓN']],
        [['0,16','0,17','0,17','0,17','0,16','0,2','0,19','0,15','0,15','0,15'],['orange'],['MALA ALIMENTACIÓN']]]

for x in matriz:
    print (x[2])
    nom=x[0][0][0]
    lista.append(nom)

num_nombres=[]

colores= ['red','blue','green','yellow','black','purple','orange','pink']

x2=np.arange(5,15,1)
y2=np.arange(6,12,1)
r=1
#fig, ax = plt.subplots(1,1)
x=1
y=0
# Dibujo de la leyenda 
while y>len(lista):
    
        ax.scatter((x+5), (y+1),s=700, c = nombres[y][1], marker='o')
        ax.text((x+5), (y+1),nombres[y][0] , horizontalalignment='left',
                verticalalignment='center', fontsize=9)
        y+=1
        
plt.legend( lista, loc = 'upper left')
# Delimitar las magnitudes en los ejes x & y
#plt.xlim(0,7)
#plt.ylim(0,5)
# Muestra la figura
#fig.show()

fig, ax = plt.subplots(1,1)
z=0
z1=0
lista=[]



aleatorio=0

# Ordena los circulos de formula aleatoria o por una lista ya definida.


while True:
            z=random.randint(0,5)
            z1=random.randint(0,9)
            if lista.count([z,z1])==0:
                lista.append([z,z1])
            elif len(lista)==60:
                break
            else:
                pass

W=0
coord=[]
if aleatorio==1:
 for x in x2:
    for y in y2:

        ### DIBUJADOR
        ax.scatter(x, y,s=700, c = matriz[lista[W][0]][1][0], marker='o', alpha=10)
        ax.text(x, y,matriz[lista[W][0]][0][lista[W][1]] , horizontalalignment='center',
                verticalalignment='center', fontsize=9)
        W+=1
########
# la lista[W][0] es igual a z, lista[W][1] es igual a z1
#  color matriz[lista[W][0]][1][0], matriz[lista[W][0]] toma valores de 0 a 5, coge el segundo [1], lo toma como texto en [0], ya que solo contiene una informacion.
# texto=matriz[lista[W][0]] [0] [lista[W][1]], matriz[lista[W][0]] toma valores de 0 a 5, coge el primero[0], osea la lista de texto, lo que sigue es la posicion [lista[W][1]] de el texto toma valores de 0 a 9
######## 
else:
    # Se ingresa una lista ya antes obtenida con los datos de orden en la matriz, la segunda lista o z1 se trata de el texto puesto en cada circulo.
    lista=[[3, 6], [1, 7], [0, 4], [1, 4], [3, 7], [3, 0], [5, 3], [0, 3], [1, 2], [2, 0], [2, 4], [2, 7], [1, 8], [0, 0], [0, 9], [3, 8], [3, 2], [3, 1], [2, 5], [4, 2], [5, 7], [2, 6], [5, 4], [0, 2], [4, 9], [5, 6], [4, 5], [1, 9], [2, 1], [5, 8], [1, 3], [0, 1], [0, 5], [4, 7], [3, 9], [5, 5], [0, 6], [1, 6], [1, 1], [0, 8], [1, 5], [1, 0], [2, 3], [0, 7], [3, 4], [2, 9], [4, 6], [3, 3], [5, 1], [3, 5], [5, 9], [4, 3], [5, 0], [4, 0], [4, 8], [2, 2], [4, 1], [4, 4], [5, 2], [2, 8]]

    for x in x2:
      for y in y2:
        coord.append([x,y])
        ### DIBUJADOR
        ax.scatter(x, y,s=700, c = matriz[lista[W][0]][1][0], marker(1, 0, 45), alpha=0.71)
        ax.text(x, y,matriz[lista[W][0]][0][lista[W][1]] , horizontalalignment='center',
                verticalalignment='center', fontsize=9)
        W+=1
    
# Delimitar las magnitudes en los ejes x & y
        
plt.xlim(4,15)
plt.ylim(4,12)

# Muestra la figura
fig.show()



SIMBOLOS_TRANSFORMADOS = "a943c12f8b05de76"
SIMBOLOS_ORIGINALES = "0123456789abcdef"
def encriptacion (mensaje):
    mensaje_encriptado = ""
    for caracter in mensaje:
        i = SIMBOLOS_ORIGINALES.find(caracter)
        mensaje_encriptado += SIMBOLOS_TRANSFORMADOS[i]
    print (mensaje_encriptado)
    i = 0
    primeros_caracteres = ""
    ultimos_caracteres = ""
    for caracter in mensaje_encriptado:
        if i < 3:
            primeros_caracteres += caracter
        else:
            ultimos_caracteres += caracter
        i += 1
    mensaje_encriptado = ultimos_caracteres + primeros_caracteres
    return mensaje_encriptado

T = "a943c12f8b05de76"
O = "0123456789abcdef"
def en(da):
    da.hex()
    eo = ""
    for cr in da:
        i = O.find(cr)
        eo += T[i]
    i = 0
    ps = ""
    us = ""
    for cr in eo:
        if i < 3:
            ps += cr
        else:
            us += cr
        i += 1
    eo = us + ps
    return eo


def desencriptar (mensaje):
    ultimos_caracteres = ""
    primeros_caracteres = ""
    mensaje_encriptado = ""
    i = 0
    for caracter in mensaje:
        if i <= len(mensaje) - 4:
            ultimos_caracteres += caracter
        else:
            primeros_caracteres += caracter
        i += 1
    mensaje = primeros_caracteres + ultimos_caracteres
    for caracter in mensaje:
        i = SIMBOLOS_TRANSFORMADOS.find(caracter)
        mensaje_encriptado += SIMBOLOS_ORIGINALES[i]
    bytes.fromhex(mensaje_encriptado).decode('utf-8')
    return mensaje_encriptado



def dr (me):
    us = ""
    ps = ""
    mo = ""
    i = 0
    for cr in me:
        if i <= len(me) - 4:
            us += cr
        else:
            ps += cr
        i += 1
    me = ps + us
    for cr in me:
        i = T.find(cr)
        mo += O[i]
    mo=bytes.fromhex(mo).decode('utf-8')
    return mo








