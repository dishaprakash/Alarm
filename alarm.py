import tkinter as tk
import sys
import time
import pygame
import sqlite3
import datetime
import threading

pygame.init()
cdate=''
pygame.mixer.music.load("beep.wav") 

def set(d,t):
    global r
    global cdate
    c.execute("INSERT INTO alarms(date,time) VALUES(?,?)",[d,t])
    conn.commit()
    c.execute("SELECT date,time FROM alarms")
    cdate = c.fetchall()
    r+=1
    main(r)

    
def check():
    global lab    
    while 1:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        dat = datetime.date.today().strftime("%d/%m/%Y")
        for i in cdate:
            if i[0] == dat and i[1] == now:
                pygame.mixer.music.play(15)
                
        time.sleep(1)

def main(r):
    background_image = tk.PhotoImage(file = 'clock.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0,y=0,relheight=1,relwidth=1)

    label = tk.Label(root,text='Alarm Clock',font=('Courier New TUR',40))
    label.place(relx=0.5,rely=0.2)

    label = tk.Label(root,text='Date in \ndd/mm/yyyy',font=('Courier New TUR',20))
    label.place(relx=0.44,rely=0.4)

    label = tk.Label(root,text='Time in \nHH:MM:SS',font=('Courier New TUR',20))
    label.place(relx=0.74,rely=0.4)
    
    entry1 = tk.Entry(root,font=('Courier New TUR',20))
    entry1.place(relx=0.42,rely=0.55,relheight=0.05,relwidth=0.2)

    entry2 = tk.Entry(root,font=('Courier New TUR',20))
    entry2.place(relx=0.71,rely=0.55,relheight=0.05,relwidth=0.2)

    
    button = tk.Button(root,text='Set Alarm',font=('Courier New TUR',20),bg='#444657',activebackground='black',fg='white',activeforeground='white',
                       command=lambda:(set(entry1.get(),entry2.get())))
    button.place(relx=0.58,rely=0.8)

    if r>0:
        label = tk.Label(root,text='Alarm Set',font=('Courier New TUR',20),fg='red')
        label.place(relx=0.58,rely=0.7)
    
    root.mainloop()
    
root = tk.Tk()
canvas =tk.Canvas(root,width=800,height=600)
canvas.pack()

conn = sqlite3.connect('Alarm.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS alarms(date TEXT,time TEXT)")
r=0
if __name__ == '__main__':
    mProcess = threading.Thread(target=check)
    mProcess.daemon = True
    mProcess.start()
main(r)
root.mainloop()
