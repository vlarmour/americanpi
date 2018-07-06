from gpiozero import Button, LED
from time import sleep
import pygame

pygame.init()

redbtn = Button(17)
whitebtn = Button(27)
bluebtn = Button(22)

redLED = LED(14)
whiteLED = LED(15)
blueLED = LED(18)

redaudio = pygame.mixer.Sound('/home/pi/Desktop/IMG_7209.wav')
blueaudio = pygame.mixer.Sound('/home/pi/Desktop/IMG_7218.wav')
whiteaudio = pygame.mixer.Sound('/home/pi/Desktop/IMG_7228.wav')

def red():
    redbtn.wait_for_press()
    redLED.on()
    redaudio.play()

def white():
    whitebtn.wait_for_press()
    whiteLED.on()
    whiteaudio.play()
    
def blue():
    bluebtn.wait_for_press()
    blueLED.on()
    blueaudio.play()
    
while True:
    redbtn.wait_for_press()
    redLED.on()
    redaudio.play()
    whitebtn.wait_for_press()
    whiteLED.on()
    whiteaudio.play()
    bluebtn.wait_for_press()
    blueLED.on()
    blueaudio.play()