import pygame.mixer

sounds = pygame.mixer
sounds.init()

def wait_sound(channel):
    while channel.get_busy():
        pass


s = sounds.Sound('heartbeat.wav')
wait_sound(s.play())
s = sounds.Sound('guitar.wav')
wait_sound(s.play())
s = sounds.Sound('cat.wav')
wait_sound(s.play())
s = sounds.Sound('bell.wav')
wait_sound(s.play())
