# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 11:11:07 2021
@author: oosiris
"""
import os
import datetime
from interaccion_r4 import interact 
from funciones_de_impedancia_r7 import interact2
from fac_grupo_pilotes_r2 import INTERACT3
from Reporte import reporte


from tkinter import *
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
#-----------------------------------------------------------------ventana principal------------------------------------------
raiz =tk.Tk()
raiz.title("Interact")
fondo = tk.Frame(raiz, width=900, height=600)
fondo.grid(columnspan=1, rowspan=1)
raiz.iconbitmap("logoico1.ico")


#_------------------------------------------------------------------logo-----------------------------------------------------
logo = Image.open(r'logo.jpg')
logo = logo.resize((650, 420), Image.ANTIALIAS) # Redimension (Alto, Ancho)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.place(x=100, y=150)

#-------------------------------------------------------FUNCION DE CALCULO DE PERIODO DEL SUELO------------------------------
def velocidad_vs():
    archivo_vs = filedialog.askopenfilename(title="abrir", initialdir="C:/HP/Dropbox/PYTHON",filetypes=(("Archivos de texto","*.txt"),("todos los archivos","*,*"))) # abrir el archivo
    #print(archivo_vs)
    nombre_archivo_vs=os.path.basename(archivo_vs) # obtener la ruta del archivo para asignarlo como variable
    #print(nombre_archivo_vs)
    matriz=np.loadtxt(archivo_vs, skiprows=1,usecols=(0,1,2,3)) # una vez conocido el archivo, numpy extrae sus datos de la matriz
    #print(matriz)
    gamma=matriz[:,0]   # OBTENCION DE LA COLUMNA GAMMA
    niu_=matriz[:,1]    # OBTENCION DE LA COLUMNA NIU
    Hs=matriz[:,2]      # OBTENCION DE LA COLUMNA HS
    Vs=matriz[:,3]      # OBTENCION DE LA COLUMNA VS
    hamahs=gamma*Hs
    G=(gamma/9.81)*Vs**2
    #--------------------------------------------------------ABRIR VENTANA SECUNDARIA-----------------------------------------
    v_s_2=tk.Toplevel(raiz,width=1000, height=900)  # SE ASIGNA A LA VENTANA RAIZ
    v_s_2.title("RESULTADOS")   #TITULO
    #---------------APLICAR LA FUNCION Y OBTENER LOS VALORES DE RETURN DE LA FUNCION DEL ARCHIVO VINCULADO
    Ts_1, Val_1, Vs_formula_1, prof_1, Vs_prom_1, Lent_prom_1 = interact(gamma,G,Hs,Vs) # obtengo los resultados de la función y los integro a mi programa asignandolo a una variable
    #print(Ts_1 , Val_1, Vs_formula_1,prof_1,Vs_prom_1, Lent_prom_1)
    # -----------------------------------------------------------PREPARAR LA GRAFICA------------------------------------------
    fig = Figure(figsize=(10,3), dpi=100)
    fig.add_subplot(111).plot(prof_1,Vs, Label="line1")
    fig2 =Figure(figsize=(10,3), dpi=100)
    fig2.add_subplot(111).plot((min(prof_1),max(prof_1)),(Vs_prom_1,Vs_prom_1))
    #--------------------------------------------------PREPARAR EL LIENZO DE PRESENTACION-------------------------------------
    canvas =FigureCanvasTkAgg(fig,master=v_s_2)
    canvas2 =FigureCanvasTkAgg(fig2,master=v_s_2)
    canvas.draw()
    canvas2.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH )
    canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH )
    #-------------------------------------ESTABLECER LA BARRA DE ERRAMIENTAS EN LA GRAFICA------------------------------------
    toolbar=NavigationToolbar2Tk(canvas, v_s_2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
    #-----------REDONDEAR VALORES PARA QUE NO APAREZCAN TANTOS DIGITOS DESPUES DEL CERO---------------------------------------
    Vs_formula_1=round(Vs_formula_1,2) # si no se redondea primero el valor no aparece en la etiqueta, 
    Ts_1=round(Ts_1,2) # si no se redondea primero el valor no aparece en la etiqueta, 
    Vs_prom_1=round(Vs_prom_1,2)
    Lent_prom_1=round(Lent_prom_1,2)
    #----------------------------------------MOSTRAR RESULTADOS EN ETIQUETAS Y LA GRAFICA-------------------------------------
    milabel_2=tk.Label(v_s_2, text=("Vs=H4/Ts=",Vs_formula_1,"m/s",",Ts=",Ts_1,"s,"),font=("Candara",15))
    milabel_2.place(x=330, y=0)
    milabel_3=tk.Label(v_s_2, text=("Velocidad_prom_Vs=",Vs_prom_1,"m/s"),font=("Candara",15))
    milabel_3.place(x=330, y=285)
    milabel_4=tk.Label(v_s_2, text=("Lentitud_prom_Vs2=", Lent_prom_1,"m/s"),font=("Candara",15))
    milabel_4.place(x=330, y=310)
    # -------------------------------------------COLOCAR LA FUNCION DE CERRAR-------------------------------------------------
    boton_cerrar=tk.Button(v_s_2, text="cerrar ventana", command=v_s_2.destroy)
    boton_cerrar.location(x=600,y=700)
    boton_cerrar.pack()
#-------------------------------------------------------FUNCION DE CALCULO DE IMPEDANCIAS------------------------------
def impedancias():
    hora=datetime.datetime.now()

    archivo_imped = filedialog.askopenfilename(title="abrir", initialdir="C:/HP/Dropbox/PYTHON",filetypes=(("Archivos de texto","*.txt"),("todos los archivos","*,*"))) # abrir el archivo
    #print(archivo_imped)
    nombre_archivo_vs=os.path.basename(archivo_imped) # obtener la ruta del archivo para asignarlo como variable
    #print(nombre_archivo_vs)
    matriz=np.loadtxt(archivo_imped, skiprows=1,usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13)) # una vez conocido el archivo, numpy extrae sus datos de la matriz
    #print(matriz)
    G=matriz[0,0]   # OBTENCION DE LA COLUMNA GAMMA
    B=matriz[0,1]    # OBTENCION DE LA COLUMNA NIU
    L=matriz[0,2]      # OBTENCION DE LA COLUMNA HS
    Hs=matriz[0,3]      # OBTENCION DE LA COLUMNA VS
    v=matriz[0,4]
    D=matriz[0,5]
    epsilon=matriz[0,6]
    Vs=matriz[0,7]
    dp=matriz[0,8]
    Ep=matriz[0,9]
    Es=matriz[0,10]
    Lp=matriz[0,11]
    x=matriz[:,12]
    y=matriz[:,13]
    Lysmer=3.4*Vs/(np.pi*(1-v))

        #---------------APLICAR LA FUNCION Y OBTENER LOS VALORES DE RETURN DE LA FUNCION DEL ARCHIVO VINCULADO
    
    A,R,Rr,n_s, n_p, w1, Kx_o, kx, Kv, kv , Kr,n_h,n_v, n_r, nhs, ch, cv, kr, nrp, cr, Kh_o, Ch_o, Kv_o, Cv_o, Kr_o, Cr_o,K_z_h_compx,K_z_v_compx,K_z_r_compx, n_p_s, n_p_p, n_p_niu, K_p_h, k_p_h,c_p_h, K_p_v, k_p_v,c_p_v, w1,K_p_m_h,C_p_m_h,K_p_m_v,C_p_m_v, G,K_fg_h_compx,K_fg_v_compx =interact2(G,B,L,Hs,v,D,epsilon,Vs,dp,Ep,Es,Lp)

    #---------------APLICAR LA FUNCION PARA CALCULO DE FACTORES DE GRUPO Y OBTENER LOS VALORES DE RETURN DE LA FUNCION DEL ARCHIVO VINCULADO
         
    Fact,Fact_v,alfa_v,alfaij, alfa_h_f,x,xx,alfa_v3,alfa_v4,alfaij_v,FGRT =  INTERACT3 (dp,Vs,v,epsilon,x,y,Lysmer)
    #print(" el factor de grupo horizontal es:")
    #print(Fact)
    #print(" el factor de grupo rotacional es:")
    #print(Fact_v)
    
    # ===================================================================RIGIDEZ DEL CONJUNTO ZAPATA + PILOTES========================================================
    #---------------------------------------------------------------------horizontal----------------------------------------------------------------------------------
    
    K_gp_h=K_fg_h_compx*Fact # IMPEDANCIA DE PILOTE X FACTOR DE GRUPO DE PILOTE, ES DECIR ESTE ES LA IMPEDANCIA FINAL DEL CONJUNTO
    #print("la impedancia del grupo de pilotes es")
    #print(K_gp_h)
    
    Ktot_h=K_gp_h+K_z_h_compx   # IMPEDANCIA DEL CONJUNTO ZAPATA + PILOTES HORIZONTAL
    #print( "oscar osiris es:")
    #print(Ktot_h)
    Ktot_h_real=np.real(Ktot_h)
    Ktot_h_imag=np.imag(Ktot_h)
    eps_tot_gp_h=Ktot_h_imag/(2*Ktot_h_real)
    
    #---------------------------------------------------------------------ROTACIONAL----------------------------------------------------------------------------------
    
    #print( "factor impedancia vertical:")
    #print(K_p_v)
    
    #print( "factor impedancia vertical:")
    #print(K_fg_v_compx)
    
    K_gp_r=K_fg_v_compx*Fact_v # IMPEDANCIA DE PILOTE X FACTOR DE GRUPO DE PILOTE, ES DECIR ESTE ES LA IMPEDANCIA FINAL DEL CONJUNTO
    #print( "factor de grupo rotacinal:")
    #print(K_gp_r)
    #print( "factor de grupo rotacinal zapata:")
    #print(K_z_r_compx)
    
    
    Ktot_rot=K_gp_r+K_z_r_compx   # IMPEDANCIA DEL CONJUNTO ZAPATA + PILOTES HORIZONTAL
    #print( "el factor de impedamcia rotacional total es:")
    #print(Ktot_rot)
    Ktot_rot_real=np.real(Ktot_rot)
    Ktot_rot_imag=np.imag(Ktot_rot)
    eps_tot_gp_r=Ktot_rot_imag/(2*Ktot_rot_real)
    #print(Ktot_rot_real,Ktot_rot_imag)
    
    
    #--------------------------------------------------------ABRIR VENTANA SECUNDARIA-----------------------------------------
    imped_k_o=tk.Toplevel(raiz,width=1000, height=900)  # SE ASIGNA A LA VENTANA RAIZ
    imped_k_o.title("IMPEDANCIA ESTATICA Y AMORTIGUAMIENTO HORIZONTALES ZAPATA")   #TITULO
    imped_k_o.iconbitmap("logoico1.ico")
    
    imped_k_v=tk.Toplevel(raiz,width=1000, height=900)  # SE ASIGNA A LA VENTANA RAIZ
    imped_k_v.title("IMPEDANCIA ESTATICA Y AMORTIGUAMIENTO VERTICALES ZAPATA")   #TITULO
    imped_k_v.iconbitmap("logoico1.ico")
    
    imped_k_r=tk.Toplevel(raiz,width=1000, height=900)  # SE ASIGNA A LA VENTANA RAIZ
    imped_k_r.title("IMPEDANCIA ESTATICA Y AMORTIGUAMIENTO ROTACIONALES ZAPATA")   #TITULO
    imped_k_r.iconbitmap("logoico1.ico")
    
    p_pilote=tk.Toplevel(raiz,width=1000, height=900)  # SE ASIGNA A LA VENTANA RAIZ
    p_pilote.title("POSICION DE PILOTES")   #POSICION DE PILOTES
    p_pilote.iconbitmap("logoico1.ico")
    
    imped_k_h_p=tk.Toplevel(raiz,width=1000, height=900)  # SE ASIGNA A LA VENTANA RAIZ
    imped_k_h_p.title("IMPEDANCIA ESTATICA Y AMORTIGUAMIENTO PILOTE INDIVIDUAL HORIZONTAL")   
    imped_k_h_p.iconbitmap("logoico1.ico")
    
    imped_k_v_p=tk.Toplevel(raiz,width=1000, height=900)  # SE ASIGNA A LA VENTANA RAIZ
    imped_k_v_p.title("IMPEDANCIA ESTATICA Y AMORTIGUAMIENTO PILOTE INDIVIDUAL VERTICAL")   
    imped_k_v_p.iconbitmap("logoico1.ico")
    
    #imped_k_r_p=tk.Toplevel(raiz,width=1000, height=900)  # SE ASIGNA A LA VENTANA RAIZ
    #imped_k_r_p.title("IMPEDANCIA ESTATICA Y AMORTIGUAMIENTO PILOTE INDIVIDUAL ROTACIONAL")   
   
    
    # ===================================================================PREPARAR LA GRAFICAS========================================================
    fig_Khor = Figure(figsize=(10,3), dpi=100)
    fig_Khor.add_subplot(title="K_h_zapata").plot(w1,Kh_o)
    fig_Khor.legend('w',loc=8)    # -----------------grafica K horizontal
    
    fig_Chor = Figure(figsize=(10,3), dpi=100)
    fig_Chor.add_subplot(title="C_h_zapata").plot(w1,Ch_o)
    fig_Chor.legend('w',loc=8) # -----------------grafica C horizontal
    
    fig_Kvert = Figure(figsize=(10,3), dpi=100)
    fig_Kvert.add_subplot(title="K_v_zapata").plot(w1,Kv_o)
    fig_Kvert.legend('w',loc=8) # -----------------grafica K vertical
    
    fig_Cvert = Figure(figsize=(10,3), dpi=100)
    fig_Cvert.add_subplot(title="C_v_zapata").plot(w1,Cv_o)
    fig_Cvert.legend('w',loc=8)# -----------------grafica C vertical
    
    fig_Krot = Figure(figsize=(10,3), dpi=100)
    fig_Krot.add_subplot(title="K_r_zapata").plot(w1,Kr_o)
    fig_Krot.legend('w',loc=8)# -----------------grafica K rotacional
    
    fig_Crot = Figure(figsize=(10,3), dpi=100)
    fig_Crot.add_subplot(title="C_r_zapata").plot(w1,Cr_o)
    fig_Crot.legend('w',loc=8) #-----------------grafica C rotacional
    
    # ========================PILOTES=======================================
    fig_p_pilotes = Figure(figsize=(10,3), dpi=100)
    fig_p_pilotes.add_subplot(title="Posicion Pilotes (x,y)").plot(x,y,'o',color='blue')
    
    #-------------IMPEDANCIAS----------

    fig_Chor_pil = Figure(figsize=(10,3), dpi=100)
    fig_Chor_pil.add_subplot(title="C_h_pilote").plot(w1,C_p_m_h)
    fig_Chor_pil.legend('w',loc=8) # -----------------grafica C horizontal
    
    fig_Kver_pil = Figure(figsize=(10,3), dpi=100)
    fig_Kver_pil.add_subplot(title="K_h_pilote").plot(w1,K_p_m_v)
    fig_Kver_pil.legend('w',loc=8)    # -----------------grafica K horizontal
    
    fig_Cver_pil = Figure(figsize=(10,3), dpi=100)
    fig_Cver_pil.add_subplot(title="C_h_pilote").plot(w1,C_p_m_v)
    fig_Cver_pil.legend('w',loc=8) # -----------------grafica C horizontal
    
    
    #--------------------------------------------------PREPARAR EL LIENZO DE PRESENTACION-------------------------------------
    canvas_Khor =FigureCanvasTkAgg(fig_Khor,master=imped_k_o)
    canvas_Khor.draw()
    canvas_Khor.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH ) # lienzo K horizontal
    canvas_Chor =FigureCanvasTkAgg(fig_Chor,master=imped_k_o)
    canvas_Chor.draw()
    canvas_Chor.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH ) # lienzo C horizonal
    
    canvas_Kvert =FigureCanvasTkAgg(fig_Kvert,master=imped_k_v) 
    canvas_Kvert.draw()
    canvas_Kvert.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH )# lienzo K vertical
    canvas_Cvert =FigureCanvasTkAgg(fig_Cvert,master=imped_k_v)
    canvas_Cvert.draw()
    canvas_Cvert.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH )# lienzo C vertical
    
    canvas_Krot =FigureCanvasTkAgg(fig_Krot,master=imped_k_r)
    canvas_Krot.draw()
    canvas_Krot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH ) # lienzo K rotacinal
    canvas_Crot =FigureCanvasTkAgg(fig_Crot,master=imped_k_r)
    canvas_Crot.draw()
    canvas_Crot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH )# lienzo C rotacinal
    
    canvas_p_pilotes =FigureCanvasTkAgg(fig_p_pilotes,master=p_pilote)
    canvas_p_pilotes.draw()
    canvas_p_pilotes.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH ) # lienzo POSICION DE PILOTES
    # ======PILOTES=======
    
    canvas_Chor_p =FigureCanvasTkAgg(fig_Chor_pil,master=imped_k_h_p)
    canvas_Chor_p.draw()
    canvas_Chor_p.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH ) # lienzo C horizonal
    
    canvas_Kvert_p =FigureCanvasTkAgg(fig_Kver_pil,master=imped_k_v_p) 
    canvas_Kvert_p.draw()
    canvas_Kvert_p.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH )# lienzo K vertical
    
    canvas_Cvert_p =FigureCanvasTkAgg(fig_Cver_pil,master=imped_k_v_p)
    canvas_Cvert_p.draw()
    canvas_Cvert_p.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH )# lienzo C vertical
    
        #-------------------------------------ESTABLECER LA BARRA DE HERRAMIENTAS EN LA GRAFICA------------------------------------
    toolbar=NavigationToolbar2Tk(canvas_Khor, imped_k_o)
    toolbar.update()
    canvas_Khor.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH)
    
    toolbar2=NavigationToolbar2Tk(canvas_Chor, imped_k_o)
    toolbar2.update()
    canvas_Chor.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    toolbar3=NavigationToolbar2Tk(canvas_Kvert, imped_k_v)
    toolbar3.update()
    canvas_Kvert.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH)
    
    toolbar4=NavigationToolbar2Tk(canvas_Cvert, imped_k_v)
    toolbar4.update()
    canvas_Cvert.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    toolbar5=NavigationToolbar2Tk(canvas_Krot, imped_k_r)
    toolbar5.update()
    canvas_Krot.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH)
    
    toolbar6=NavigationToolbar2Tk(canvas_Crot, imped_k_r)
    toolbar6.update()
    canvas_Crot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)    
    
    toolbar7=NavigationToolbar2Tk(canvas_p_pilotes, p_pilote)
    toolbar7.update()
    canvas_p_pilotes.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)    
    
    # PILOTES


    
    toolbar9=NavigationToolbar2Tk(canvas_Chor_p, imped_k_h_p)
    toolbar9.update()
    canvas_Chor_p.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    toolbar10=NavigationToolbar2Tk(canvas_Kvert_p, imped_k_v_p)
    toolbar10.update()
    canvas_Kvert_p.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH)
    
    toolbar11=NavigationToolbar2Tk(canvas_Cvert_p, imped_k_v_p)
    toolbar11.update()
    canvas_Cvert_p.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
    

    boton_cerrar_kh=tk.Button(imped_k_o, text="cerrar ventana", command=imped_k_o.destroy)
    boton_cerrar_kh.location(x=600,y=700)
    boton_cerrar_kh.place(x=300,y=650)    
    
    boton_cerrar_kv=tk.Button(imped_k_v, text="cerrar ventana", command=imped_k_v.destroy)
    boton_cerrar_kv.location(x=600,y=700)
    boton_cerrar_kv.place(x=300,y=650)    
    
    boton_cerrar_kr=tk.Button(imped_k_r, text="cerrar ventana", command=imped_k_r.destroy)
    boton_cerrar_kr.location(x=600,y=700)
    boton_cerrar_kr.place(x=300,y=650)    
    
    bot_c_p_pil=tk.Button(p_pilote, text="cerrar ventana", command=p_pilote.destroy)
    bot_c_p_pil.location(x=600,y=700)
    bot_c_p_pil.place(x=200,y=650)    
    #===============================CREACIÓN DE REPORTE===================================================

    def ventana_reporte():
        reporte(hora,G,Hs,v,epsilon,Vs,D,B,L,dp,Ep,Es,Lysmer,x,y,A,R,Rr,w1,n_s,n_p,n_h,n_r,n_v,nhs,Kx_o,kx,ch,Kv,kv,cv,Kr,kr,cr,Kh_o,Ch_o,Kv_o,Cv_o,Kr_o,Cr_o,n_p_s,n_p_p,n_p_niu,K_p_h,k_p_h,c_p_h,K_p_v,k_p_v,c_p_v,Fact,Fact_v,K_gp_h,K_gp_r,Ktot_h,Ktot_h_real,Ktot_h_imag,Ktot_rot,Ktot_rot_real,Ktot_rot_imag,eps_tot_gp_h,eps_tot_gp_r)        
    
    imped_report=tk.Toplevel(raiz,width=300, height=150)  # SE ASIGNA A LA VENTANA RAIZ
    imped_report.title("CREACIÓN DE REPORTE")
    imped_report.iconbitmap("logoico1.ico")
    
    fondo_texto_report=tk.StringVar()
    botoncillo_report=tk.Button(imped_report,command=ventana_reporte, textvariable=fondo_texto_report, font="Raleway", bg="grey", fg="white", height=4, width=20) 
    fondo_texto_report.set("GUARDAR REPORTE")
    botoncillo_report.place(x=50, y=30)

    

    
      
    #return     hora,G,Hs,v,epsilon,Vs,D,B,L,dp,Ep,Es,Lysmer,x,y,A,R,Rr,w1,n_s,n_p,n_h,n_r,n_v,nhs,Kx_o,kx,ch,Kv,kv,cv,Kr,kr,cr,Kh_o,Ch_o,Kv_o,Cv_o,Kr_o,Cr_o,n_p_s,n_p_p,n_p_niu,K_p_h,k_p_h,c_p_h,K_p_v,k_p_v,c_p_v,Fact,Fact_v,K_gp_h,K_gp_r,Ktot_h,Ktot_h_real,Ktot_h_imag,Ktot_rot,Ktot_rot_real,Ktot_rot_imag,eps_tot_gp_h,eps_tot_gp_r 
    



    
fondo_texto_Vs=tk.StringVar()
botoncillo_Vs=tk.Button(fondo, command=velocidad_vs, textvariable=fondo_texto_Vs, font="Raleway", bg="grey", fg="white", height=4, width=20) 
fondo_texto_Vs.set("Calculo del Vs")
botoncillo_Vs.place(x=100,y=50)
    
fondo_texto_fimp=tk.StringVar()
botoncillo_fimp=tk.Button(fondo, command=impedancias, textvariable=fondo_texto_fimp, font="Raleway", bg="grey", fg="white", height=4, width=20) # le falta su linea de comeando
fondo_texto_fimp.set("F.Imp zapata+pilotes")
botoncillo_fimp.place(x=300,y=50)

fondo_texto_fimp_pil=tk.StringVar()
botoncillo_fimp_pil=tk.Button(fondo, textvariable=fondo_texto_fimp_pil, font="Raleway", bg="grey", fg="white", height=4, width=20) # le falta su linea de comeando
fondo_texto_fimp_pil.set("F.Imp.zapata")
botoncillo_fimp_pil.place(x=500, y=50)


raiz.mainloop()
    
    
