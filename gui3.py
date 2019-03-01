from tkinter import *
import pygame.mixer

app = Tk()
app.title('Who wants to be a millionaire')
app.geometry('300x100+200+100')

sounds = pygame.mixer
sounds.init()

rights = 0
wrongs = 0
def wait_sound(channel):
    while channel.get_busy():
        pass


def right_song():
    global rights
    s = sounds.Sound('heartbeat.wav')
    wait_sound(s.play())
    rights += rights

def wrong_song():
    global wrongs
    s = sounds.Sound('bell.wav')
    wait_sound(s.play())
    wrongs += wrongs

b1 = Button(app, text = 'Right!', width = 10, command = right_song)
b1.pack (side = 'left', padx = 10, pady = 10)
b2 = Button(app, text = 'Wrong!', width = 10, command = wrong_song)
b2.pack (side = 'right', padx = 10, pady = 10)

app.mainloop()






