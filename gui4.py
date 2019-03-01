from tkinter import *
import pygame.mixer

app = Tk()
app.title('Who wants to be a millionaire')

sounds = pygame.mixer
sounds.init()

rights = IntVar()
rights.set(0)
wrongs = IntVar()
wrongs.set(0)

def wait_sound(channel):
    while channel.get_busy():
        pass


def right_song():
    global rights
    s = sounds.Sound('heartbeat.wav')
    wait_sound(s.play())
    rights.set(rights.get() + 1)
    

def wrong_song():
    global wrongs
    s = sounds.Sound('bell.wav')
    wait_sound(s.play())
    wrongs.set(wrongs.get() + 1)


lab = Label(app, text='Press the button', height = 3)
lab.pack()
lab1 = Label(app, textvariable = rights)
lab1.pack(side = 'left')
lab2 = Label(app, textvariable = wrongs)
lab2.pack(side = 'right')


b1 = Button(app, text = 'Right!', width = 10, command = right_song)
b1.pack (side = 'left', padx = 10, pady = 10)
b2 = Button(app, text = 'Wrong!', width = 10, command = wrong_song)
b2.pack (side = 'right', padx = 10, pady = 10)

app.mainloop()