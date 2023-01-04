# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 17:15:46 2023

@author: User
"""

from datetime import datetime
from tkinter import *
import time 

oyna = Tk()
oyna.title('✅YANGI YILNI ANIQLASH✅')
oyna.geometry("520x520")

natija = Label(text="Yangi yil",bg="lime",font="Arial 12")
natija.place(x=30,y=160,width="460",height="50")

def aniqla():
    yangi_yil = {"yil":2023,"oy":12,"kun":31}
    vaqt = {"soat":23,"minut":59,"sekund":59}
    bugun = datetime.today()
    yil = bugun.year
    oy = bugun.month
    kun = bugun.day
    
    bugun = datetime.today()
    soat = bugun.hour
    minut = bugun.minute
    sekund = bugun.second
    
    aniqlandi = " Yangi yilga {0} oy, {1} kun  va {2} soat, {3} minut, {4} sekund qoldi".format(yangi_yil["oy"]-oy,yangi_yil["kun"]-kun,vaqt["soat"]-soat,vaqt["minut"]-minut,vaqt["sekund"]-sekund)
    natija.config(text=aniqlandi)
   
    
    

aniqlash = Button(text="Yangi yilni aniqlash",bg="yellow",command=aniqla, font="Arial 15")
aniqlash.place(x=180,y=220,width="170",height="60")
oyna.mainloop()






