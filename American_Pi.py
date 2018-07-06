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
    if redbtn.is_pressed:
        redLED.on()
        redaudio.play()
    if whitebtn.is_pressed:
        whiteLED.on()
        whiteaudio.play()
    if bluebtn.is_pressed:
        blueLED.on()
        blueaudio.play()