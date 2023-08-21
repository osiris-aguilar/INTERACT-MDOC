
"""
Created on Sun Sep 19 08:36:52 2021

@author: oosiris
"""

import numpy as np
import math as math
import matplotlib.pyplot as plt

# DATOS DE ENTRADA
#dp=1   # este valor es comun para el modulo previo
#Vs=100 # este valor es comun para el modulo previo
#v=0.311 # este valor es comun para el modulo previo
#epsilon=0.02 # este valor es comun para el modulo previo

#Lysmer=3.4*Vs/(np.pi*(1-v))
#x=np.array([-1.45,1.45,-1.45,1.45],dtype=complex) # fuciona con complejos también
#y=np.array([1.45,1.45,-1.45,-1.45],dtype=complex)# como se puede observar, el método funciona incluso con números complejos

""" CALCULO DE LAS IESIMAS DISTANCIAS DE LA MATRIZ"""
def INTERACT3 (dp,Vs,v,epsilon,x,y,Lysmer):


    s=[]
    for i in range (0,len(x)):
        kz=[]
        for w in range (0,len(x)):
            s_1=((x[i]-x[w])**2+(y[i]-y[w])**2)**0.5
            kz.append(s_1)
        s.append(kz)
    s=np.array(s)
    #s12=np.reshape(s,(len(x),len(x))) este sería otro metodo sin utilizar k[]
    #print(s)
    """ CALCULO DE LOS IESIMOS ANGULOS ENTRE PILOTES"""
    beta=[]
    for i in range (0,len(x)):
        ksss=[]
        for w in range (0,len(x)):
            if i==w: # condicionante para que la matriz diagonal sea de unos
                beta_1=1
                ksss.append(beta_1)
            elif (x[i]-x[w])==0: # condicionante para que no divida entre cero y marque nan o inf (valores nulos o infinito)
                beta_1=np.pi*0.5 # revisar bien esta condición
                ksss.append(beta_1)
            elif i!=w: # conficionante para cualquier otro angulo distinto de cero y 90 grados (el signo de admiración invertido es para formar la desigualdad junto con el igual)
                beta_1=(y[i]-y[w])/(x[i]-x[w])# aqui podría haber un conflicto
                ksss.append(np.arctan(beta_1))
        beta.append(ksss)
    beta=np.array(beta)
    #beta=np.arctan(beta)  # se obtiene el angulo cuyo tangenete
    
    #print(beta)
    
    #beta=np.nan_to_num(beta,copy=True,nan=0, posinf=90, neginf=90) # excelente para reemplazar los ceros e infinitos por el valor que se requiera
    
    
    # ============================DEFINICIÓN DE LAS FRECUENCIAS ANGULARES=========================
    frec_ang=[]
    
    for omega in range (0,100,1):
        incremento=1
        omega_1=incremento*omega
        frec_ang.append(omega_1)
    frec_ang=np.array(frec_ang)  # VECTOR DE FRECUENCIAS ANGULARES
    
    Fact=[] #factor final de para horizontales
    Fact_v=[]#factor final de para verticales
     # DEFINICION DE FACTOR DE GRUPO COMO UN VECTOR
    
    """ PARA LAS ONDAS PRIMARIAS EN COMPRESION (NO TOMA EN CUENTA LOS COSENOS Y SENOS  CUADRADOS , ES UN PASO PREVIO) """
    for ww in range(0,100,1):
        alfa_h1=(2*s/dp)**(-0.5) # aqui la parte no exponencial para la onda p
        alfa_h1=np.nan_to_num(alfa_h1,copy=True,nan=1, posinf=1, neginf=1) # revisar si esto es cierto
        alfa_h2=np.exp((-1)*epsilon*s*frec_ang[ww]/Lysmer) # aqui la parte exponencial para la onda p
        alfa_h3=np.cos(frec_ang[ww]*s/Lysmer) # aqúi la parte real
        alfa_h4=np.sin(frec_ang[ww]*s/Lysmer) # aquío la parte imaginaria
        
        alfa_h=[]
        for i in range (0,len(x)):
            ki=[]
            for w in range (0,len(x)):
                if i==w: # este no necesariamiente es cierto porque no es la matriz alga final, es solo el calculo local de alfa (i,j) que despues deberá multiplicarse por los respectivos angulos de inclinacion coseno y seno
                    alfas_1=1
                    ki.append(alfas_1)
                elif i!=w:
                    alfas_1=alfa_h1[i,w]*alfa_h2[i,w]*(alfa_h3[i,w]-alfa_h4[i,w]*1j)
                    ki.append(alfas_1)
            alfa_h.append(ki)
        alfa_h=np.array(alfa_h)
        
        """ CALCULO DE LOS IESIMOS VALORES DE ALFA P (PARA ONDAS SECUNDARIAS DE CORTANTE)"""
        alfa_v1=(2*s/dp)**(-0.5) # aqui la parte no exponencial para la onda p
        alfa_v1=np.nan_to_num(alfa_v1,copy=True,nan=1, posinf=1, neginf=1) # revisar si esto es cierto
        alfa_v2=np.exp((-1)*epsilon*s*frec_ang[ww]/Vs) # aqui la parte exponencial para la onda p
        alfa_v3=np.cos(frec_ang[ww]*s/Vs) # aqúi la parte real
        alfa_v4=np.sin(frec_ang[ww]*s/Vs) # aquío la parte imaginaria
        #print(alfa_1,"   ",alfa_2,"   ",alfa_3,"   ",alfa_4)
        
        alfa_v=[]
        for i in range (0,len(x)):
            ki_v=[]
            for w in range (0,len(x)):
                if i==w: # este no necesariamiente es cierto porque no es la matriz alga final, es solo el calculo local de alfa (i,j) que despues deberá multiplicarse por los respectivos angulos de inclinacion coseno y seno
                    alfas_v1=1
                    ki_v.append(alfas_v1)
                elif i!=w:
                    alfas_v1=alfa_v1[i,w]*alfa_v2[i,w]*(alfa_v3[i,w]-alfa_v4[i,w]*(1j))
                    ki_v.append(alfas_v1)
            alfa_v.append(ki_v)
        alfa_v=np.array(alfa_v)
        alfaij_v=np.linalg.inv(alfa_v)
        
        
        xx=np.transpose(x)
        FGR_1=np.dot(alfaij_v,x)
        FGRT=np.dot(np.transpose(FGR_1),xx)
        #print("factor osiriano")
        #print(FGRT)
        Fact_v.append(FGRT)
        
      
        
        """CALCULO DE FACTOR DE GRUPO HORIZONTAL YA TOMA EN CUENTA LOS COSENOS Y SENOS CUADRADOS RESPECTO A LOS OTROS PILOTES"""
        
        alfa_h_f=[]
        for i in range (0,len(x)):
            ki_f=[]
            for w in range (0,len(x)):
                if i==w: # este no necesariamiente es cierto porque no es la matriz alga final, es solo el calculo local de alfa (i,j) que despues deberá multiplicarse por los respectivos angulos de inclinacion coseno y seno
                    alfas_1_f=1
                    ki_f.append(alfas_1_f)
                elif i!=w:
                    alfas_1_f=alfa_h[i,w]*np.cos(beta[i,w])*np.cos(beta[i,w])+alfa_v[i,w]*np.sin(beta[i,w])*np.sin(beta[i,w])
                    ki_f.append(alfas_1_f)
            alfa_h_f.append(ki_f)
        alfa_h_f=np.array(alfa_h_f)
        alfaij=np.linalg.inv(alfa_h_f)
        
        suma_h=np.sum(alfaij) # esta es una forma de hacerlo a traves de numpy
        
        suma = 0
        for i in range (0,len(x)):
            for w in range (0,len(x)):
                suma += alfaij[i][w] # esta es otra forma de hacer la suma a traves del propio python
        #print(suma)
        Fact.append(suma_h)
        #print("nota 1")
        #print(Fact)
        #print("fin de nota 1")
    Fact=np.array(Fact)
    Fact_v=np.array(Fact_v)
    
    Fact_real=np.real(Fact)
    Fact_imag=np.imag(Fact)
    #print(" el factor de grupo es:\n" )
    #print(Fact_v) 
    #print(Fact)
    
    
    
    
    #plt.plot(frec_ang,Fact_real,label="2")# verificado
    #plt.title('Fact')# verificado
    #plt.xlabel('frecuencia angular (w)')# verificado
    #plt.ylabel('')# verificado
    #plt.legend(loc=9,fontsize=7) #-->leyenda, con tamaño y localización
    #plt.show()# verificado
    
    
    #plt.plot(frec_ang,Fact_imag,label="2")# verificado
    #plt.title('Fact')# verificado
    #plt.xlabel('frecuencia angular (w)')# verificado
    #plt.ylabel('')# verificado
    #plt.legend(loc=9,fontsize=7) #-->leyenda, con tamaño y localización
    #plt.show()# verificado
    # return Fact
    return Fact,Fact_v,alfa_v,alfaij, alfa_h_f,x,xx,alfa_v3,alfa_v4,alfaij_v,FGRT
    
#Fact,Fact_v,alfa_v,alfaij, alfa_h_f,x,xx,alfa_v3,alfa_v4,alfaij_v,FGRT =  INTERACT3 (dp,Vs,v,epsilon,x,y,Lysmer)



    # Una vez calculados todos los valores individuales el proceso para volverlo matríz debe pasa por un for
    #para que se multipliquen los iesimos valores de alfa_! por los iesimos valores de afa_2, etc
    #beta_rs=np.reshape(beta,(len(x),len(x)))
    #print(beta_rs)
    #beta_rs=np.nan_to_num(beta_rs, copy=True, nan=2, posinf=2, neginf=2) # excelente para reemplazar los ceros e infinitos por el valor que se requiera
    #a = np.zeros((3, 3),int) #Inicializo una matriz
    #np.fill_diagonal(a,5) # Relleno la diagonal con un valor especifico
    #a
    #print(a)
    #ax=np.array([-1.5,1.5,-1.5,1.5],dtype=complex) # con esto se transforma una matriz en complejos
    #ax=np.arctan(alfa)
    #bx=ax*180/3.1416
    #ar=np.array([1,2,3])
    #ar=np.exp(ar) # funcion para calcular la exponencial
    #print (ar)
    #osito=np.array([[-1.5+4j,1.5+4j],[-1.5+4j,1.5+4j]],dtype=complex)
    #osita=np.array([[1.5+4j,1.5+4j],[-1.5+4j,-1.5+4j]],dtype=complex)
    #print(osito," , " ,osita)
    
