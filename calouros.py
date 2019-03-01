import pygame.mixer

sounds = pygame.mixer
sounds.init()

def wait_sound(channel):
    while channel.get_busy():
        pass

right = 0
wrong = 0
options = int(input('Press 1)Right 2)Wrong and 0)Finish  '))
while options != 0:
    if options == 1:
        s = sounds.Sound('guitar.wav')
        wait_sound(s.play())
    if options == 2:
        s = sounds.Sound('heartbeat.wav')
        wait_sound(s.play())
    options = int(input('Press 1)Right 2)Wrong and 0)Finish  '))
print('Rights: ', right, 'Wrongs: ', wrong)


