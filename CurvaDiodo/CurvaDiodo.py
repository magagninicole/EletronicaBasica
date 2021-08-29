import matplotlib.pyplot as mp
import math
import numpy

IS = 1*10**(-16)
Vt = 0.025
passo = 0.001
i = 0.0


#CÁLCULO DE ID
VD = numpy.arange(0, .8, passo)
ID = IS*(numpy.exp(VD/Vt)-1)

#CÁLCULO RETA DE CARGA
Vcc = 10
rs = 2000
id = (-VD + Vcc)/rs

mp.subplot(2,1,1)
mp.plot(VD, ID)
mp.subplot(2,1,1)
mp.plot(VD, id, 'r')
mp.title('Curva do Diodo e reta de carga')

mp.grid()
mp.show()