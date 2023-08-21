# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:26:49 2021

@author: oosiris
"""
"""número de estratos"""

import numpy as np


def interact(gamma,d_G,Hs):
    x0=[]
    sum_d_G=0
    for i in range(0,len(gamma-1),1):
        sum_d_G+=d_G[(i)]
        x0.append(sum_d_G)
    x1=np.array(x0)
    x=x1/sum_d_G 
    
    xxx=[]
    for n in range (0,len(gamma-1),1):
        if n==0:
            parentesis=x[(0)]**2
            xxx.append(parentesis)
        elif n>0:
            parentesis=x[(n)]**2+x[(n)]*x[(n-1)]+x[(n-1)]**2
            xxx.append(parentesis)
    xxx2=np.array(xxx)    
    Mult_vec=gamma*Hs*xxx2
    sum_gamm_hi=0
    
    for m in range(0,len(gamma-1),1):
        sum_gamm_hi+=Mult_vec[(m)]
    
    """SOLO FALTA OBTENER DIRECTAMENTE EL PERIODO, YA ESTÁ LA MESA SERVIDA""" 
    """ sum_d_G, sum_gamm_hi"""
    Ts=4/((9.81)**(.5))*(sum_gamm_hi*sum_d_G)**(0.5)
    """ peridodo estructural """
    
    Te = 2 
    Hss = 30
    He= 25
    Val=Te*Hss/(Ts*He)

    if Val >2.5:
        print("No es necesario considerar los efectos de interacción")
    elif Val <2.5:
        print("Es necesario considerar los efectos de interacción")
        
    
