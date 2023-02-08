import pygame
import random
#import time
pygame.init()

#variables:
BGCOLOR = "light blue"
player_1 = ""
tie = 0
win = 0
loss = 0

#loading assets:
rock_image = pygame.image.load("assets/Rock.png")
rock_image = pygame.transform.scale(rock_image, (100, 100))
paper_image = pygame.image.load("assets/Paper.png")
paper_image = pygame.transform.scale(paper_image, (100, 100))
scissors_image = pygame.image.load("assets/Scissors.png")
scissors_image = pygame.transform.scale(scissors_image, (100, 100))



#functions for interactable objects:

def printing_text(text, x, y):
        set_my_text = pygame.font.SysFont("arial", 60)
        textSurface = set_my_text.render(text, True, "black")
        screen.blit(textSurface, (x, y))

        

#initialize screen
screen = pygame.display.set_mode([1000, 1000])

running = True
while running:

        # check for events / get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                '''
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player_1 = "Rock"
                elif event.key == pygame.K_p:
                    player_1 = "Paper"
                elif event.key == pygame.K_s:
                    player_1 = "Scissors"
                    '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if rock.collidepoint(mouse_x, mouse_y):
                            player_1 = 'Rock'
                    if paper.collidepoint(mouse_x, mouse_y):
                            player_1 = 'Paper'
                    if scissors.collidepoint(mouse_x, mouse_y):
                            player_1 = 'Scissors'
                    #pygame will track the position you clicked



            
        # do stuff / proccess input

        choices = ['Rock', 'Paper', 'Scissors']
        player_2 = choices[random.randint(0,2)]
        
        



        # update screen

        screen.fill(BGCOLOR)
        rock = screen.blit(rock_image, (100,200))
        paper = screen.blit(paper_image, (350, 200))
        scissors = screen.blit(scissors_image, (600, 200))
        
        printing_text(f"ties: {tie} losses: {loss} wins: {win}", 200, 800)
        
        if player_1 != "":

                printing_text(f"You chose {player_1}", 275, 500)
                '''
                pygame.time.wait(1000)
                printing_text(".", 250, 600)
                pygame.time.wait(1000)
                printing_text(".", 500, 600)
                pygame.time.wait(1000)
                printing_text(".", 750, 600)
                '''
                printing_text(f"Your opponent chose {player_2}", 125, 600)
                if player_1 == player_2:
                       printing_text("You tied", 400, 700)
                       tie += 1
        
                elif player_1 == 'Rock':
                        if player_2 == 'Scissors':
                                printing_text("You won!", 400, 700)
                                win += 1
                        elif player_2 == "Paper":
                                printing_text("You lost!", 400, 700)
                                loss += 1
                elif player_1 == 'Paper':
                        if player_2 == 'Rock':
                                printing_text('You won!', 400, 700)
                                win += 1
                        elif player_2 == 'Scissors':
                                printing_text('You lost!', 400, 700)
                                loss += 1
                elif player_1 == 'Scissors':
                        if player_2 == 'Paper':
                                printing_text("You won!", 400, 700)
                                win += 1
                        elif player_2 == 'Rock':
                                printing_text("You lost!", 400, 700)
                                loss += 1


                pygame.display.update()
                pygame.time.wait(1500)
                player_1 = ""




            

        
        #pygame.draw.circle(screen, "red", (400,300), 100)
    
        # draw screen

        pygame.display.flip()

pygame.quit()
