# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 15:47:42 2022

@author: oosiris
"""
import os
from tkinter import filedialog
import datetime

def reporte(hora,G,Hs,v,epsilon,Vs,D,B,L,dp,Ep,Es,Lysmer,x,y,A,R,Rr,w1,n_s,n_p,n_h,n_r,n_v,nhs,Kx_o,kx,
            ch,Kv,kv,cv,Kr,kr,cr,Kh_o,Ch_o,Kv_o,Cv_o,Kr_o,Cr_o,n_p_s,n_p_p,n_p_niu,K_p_h,k_p_h,
            c_p_h,K_p_v,k_p_v,c_p_v,Fact,Fact_v,K_gp_h,K_gp_r,Ktot_h,Ktot_h_real,Ktot_h_imag,Ktot_rot,
            Ktot_rot_real,Ktot_rot_imag,eps_tot_gp_h,eps_tot_gp_r):
    archivo_OAG=filedialog.asksaveasfilename(initialdir = "/",filetypes=[('text file','*.txt')],defaultextension='.txt') # cuadro de dialogo salvar como
    nombre_arch=os.path.basename(archivo_OAG) # obtención de la ruta del archivo guardado
    print(os.path.basename(archivo_OAG))
    
    file=open(archivo_OAG, 'w') 
    file.write("Interact versión 1.0.0, 2022" + os.linesep)
    file.write("Programa para cálculo de interacción suelo-estructura conforme MDOC 2015-CFE" + os.linesep)
    file.write("Creado por Osca Osiris Aguilar G." + os.linesep)
    file.write("correo:moscosir@hotmail.com" + os.linesep)
    file.write("hora: " )
    file.write( "%s\n" % hora.strftime('%d/%m/%Y %H:%M:%S') + os.linesep)
    file.write( "========================DATOS DE ENTRADA================="+ os.linesep)
    
    file.write("Módulo G del suelo (ton/m2):" )
    file.write("%s" % G )
    file.write(" "+ os.linesep)
      
    file.write("Espesor del estrato eq. Hs (m):" )
    file.write("%s" % Hs )
    file.write(" "+ os.linesep)
    
    file.write("Relación de Poisson v  del estrato eq.:" )
    file.write("%s" % v )
    file.write(" adim"+ os.linesep)
    
    file.write("Amortiguamiento:" )
    file.write("%s" % epsilon )
    file.write(" "+ os.linesep)
    
    file.write("Velocidad Vs (m/s):" )
    file.write("%s" % Vs )
    file.write(" "+ os.linesep)
    
    file.write("Profundidad de desplante D de la zapata (m):" )
    file.write("%s" % D )
    file.write(" "+ os.linesep)
    
    file.write("Ancho B de la zapata (m):" )
    file.write("%s" % B )
    file.write(" "+ os.linesep)
    
    file.write("Ancho L de la zapata (m):" )
    file.write("%s" % L )
    file.write(" "+ os.linesep)
    
    file.write("Diametro dp del pilote (m):" )
    file.write("%s" % dp )
    file.write(" "+ os.linesep)
    
    file.write("Módulo Ep del pilote (ton/m2):" )
    file.write("%s" % Ep )
    file.write(" "+ os.linesep)
    
    file.write("Módulo Es del suelo (ton/m2):" )
    file.write("%s" % Es )
    file.write(" "+ os.linesep)
    
    file.write("Velocidad de Lysmer (m/s):" )
    file.write("%s" % Lysmer )
    file.write(" "+ os.linesep)
    
    file.write("Coordenadas X del pilote (m):" )
    file.write("%s" % x + os.linesep)
    file.write("Coordenadas Y del pilote (m):" )
    file.write("%s" % y + os.linesep)
    
    file.write("Area de la zapata (m2):" )
    file.write("%s" % A )
    file.write(" "+ os.linesep)
    
    file.write("Radio de la cimentación circular eq.(m):" )
    file.write("%s" % R )
    file.write(" "+ os.linesep)
    
    file.write("Radio de la cimentación circular eq. en rotación (m):" )
    file.write("%s" % Rr )
    file.write(" "+ os.linesep)
    
    file.write("Radio de la cimentación circular eq. en rotación (m):" )
    file.write("%s" % Rr )
    file.write(" "+ os.linesep)
    
    file.write( "========================PARÁMETROS DE LA FRECUENCIA PARA ZAPATA================="+ os.linesep)
    
    file.write("Frecuencia angular w (omega, abcisas para todas las gráficas):"+ os.linesep )
    for item in w1:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Parámetro de frecuencia ns :" )
    file.write("%s" % n_s )
    file.write(" "+ os.linesep)
    
    file.write("Parámetro de frecuencia np :" )
    file.write("%s" % n_p )
    file.write(" "+ os.linesep)
    
    file.write("Parámetro de frecuencia nh (horizontal):" )
    file.write(" "+ os.linesep)
    for item in n_h:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Parámetro de frecuencia nr (rotacional):" )
    file.write(" "+ os.linesep)
    for item in n_r:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Parámetro de frecuencia nh (vertical):" )
    file.write(" "+ os.linesep)
    for item in n_v:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Parámetro de frecuencia nhs:" )
    file.write(" "+ os.linesep)
    for item in nhs:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)


    file.write( "========================FUNCIONES DE IMPEDANCIA DE LA ZAPATA================="+ os.linesep)
    file.write("Rigidez estática horizontal Kh:" )
    file.write("%s" % Kx_o )
    file.write("ton/m "+ os.linesep)
    
    file.write("Coeficiente de rigidez horizontal kh:" )
    file.write("%s" % kx )
    file.write(" "+ os.linesep)
    
    file.write("Coeficiente de amortiguamiento horizontal ch:"+ os.linesep )
    for item in ch:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
        
    file.write("Rigidez estática Vertical Kv:" )
    file.write("%s" % Kv )
    file.write("ton/m "+ os.linesep)
    
    file.write("Coeficiente de rigidez vertical kv:" )
    file.write("%s" % kv )
    file.write(" "+ os.linesep)
    
    file.write("Coeficiente de amortiguamiento vertical cv:" + os.linesep)
    for item in cv:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Rigidez estática rotacional Kr:" )
    file.write("%s" % Kr )
    file.write("ton/m "+ os.linesep)
           
    file.write("Coeficiente de rigidez rotacional kr:" + os.linesep)
    for item in kr:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Coeficiente de amortiguamiento rotacional cr:" + os.linesep)
    for item in cr:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)

    file.write( "========================RIGIDECES Y AMORTIGUAMIENTOS DE ZAPATA==================="+ os.linesep)
   
    file.write("Rigidez dinámica horizontal Kh_o zapata:" + os.linesep)
    for item in Kh_o:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
        
    file.write("Amortiguamiento horizontal Ch_o zapata: " + os.linesep)
    for item in Ch_o:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Rigidez dinámica vertical Kv_o zapata:" + os.linesep)
    for item in Kv_o:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
        
    file.write("Amortiguamiento horizontal Cv_o zapata:" + os.linesep)
    for item in Cv_o:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Rigidez dinámica rotacional Kr_o zapata:" + os.linesep)
    for item in Kr_o:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
        
    file.write("Amortiguamiento rotacional Cr_o zapata:" + os.linesep)
    for item in Cr_o:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    
    file.write( "========================PARÁMETROS DE LA FRECUENCIA PILOTES==================="+ os.linesep)
    file.write("Parámetro de la frecuencia ns pilote:" )
    file.write("%s" % n_p_s )
    file.write("   "+ os.linesep)
    
    file.write("Parámetro de la frecuencia np pilote:" )
    file.write("%s" % n_p_p )
    file.write("  "+ os.linesep)

    file.write("Parámetro de la frecuencia n=w*dp/Vs pilote:" + os.linesep)
    for item in n_p_niu:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    
    file.write( "========================FUNCIONES DE IMPEDANCIA DE PILOTE================="+ os.linesep)
    file.write("Rigidez estática horizontal pilote Kh:" )
    file.write("%s" % K_p_h )
    file.write(" ton/m "+ os.linesep)
    
    file.write("Coeficiente de rigidez horizontal pilote kh:" )
    file.write("%s" % k_p_h )
    file.write("  "+ os.linesep)
    
    file.write("Coeficiente de amortiguamiento horizontal pilote ch:" + os.linesep )
    for item in c_p_h:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Rigidez estática vertical pilote Kv:" )
    file.write("%s" % K_p_v )
    file.write(" ton/m "+ os.linesep)
    
    file.write("Coeficiente de rigidez vertical pilote kv:" + os.linesep )
    for item in k_p_v:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Coeficiente de amortiguamiento vertical pilote cv:" + os.linesep )
    for item in c_p_v:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write( "========================FACTORES DE GRUPO PILOTES================="+ os.linesep)

    file.write("Factor de grupo de pilotes horizontales:" + os.linesep )
    for item in Fact:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Factor de grupo de pilotes rotacional:" + os.linesep )
    for item in Fact_v:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write( "========================RIGIDECES Y AMORTIGUAMIENTOS DE GRUPO DE PILOTES==================="+ os.linesep)

    
    file.write("Rigidez final del grupo de pilotes horizontal:" + os.linesep )
    for item in K_gp_h:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Rigidez final del grupo de pilotes rotacional:" + os.linesep )
    for item in K_gp_r:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write( "========================RIGIDECES Y AMORTIGUAMIENTOS DEL CONJUNTO ZAPATA+PILOTES==================="+ os.linesep)
    file.write("Rigidez final horizontal del sistema zapata+pilotes:" + os.linesep )
    for item in Ktot_h:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Rigidez final horizontal del sistema zapata+pilotes (SOLO LA PARTE REAL):" + os.linesep )
    for item in Ktot_h_real:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Rigidez final horizontal del sistema zapata+pilotes (SOLO LA PARTE COMPLEJA DE AMORTIGUAMIENTO):" + os.linesep )
    for item in Ktot_h_imag:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Rigidez final rotacional del sistema zapata+pilotes:" + os.linesep )
    for item in Ktot_rot:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Rigidez final rotacional del sistema zapata+pilotes (SOLO LA PARTE REAL):" + os.linesep )
    for item in Ktot_rot_real:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Rigidez final rotacional del sistema zapata+pilotes (SOLO LA PARTE COMPLEJA DE AMORTIGUAMIENTO):" + os.linesep )
    for item in Ktot_rot_imag:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write( "=======================AMORTIGUAMIENTO DEL SISTEMA ZAPATA-PILOTES==================="+ os.linesep)
    
    file.write("Amortiguamiento del sistema horizontal epsilon_h =C*w/(2*Kh):" + os.linesep )
    for item in eps_tot_gp_h:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)
    
    file.write("Amortiguamiento del sistema rotacional epsilon_h =C*w/(2*Kr):" + os.linesep )
    for item in eps_tot_gp_r:
        file.write("          %s\n" % item )
    file.write(" "+ os.linesep)

    
    file.write("                                        FIN DEL REPORTE"+ os.linesep)
    
    hora_fin=datetime.datetime.now()
    file.write( "                                        %s\n" % hora_fin.strftime('%d/%m/%Y %H:%M:%S') + os.linesep)
    file.write("Interact versión 1.0.0, 2022" + os.linesep)
    file.write("Programa para cálculo de interacción suelo-estructura conforme MDOC 2015-CFE" + os.linesep)
    file.write("Creado por Osca Osiris Aguilar G." + os.linesep)
    file.write("Correo:moscosir@hotmail.com" + os.linesep)
    file.close()
    
    return hora,G,Hs,v,epsilon,Vs,D,B,L,dp,Ep,Es,Lysmer,x,y,A,R,Rr,w1,n_s,n_p,n_h,n_r,n_v,nhs,Kx_o,kx,ch,Kv,kv,cv,Kr,kr,cr,Kh_o,Ch_o,Kv_o,Cv_o,Kr_o,Cr_o,n_p_s,n_p_p,n_p_niu,K_p_h,k_p_h,c_p_h,K_p_v,k_p_v,c_p_v,Fact,Fact_v,K_gp_h,K_gp_r,Ktot_h,Ktot_h_real,Ktot_h_imag,Ktot_rot,Ktot_rot_real,Ktot_rot_imag,eps_tot_gp_h,eps_tot_gp_r

    