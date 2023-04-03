# Importing the necessary modules
import pygame
import random

# Initializing Pygame
pygame.init()

# Setting the screen width and height
width, height = 500, 700

# Creating a Pygame clock object to control the game's frame rate
CLOCK = pygame.time.Clock()

# Setting the initial score to 0
score = 0

# Creating a Pygame font object to display the score
font = pygame.font.Font(None, 30)

# Creating the Pygame screen
screen = pygame.display.set_mode((width, height))

# Setting the window caption
pygame.display.set_caption("car racer")

# Loading the background image and resizing it to fit the screen
back = pygame.image.load('/home/asifjahish/vscode/pp2--21B031342-/tsis8/CarRacer/AnimatedStreet.png')
back_size = pygame.transform.scale(back, (500, 700))

# Creating a Pygame Sprite subclass for the coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        coin = pygame.image.load('/home/asifjahish/vscode/pp2--21B031342-/tsis8/CarRacer/coin.png')
        coin_size= pygame.transform.scale(coin,(50,50))
        self.image = coin_size
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width // 2, width - self.rect.width // 2),1)
    
    # Method to reset the coin's position when it goes off-screen
    def reset(self):
        self.rect.center = (random.randint(self.rect.width // 2, width - self.rect.width // 2), 1)
              
    # Method to move the coin downwards on the screen
    def move(self):
        self.rect.move_ip(0, 2)
        if self.rect.top >height:
            self.reset()
  
    # Method to draw the coin on the screen
    def draw(self):
        screen.blit(self.image, self.rect)

# Creating a Pygame Sprite subclass for the computer-controlled car
class ComputerPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        redcar = pygame.image.load('/home/asifjahish/vscode/pp2--21B031342-/tsis8/CarRacer/Enemy.png')
        self.image = redcar
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width // 2, width - self.rect.width // 2), 0)

    # Method to move the computer-controlled car downwards on the screen
    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top >height:
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width // 2, width - self.rect.width // 2), 0)

    # Method to draw the computer-controlled car on the screen
    def draw(self):
        screen.blit(self.image, self.rect)

# Creating a Pygame Sprite subclass for the player's car
# define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player = pygame.image.load('/home/asifjahish/vscode/pp2--21B031342-/tsis8/CarRacer/Player.png')
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - self.rect.height // 2 - 20)
        self.player_x = width
        self.player_y = 0
        self.player_speed = 3

    def draw(self):
        screen.blit(self.image, (self.player_x, self.player_y))

    def movement(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 5 and pressed[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < width - 5 and pressed[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)


player = Player()
computerPlayer = ComputerPlayer()
coin= Coin()
score_text = font.render("Score: 0", True, (255, 255, 255))

# set up the groups of sprites
coin_group = pygame.sprite.Group(coin)
player_group = pygame.sprite.Group(player)
computer_group = pygame.sprite.Group(computerPlayer)


# load the sound effects
crash_sound = pygame.mixer.Sound('/home/asifjahish/vscode/pp2--21B031342-/tsis8/CarRacer/crashing.mp3')
sound = pygame.mixer.Sound('/home/asifjahish/vscode/pp2--21B031342-/tsis8/CarRacer/race-car.mp3')




running = True
while running:
    screen.blit(back_size, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    sound.play()
    if pygame.sprite.spritecollide(player, coin_group, True):
        score += 1
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        coin_group.add(Coin())

    for coin in coin_group:
        coin.move()
        coin.draw()
        screen.blit(score_text, (0, 0))
    player.movement()
    computerPlayer.move()
    
    if pygame.sprite.spritecollideany(player, computer_group):
        crash_sound.play()
        sound.stop()
        running = False
    

    player_group.draw(screen)
    computer_group.draw(screen)
    
    
    pygame.display.update()
    CLOCK.tick(100)
    pygame.display.flip()

pygame.quit()


""" ## Loop through each event in the event queue
for event in pygame.event.get():
    # If the event is a "QUIT" event (e.g. user clicks on close button)
    if event.type == pygame.QUIT:
        # Set the variable "running" to False to exit the loop
        running = False

# Play the sound effect of car engine
sound.play()

# Check if the player sprite collides with the coin sprite group
if pygame.sprite.spritecollide(player, coin_group, True):
    # Increment the score by 1
    score += 1
    # Render the score text with the updated score and assign to the score_text variable
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    # Add a new coin to the coin sprite group
    coin_group.add(Coin())

# Loop through each coin in the coin sprite group
for coin in coin_group:
    # Move the coin down the screen
    coin.move()
    # Draw the coin on the screen
    coin.draw()
    # Draw the score text on the screen at (0,0)
    screen.blit(score_text, (0, 0))

# Move the player sprite according to the user input
player.movement()
# Move the computerPlayer sprite
computerPlayer.move()

# Check if the player sprite collides with the computerPlayer sprite group
if pygame.sprite.spritecollideany(player, computer_group):
    # Play the sound effect of crashing
    crash_sound.play()
    # Stop the sound effect of car engine
    sound.stop()
    # Set the variable "running" to False to exit the loop
    running = False

# Draw the player sprite on the screen
player_group.draw(screen)
# Draw the computerPlayer sprite on the screen
computer_group.draw(screen)

# Update the display
pygame.display.update()
# Set the frame rate to 100 frames per second
CLOCK.tick(100)
# Flip the display
pygame.display.flip()
"""