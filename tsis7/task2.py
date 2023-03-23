import pygame

pygame.init()
pygame.mixer.init()

# Load audio files
tracks = ["/home/sayed/VScode/python/PP2-21B031339/tsis7/music/fire.mp3",
           "/home/sayed/VScode/python/PP2-21B031339/tsis7/music/rain.mp3",
             "/home/sayed/VScode/python/PP2-21B031339/tsis7/music/Raindrops.mp3"]

current_track_index = 0
music = pygame.mixer.music.load(tracks[current_track_index])

# Define keyboard controls
play_pause_key = pygame.K_SPACE
stop_key = pygame.K_s
next_track_key = pygame.K_RIGHT
prev_track_key = pygame.K_LEFT

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define the font
font = pygame.font.Font(None, 36)

# Create the window
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Music Player")

# Start playing the music
pygame.mixer.music.play()

while True:
    # Check for keyboard events
    keys = pygame.key.get_pressed()

    if keys[play_pause_key]:
        # Toggle between playing and pausing the music
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    if keys[stop_key]:
        # Stop the music
        pygame.mixer.music.stop()

    if keys[next_track_key]:
        # Play the next track
        current_track_index = (current_track_index + 1) % len(tracks)
        music = pygame.mixer.music.load(tracks[current_track_index])
        pygame.mixer.music.play()

    if keys[prev_track_key]:
        # Play the previous track
        current_track_index = (current_track_index - 1) % len(tracks)
        music = pygame.mixer.music.load(tracks[current_track_index])
        pygame.mixer.music.play()

    # Draw the background
    screen.fill(white)

    # Draw the current track name
    text = font.render(f"Current track: {tracks[current_track_index]}", True, black)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Allow the program to exit if the window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
