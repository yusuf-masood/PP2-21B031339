

import sys
import pygame
import os
pygame.init()

size = (650, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mickey's Clock")

clock = pygame.time.Clock()

face_img = pygame.image.load(os.path.join('image','mickeyclock.jpeg'))
right_hand_img = pygame.image.load(os.path.join('image','mickeyclock.jpeg'))
left_hand_img = pygame.transform.flip(right_hand_img, True, False) # Flip image to make it left hand

right_hand_pos = (250, 250)
left_hand_pos = (250, 250)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
            pygame.fill(face_img )
    
  
    pygame.display.update()
    
    
