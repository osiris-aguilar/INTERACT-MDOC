# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 20:36:40 2021
CALCULO DE LAS FUNCIONES DE IMPEDANCIOA
@author: oosiris
"""
import numpy as np
import matplotlib.pyplot as plt
import math as math
import os
#-----------------VARIUABLES DE ZAPATA
#G=1750 #modulo de suelo --> variable a introducir
#B=5  # dimension del cimiento  --> variable a intorucir
#L=5  # dimension del cimiento  --> variable a intorucir
#Hs=22 #espesor del estrato equivalente  --> lo calcula una parte del programa pero para esta fase se deberá introducir como un dato -->variable a introducir
#v=0.311 # relacion ed poison, debe obtenerse el niu promedio ponderado por estrato, aqui solo lo estoy colocando como un solo valor pero debe provenir del promedio ponderado de los nius de los estratos
#D=1 # produndidad de enterramiento de la cimentación --> variable a introducir
#epsilon=.02 # variable a introducir
#Vs =234 #4*Hs/Ts # velocidad del estrato equivalente --> debe ser una variable de entrada

#-----------------VARIABLES DE PILOTES

#dp=1  #  --->variable a introducir
#Ep=2598076  # modulo de elasticidad del pilote ,es una variable a introducir 
#Es=4600  # modulo de elasticidad del deposito de suelo (¿del estrato en cuestion o del estrao equivalente promediado?)
#Lp=16 # este punto lo tengo que arreglar, además esta es una variable que debe salir cuando la convierta en una función

def interact2(G,B,L,Hs,v,D,epsilon,Vs,dp,Ep,Es,Lp):

    #------------------CALCULOS PRELIMINARES---------------
    A=B*L 
    Ixx=B*L**3/12
    Iyy=L*B**3/12
    R =(A/3.1416)**0.5 #radio equivalente
    Rr=(4*(B*L**3/12)/3.1416)**0.25 #esta valor tiene orientación poc lo que cambia cuando vaya para el otro sentido ya sea "x" o "y"
    
    """ CALCULO DE LOS PARAMETROS DE LA FRECUENCIA"""
    
    n_s=3.1416*R/(2*Hs)  # verificado  (1)
    n_p=(3.1416*Rr/(2*Hs))*((2*(1-v)/(1-2*v)))**0.5 # verificado (2)
    
#===================================================================ZAPATAS============================================================   
    """CALCULO DE LA RIGIDEZ ESTATICA DE UNA ZAPATA"""
    """HORIZONTAL"""
    Kx_o=(8*G*R)/(2-v)*(1+(R/(2*Hs)))*(1+(2*D)/(3*R))*(1+(5*D/(4*Hs))) # verificado (3)
    kx=1 # verificado  (4)
    
    """ VERTICAL"""
    Kv=(4*G*R/(1-v))*(1+1.28*(R/Hs))*(1+(D/(2*R)))*(1+(0.85-0.28*(D/R))*((D/Hs)/(1-(D/Hs))))# verificado (5)
    kv=1 # verificado (6)
    
    """ CABECEO"""
    Kr=(8*G*Rr**3)/(3*(1-v))*(1+(Rr/(6*Hs)))*(1+(2*D/Rr))*(1+(0.71*(D/Hs)))  # verificado (7)
    
    """ ejercicio para almacenar los resultados de un ciclo for un un array"""
    
    n_h=[] # verificado
    n_r=[] # verificado
    n_v=[]# verificado
    
    w1=[]# verificado
    for w in range(0,100,1):
        n_h_1=w*R/Vs # verificado
        n_v_1=w*R/Vs # verificado
        n_r_1=w*Rr/Vs # verificado
        n_h.append(n_h_1) # verificado
        n_v.append(n_v_1) # verificado
        n_r.append(n_r_1)# verificado
        w1.append(w) # verificado
    n_h=np.array(n_h) # verificado (8)
    n_v=np.array(n_h) # verificado (9)
    n_r=np.array(n_r) # verificado (10)
    w1=np.array(w1) # verificado 
    
    nhs=n_h/n_s # verificado (11)
    ch=[] # verificado
    for w in range (0,100,1): # verificado
        if nhs[w] <=1:# verificado
            ch1=0.65*epsilon*nhs[w]/(1-(1-2*epsilon)*nhs[w]**2)# verificado
            ch.append(ch1)# verificado
        elif nhs[w] >1:# verificado
            ch1=0.576# verificado
            ch.append(ch1)# verificado
    ch=np.array(ch) # verificado (12)
    
    #plt.plot(w1,ch,label="Ch")
    #plt.title('ch')
    #plt.xlabel('frecuencia angular (w)')
    #plt.ylabel('c h')
    #plt.legend(loc=9,fontsize=7) #-->leyenda, con tamaño y localización
    #plt.show()
    
    cv=[]# verificado
    for w in range (0,100,1):# verificado
        if n_v[w] < n_p:# verificado
            cv1=0# verificado
            cv.append(cv1)# verificado
        elif n_v[w] > n_p:# verificado
            cv1=(0.85*(1+1.85*(1-v)*D/R))/(1+0.5*(D/R))# verificado
            cv.append(cv1)# verificado
    cv=np.array(cv)# verificado (13)
    
    #plt.plot(w1,cv,label="Cv")# verificado
    #plt.title('cv')# verificado
    #plt.xlabel('frecuencia angular (w)')# verificado
    #plt.ylabel('c v')# verificado
    #plt.legend(loc=9,fontsize=7) #-->leyenda, con tamaño y localización
    #plt.show()# verificado
    
    kr=[]# verificado
    for w in range (0,100,1):# verificado
        if n_r[w] <= 2.5:# verificado
            kr1=1-0.2*n_r[w]# verificado
            kr.append(kr1)# verificado
        elif n_r[w] > 2.5 and v<=(1/3):# verificado
            kr1=0.5# verificado
            kr.append(kr1)# verificado
        elif n_r[w] > 2.5 and v>=(0.45):
            kr1=1-0.2*n_r[w]# verificado
            kr.append(kr1)# verificado# verificado
        elif n_r[w] > 2.5 and (1/3)<v<(0.45):
            kr1=((1-0.2*n_r[w]-0.5)/(n_r[w]-2.5))*(n_r[w]-2.5)+0.5
            kr.append(kr1)
    kr=np.array(kr) # (14)
        
    #plt.plot(w1,kr,label="kr")# verificado
    #plt.title('kr')# verificado
    #plt.xlabel('frecuencia angular (w)')# verificado
    #plt.ylabel('k r')# verificado
    #plt.legend(loc=9,fontsize=7) #-->leyenda, con tamaño y localización
    #plt.show()# verificado
    
    nrp=n_r/n_p  # (15)
    
    cr=[]
    for w in range (0,100,1):# verificado
        if nrp[w] <= 1:# verificado
            cr1=0.5*epsilon*nrp[w]/(1-(1-2*epsilon)*nrp[w]**2)# verificado
            cr.append(cr1)# verificado
        elif nrp[w] > 1:# verificado
            cr1=0.3*n_r[w]**2/(1+n_r[w]**2)# verificado
            cr.append(cr1)# verificado
    
    cr=np.array(cr)# verificado (16)
    
    #plt.plot(w1,cr,label="cr")# verificado
    #plt.title('cr')# verificado
    #plt.xlabel('frecuencia angular (w)')# verificado
    #plt.ylabel('c r')# verificado
    #plt.legend(loc=9,fontsize=7) #-->leyenda, con tamaño y localización
    #plt.show()# verificado
    
    #=========RIGIDEZ Y AMORTIUAMIENTO FINAL HORIZONTAL==================
    Kh_o=Kx_o*(kx-2*epsilon*n_h*ch) # (17)
    #plt.plot(w1,Kh_o,label="Kh")
    #plt.title('Kh')
    #plt.xlabel('frecuencia angular (w)')
    #plt.ylabel('K h')
    #plt.legend(loc=9,fontsize=7) 
    #plt.show()
    
    Ch_o=Kx_o*(n_h*ch+2*epsilon*kx)/w1 #(18)
    #plt.plot(w1,Ch_o,label="Ch")
    #plt.title('Ch')
    #plt.xlabel('frecuencia angular (w)')
    #plt.ylabel('C h')
    #plt.legend(loc=9,fontsize=7) 
    #plt.show()
    
    #=========RIGIDEZ Y AMORTIUAMIENTO FINAL VERTICAL==================
    
    Kv_o=Kv*(kv-2*epsilon*n_v*cv) # (19)
    #plt.plot(w1,Kv_o,label="Kv")
    #plt.title('Kv')
    #plt.xlabel('frecuencia angular (w)')
    #plt.ylabel('K v')
    #plt.legend(loc=9,fontsize=7) 
    #plt.show()
    
    Cv_o=Kv*(n_v*cv+2*epsilon*kv)/w1 #(20)
    #plt.plot(w1,Cv_o,label="Cv")
    #plt.title('Cv')
    #plt.xlabel('frecuencia angular (w)')
    #plt.ylabel('C v')
    #plt.legend(loc=9,fontsize=7) 
    #plt.show()
    
    #=========RIGIDEZ Y AMORTIUAMIENTO FINAL ROTACIONAL==================
    Kr_o=Kr*(kr-2*epsilon*n_r*cr) # (21)
    #plt.plot(w1,Kr_o,label="Kr")
    #plt.title('Kr')
    #plt.xlabel('frecuencia angular (w)')
    #plt.ylabel('K r')
    #plt.legend(loc=9,fontsize=7) 
    #plt.show()
    
    Cr_o=Kr*(n_r*cr+2*epsilon*kr)/w1 # (22)
    #plt.plot(w1,Cr_o,label="Cr")
    #plt.title('Cr')
    #plt.xlabel('frecuencia angular (w)')
    #plt.ylabel('C r')
    #plt.legend(loc=9,fontsize=7) 
    #plt.show()
    
# ================================================IMPEDANCIAS ZAPATAS============================================
    K_z_h_compx=Kh_o+Ch_o*w1*1J
    K_z_v_compx=Kv_o+Cv_o*w1*1J
    K_z_r_compx=Kr_o+Cr_o*w1*1J
        
    #---------------------------------------------------------------- FIN DE LA PARTE DE ZAPATAS----------------
    
    #------------------------------------ INICIO DE LA PARTE DE PILOTES-----------------------
    
    n_p_s=3.1416*dp/(2*Hs)  # (23)
    n_p_p=3.4*n_p_s/(3.1416*(1-v)) # (24)
    
    n_p_niu=[] 
    for w in range(0,100,1):
        n_p_p1=w*dp/Vs
        n_p_niu.append(n_p_p1) 
    n_p_niu=np.array(n_p_niu)  # (25)
    
    """ funciones de impedancia"""
    
    """ horizontal"""
    
    K_p_h=dp*Es*(Ep/Es)**(.21) # (26)
    k_p_h=1 #(27)
    
    c_p_h=[]
    for w in range (0,100,1):
        if n_p_niu[w] <= n_p_s:
            c_ph_1=0.8*epsilon
            c_p_h.append(c_ph_1)
        elif n_p_niu[w] > n_p_s:
            c_ph_1=0.8*epsilon+0.175*n_p_niu[w]*(Ep/Es)**(0.17)
            c_p_h.append(c_ph_1)
    c_p_h=np.array(c_p_h) # (28)
    
    #plt.plot(w1,c_p_h,label="cph")
    #plt.title('CPH')
    #plt.xlabel('frecuencia angular (w)')
    #plt.ylabel('C p H')
    #plt.legend(loc=9,fontsize=7) 
    #plt.show()
    
    K_p_v=1.9*dp*Es*(Lp/dp)**.67 # (29)
    k_p_v=[]
    for w in range (0,100,1):
        if (Lp/dp)<15:
            k_p_v1=1
            k_p_v.append(k_p_v1)
        elif (Lp/dp)>=50:
            k_p_v1=1+n_p_niu[w]**.5
            k_p_v.append(k_p_v1)
        elif 15<=(Lp/dp)<50: #  temporalmente estoy promediando
            m=(((1+n_p_niu[w]**.5)-1)/(50-15))    #===================AQUI LA INTERPOLACION CORRECTAMENTE HECHA
            k_p_v1=(((Lp/dp)-15)*m)+1
            k_p_v.append(k_p_v1)
    k_p_v=np.array(k_p_v) #(30)
    
    #plt.plot(w1,k_p_v,label="KPV")
    #plt.title('KPV')
    #plt.xlabel('frecuencia angular (w)')
    #plt.ylabel('K p v')
    #plt.legend(loc=9,fontsize=7) 
    #plt.show()
    
    c_p_v=[]
    for w in range (0,100,1):
        if n_p_niu[w] <= n_p_p:
            c_pv_1=epsilon
            c_p_v.append(c_pv_1)
        elif n_p_niu[w] > 1.5*n_p_p:
            c_pv_1=(0.413/(1+v))*(Lp/dp)**(0.33)*(1-math.exp(-(Ep/Es)*(Lp/dp)**(-2)))*n_p_niu[w]**0.8
            c_p_v.append(c_pv_1)
        elif n_p_niu[w] > n_p_p<n_p_niu[w]<=1.5*n_p_p: # temporalmente estoy promediando
            m2=((((0.413/(1+v))*(Lp/dp)**(0.33)*(1-math.exp(-(Ep/Es)*(Lp/dp)**(-2)))*n_p_niu[w]**0.8)-epsilon)/(1.5*n_p_p-n_p_p))
            c_pv_1=(n_p_niu[w]-n_p_p)*m2+epsilon
            c_p_v.append(c_pv_1)
    c_p_v=np.array(c_p_v) #(31)
    
    #plt.plot(w1,c_p_v,label="cpv")
    #plt.title('Cv')
    #plt.xlabel('frecuencia angular (w)')
    #plt.ylabel('Cp v')
    #plt.legend(loc=9,fontsize=7) 
    #plt.show()
# ================================================IMPEDANCIAS PILOTES============================================
#--------------------------------------------------horizontales -----------------------------------------
    K_p_m_h=K_p_h*k_p_h
    C_p_m_h=2*K_p_h*c_p_h/w1
    
    K_fg_h_compx=K_p_m_h+C_p_m_h*w1*1j
    
#--------------------------------------------------verticales -------------------------------------------
    
    K_p_m_v=K_p_v*k_p_v
    C_p_m_v=2*K_p_v*c_p_v/w1
   
    K_fg_v_compx=K_p_m_v+C_p_m_v*w1*1j    
    

# -------------------------------------------------rotacionales------------------------------------------
    

#==============================reservado=============================


#=================================================REPORTE================================================
    # codigo para poder enviar a un archivo de texto
  #  file=open('reporte.txt', 'w') 
  #  file.write("Primera línea" + os.linesep)
  #  file.write("Segunda línea" + os.linesep)
  #  for item in K_p_m_v:
  #      file.write("%s\n" % item )
    
  #  file.write(" " + os.linesep)
  #  file.write(" " + os.linesep)
  #  file.write(" " + os.linesep)
   # 
   ## for item in C_p_m_v:
     #   file.write("%s\n" % item)
   # file.close()    
    
    
    return A,R,Rr,n_s, n_p, w1, Kx_o, kx, Kv, kv , Kr,n_h,n_v, n_r, nhs, ch, cv, kr, nrp, cr, Kh_o, Ch_o, Kv_o, Cv_o, Kr_o, Cr_o,K_z_h_compx,K_z_v_compx,K_z_r_compx,n_p_s, n_p_p, n_p_niu, K_p_h, k_p_h,c_p_h, K_p_v, k_p_v,c_p_v, w1,K_p_m_h,C_p_m_h,K_p_m_v,C_p_m_v, G,K_fg_h_compx,K_fg_v_compx


#n_s, n_p, Kx_o, kx, Kv, kv , Kr,n_h,n_v, n_r, nhs, ch, cv, kr, nrp, cr, Kh_o, Ch_o, Kv_o, Cv_o, Kr_o, Cr_o,K_z_h_compx,K_z_v_compx,K_z_r_compx,K_p_v, w1,K_p_m_h,C_p_m_h,K_p_m_v,C_p_m_v, G,K_fg_h_compx,K_fg_v_compx =interact2(G,B,L,Hs,v,D,epsilon,Vs,dp,Ep,Es,Lp)







 #codigo para poder enviar a un archivo de texto
#file=open('abc.txt', 'w') 
#file.write("Primera línea" + os.linesep)
#file.write("Segunda línea" + os.linesep)
#for item in K_p_m_v:
#    file.write("%s\n" % item)
#for item in C_p_m_v:
#    file.write("%s\n" % item)
#file.close()