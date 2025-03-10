from tkinter import *
from random import *
import random
import time
import threading
import json
import os


lemonapp = Tk()
lemonapp.title("майнер")
lemonapp.geometry("500x600")



def viiti():
        lemonapp.quit()





pogod_list = ['Солнечно', 'Сильно ветренно', 'Очень жарко', 'Дождь', 'Облачно']
pogod = random.choice(pogod_list)



def igra():
    global loadeday
    global loade
    try:
        filename = 'save.json'
        with open(filename) as f:
            loader = json.load(f)
            loade = loader[0]
            loadeday = loader[1]
    except FileNotFoundError:
        loade = 0
        loadeday = 1
    pphp.destroy()
    def ende():
        ratatata()
        end = Label(lemonapp, text="buhf rjy",font = ("Comic Sans MS",15))
        end.pack()
        pphpr = Button(lemonapp,width=5,height=2, text="Начать заного", font = ("Comic Sans MS",15),command = lambda: (delete(),igra()))
        pphpr.place(x = 100,y = 500)
        global loade
        global loadeday
        loade = 0
        loadeday = 1

        

    def hellol():
        jhjh()
        ratatata()
        
            
        global xx
        xx = [x,xp]
        filename = 'save.json'
        with open(filename, 'w') as f:
            json.dump(xx, f)
        
        def fff():
            drdrdr.destroy()
            
        
    
        

        
        drdrdr = Label(lemonapp, text="День закончен!вы намайнили много деняк",font = ("Comic Sans MS",15))
        drdrdr.place(x = 150,y = 0)

        viviviv = Button(lemonapp,width=15,height=8, text="Продолжить", font = ("Comic Sans MS",15),command = lambda: (igra(),viviviv.destroy(),fff()))
        viviviv.place(x = 150,y = 250)
        
            
        
        
        
        
    startigra.destroy()
    vihod2.destroy()
    
  
    
    def magaz():
        r = int(cur_dollr["text"]) + 1
        cur_dollr["text"] = str(r)
        
        
    def ratatata():
        dollariki.destroy()
        cur_dollr.destroy()
        pogoda.destroy()
        cur_pogoda.destroy()
        magazik.destroy()
        day.destroy()
        dayse.destroy()
        
        
              
    
        
    
    day = Label(lemonapp, text="День:",font = ("Comic Sans MS",15))
    dayse = Label(lemonapp, text="1",font = ("Comic Sans MS",15))
    dollariki = Label(lemonapp, text="Долларики:",font = ("Comic Sans MS",15))
    cur_dollr = Label(lemonapp, text="0",font = ("Comic Sans MS",15))
    pogoda = Label(lemonapp, text="Погода:",font = ("Comic Sans MS",15))
    cur_pogoda = Label(lemonapp, text=pogod,font = ("Comic Sans MS",15))
    

    magazik = Button(lemonapp,width=10,height=4, text="магазин", font = ("Comic Sans MS",15),command = magaz)

    
    
    

    dollariki.place(x = 10, y = 0)
    cur_dollr.place(x = 150,y = 0)
    """pogoda.place(x = 10,y = 30)
    cur_pogoda.place(x = 110,y = 30)"""
    
    magazik.place(x = 350, y = 450)
    """day.pack()
    dayse.pack()"""
    dayse["text"] = loadeday
    cur_dollr["text"] = loade
    
    t = threading.Timer(10, lambda: (hellol()))
    t.start() 
    if loadeday == 2:
        ende()
    def jhjh():
            global xp
            global x
            x = cur_dollr["text"]
            global loadeday
            loadeday = loadeday + 1
            xp = loadeday
    



def delete():
    try:
        os.remove('save.json')
    except FileNotFoundError:
        pass 

        

        

pphp = Button(lemonapp,width=5,height=2, text="удалить сохран", font = ("Comic Sans MS",15),command = delete)
pphp.place(x = 100,y = 500)


startigra = Button(lemonapp,width=10,height=10, text="Начать игру", font = ("Comic Sans MS",15),command = igra,)
vihod2 = Button(lemonapp,width=5,height=2, text="Выйти", font = ("Comic Sans MS",15),command = viiti)
vihod2.place(x = 10,y = 500)
startigra.place(x = 10, y = 10)
    

lemonapp.mainloop()