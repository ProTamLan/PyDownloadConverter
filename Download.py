from os import link
from tkinter import *
from tkinter import filedialog

screen=Tk()
title= screen.title('Downloader')
canvas=Canvas(screen, width=850, height=550,background=('#255000000'))
canvas.pack()

logo_img=PhotoImage(file='Lemon.png') #logo
logo_img=logo_img.subsample(-1) #size
canvas.create_image(850/2,550/2,image=logo_img)
link_field=Entry(screen, width=80)
link_label=Label(screen, text="Paste the link here: ", font=('Bookman Old Style', 14),background=('#255000000'))
canvas.create_window(850/2,200,window=link_label) #words
canvas.create_window(850/2,450,window=link_field) #window to drop link

path_label=Label(screen, text="Select path for download",font=('Bookman Old Style', 14))
select_button=Button(screen, text='Select')
canvas.create_window(850/2,360,window=path_label)
canvas.create_window(850/2,400,window=select_button) #path for save
#download buttom
button=Button(screen, text= "Download")
#add to canvas
canvas.create_window(250,400, window=button)

screen.mainloop()
