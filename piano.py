# coding: utf8
# piano.py

#-- параметры --
canv_wd = 600           # ширина и высота поля
canv_ht = 350

btn_wd = 40             # размеры клавиши
btn_ht = 160
pos_x = 100             # начало клавиш по горизонтали
pos_y = 150             # начало клавиш по вертикали
pos_dx = 10             # промежуток между клавишами


from Tkinter import *
import winsound
import time
import random

root = Tk()
canv = Canvas(root, height = canv_ht, width = canv_wd, bg='#000066')
canv.pack()

# клавиши
x = pos_x; y = pos_y
btn_do = canv.create_rectangle(x,y, x + btn_wd, y + btn_ht,fil = 'white')
x += btn_wd + pos_dx
btn_re = canv.create_rectangle(x,y, x + btn_wd, y + btn_ht,fil = 'white')
x += btn_wd + pos_dx
btn_mi = canv.create_rectangle(x,y, x + btn_wd, y + btn_ht,fil = 'white')
x += btn_wd + pos_dx
btn_fa = canv.create_rectangle(x,y, x + btn_wd, y + btn_ht,fil = 'white')
x += btn_wd + pos_dx
btn_sol = canv.create_rectangle(x,y, x + btn_wd, y + btn_ht,fil = 'white')
x += btn_wd + pos_dx
btn_la = canv.create_rectangle(x,y, x + btn_wd, y + btn_ht,fil = 'white')
x += btn_wd + pos_dx
btn_si = canv.create_rectangle(x,y, x + btn_wd, y + btn_ht,fil = 'white')

def play_note(note, btn):
    canv.itemconfig(btn_do, fil = 'white' )
    canv.itemconfig(btn_re, fil = 'white' )
    canv.itemconfig(btn_mi, fil = 'white' )
    canv.itemconfig(btn_fa, fil = 'white' )
    canv.itemconfig(btn_sol, fil = 'white' )
    canv.itemconfig(btn_la, fil = 'white' )
    canv.itemconfig(btn_si, fil = 'white' )
    file_name = "notes/"+note+".wav"
    winsound.PlaySound(file_name, winsound.SND_FILENAME )
    canv.itemconfig(btn, fil = 'yellow' )

musics=['birthday','ohota','pogoda','storm']

def key_handl(event):
    # обработать нажатия клавиш
    global leftrack_speed, rightrack_speed, left_count, right_count, moveball_flag
    #print event.keysym
    if  event.keysym == "z":
        play_note('do', btn_do)    
    elif  event.keysym == "x":
        play_note('re', btn_re)    
    elif  event.keysym == "c":
        play_note('mi', btn_mi)    
    elif  event.keysym == "v":
        play_note('fa', btn_fa)    
    elif  event.keysym == "b":
        play_note('sol', btn_sol)    
    elif  event.keysym == "n":
        play_note('la', btn_la)    
    elif  event.keysym == "m":
        play_note('si', btn_si)    

def mouse_handl(event):
    random.shuffle (musics)
    music = musics[0]
    file_name = music+".wav"
    winsound.PlaySound(file_name, winsound.SND_FILENAME|winsound.SND_ASYNC )    
    
# включить обработчик клавиатуры
canv.bind("<KeyPress>",key_handl)
canv.bind('<Button-1>',mouse_handl)
canv.focus_set()


root.mainloop()
