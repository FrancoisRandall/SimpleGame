import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# The below code associates an image as a value for a variable
# This also loads the image to represent the variable
# The images should be in the same folder as the python file

player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("player.jpg")
prize = pygame.image.load("prize.jpg")

# Allocate the widht and height for the image in order to create boundaries later on

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Player position placeholder 

playerXPosition = 100
playerYPosition = 50

# Makes the enemy start off screen on a random Y-axis position

enemyYPosition = -200
enemyXPosition = random.randint(0, screen_height - enemy_height)
enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)
prizeXPosition = -200
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the up or down key is pressed.
# As it is not pressed at the moment, set value to False

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# Game loop.

while 1: # This is a looping structure that will loop the indented code until you tell it to stop.

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0). 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0 :# This makes sure that the user does not move the player too far left of the window.
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width:# This makes sure that the user does not move the player too far right of the window.
            playerXPosition += 1
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    # Bounding box for the enemy2:

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    # Bounding box for the enemy3:

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    # Bounding box for the prize:

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    # Display losing status to the user:
    # Quite game and exit window:
    
    if playerBox.colliderect(enemyBox):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy2Box):
        print("You lose!") 
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(prizeBox):
        print("You win!")
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:
    # Display wining status to the user:
    # Quite game and exit window:
    
    if enemyXPosition < 0 - enemy_width:
        print("You win!")
        pygame.quit()
        exit(0)

    if enemy2XPosition < 0 - enemy2_width:
        print("You win!")
        pygame.quit()
        exit(0)

    if enemy3XPosition < 0 - enemy3_width:
        print("You win!")
        pygame.quit()
        exit(0)

    # Make enemy approach the player.
    
    enemyYPosition += 0.10
    enemy2XPosition -= 0.20
    enemy3XPosition -= 0.15
    prizeXPosition += 0.17
    
    # ================The game loop logic ends here. =============
  
