#!usr/bin/python
import pygame
import random

pygame.init()
pygame.font.init()

user=0
comp=0
userScore=0
compScore=0
quit= False
clock= pygame.time.Clock()
dispWidth=810
dispHeight=600
image=None
gameEnd= False
text_show= "Play!"
end_text=""
waiting= False

#display mode
py_display= pygame.display.set_mode((dispWidth, dispHeight))
pygame.display.set_caption('Dice up 100')


### Prepare text surface
def text_objects(text, font, clr):
    textSurface = font.render(text, True, clr)
    return textSurface, textSurface.get_rect()


### shows the text on required on position###
def show_text(msg,pos,clr):
	font1 = pygame.font.SysFont(None, 30, False, True)
	text, rect= text_objects(msg, font1, clr)
	rect.center=(pos)
	py_display.blit(text,rect)
	

###how to play part 
def how_to_play():
	intro= False
	py_display.fill((0,0,0))
	while not intro:
		message= "SPACE to roll and SHIFT to hold"
		show_text(message,(dispWidth/2,dispHeight/3),(0,0,255))
		message= "If user gets 1 all the score he/she scored in this round will be lost"
		show_text(message,(dispWidth/2,dispHeight/2.5),(0,0,255))
		message = "if pressed hold then points will be added, your aim is score 50 before computer to win..."
		show_text(message,(dispWidth/2,dispHeight/2),(0,0,255))
		message = "press enter to play"
		show_text(message,(dispWidth/2,dispHeight/1.5), (0,0,255))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type== pygame.KEYDOWN and event.key== pygame.K_RETURN:
				py_display.fill((0,0,0))
				intro = True
			
### intro or start menu of game###
def game_intro():
	intro = False
	while not intro:
		t="1. Press Enter to play \n 2. Press Space for instruction "
		show_text(t, (dispWidth/2, dispHeight/2), (255,255,255))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type== pygame.KEYDOWN and event.key== pygame.K_SPACE:
				how_to_play()
			if event.type== pygame.KEYDOWN and event.key== pygame.K_RETURN:
				intro = True
		


### Main text to display on 
def display_message(text):
	largeText = pygame.font.Font('freesansbold.ttf',87)
	TextSurf, TextRect = text_objects(text, largeText, (0,0,0))
	TextRect.center = ((dispWidth/2),(dispHeight/5))
	py_display.blit(TextSurf, TextRect)


###Display score on screen
def display_score():
	show_text("comp_score: "+str(compScore),(dispWidth*0.15,dispHeight/1.5) , (0, 0, 0))
	show_text("user_score: "+str(userScore),(dispWidth/1.25,dispHeight/1.5) , (0, 0, 0))
	

### updates the changes###
def change_and_update(image, text):
	py_display.fill((153,51,255))
	show_image(image)
	show_text(end_text,(dispWidth/2, dispHeight/2), (0,0,255))
	display_message(text)
	display_score()
	pygame.display.update()


### display image on screen
def show_image(image):
	py_display.blit(image, (dispWidth*0.4, dispHeight*0.3))



###get the image and the number randomly generated
def get_random_image():
	imgs=['dice1.png','dice2.png','dice3.png','dice4.png','dice5.png','dice6.png'] 
	num= random.randint(1,6)-1
	image= pygame.image.load("dice_faces/"+imgs[num])
	return image,num+1


### Computer Turn
def comp_turn():
	global comp
	global image
	global compScore
	global gameEnd
	global text_show
	global waiting
	global end_text
	score=0
	while comp < 20 and score != 1 and not gameEnd:
		image,score= get_random_image()
		comp=comp+score
		change_and_update(image, "wait...")
		clock.tick(60)
		#print comp," ",score
		pygame.time.wait(1000)
	if comp>=20 :
		compScore=compScore+comp
	if compScore>=50:
		text_show="comp wins"+str(compScore)
		end_text="PRESS ENTER TO PLAY AGAIN"
		gameEnd= True
	comp=0
	waiting= False




	



image,num=get_random_image()

game_intro()

#game loop
while not quit:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit= True

		if event.type== pygame.KEYDOWN and event.key== pygame.K_SPACE and gameEnd==False and  waiting==False:
			image, score = get_random_image()
			if score == 1:
				user=0
				change_and_update(image, "wait...")
				pygame.time.wait(1000)
				waiting=True
				comp_turn()
			else:
				change_and_update(image, "Play!")
				user=user+score


		if event.type== pygame.KEYDOWN and event.key== pygame.K_RSHIFT and gameEnd== False and waiting==False:
			userScore= userScore+ user
			user=0
			if userScore>=50:
				text_show= "user WIN"+str(userScore)
				end_text="PRESS ENTER TO PLAY AGAIN"
				gameEnd= True
			else:
				change_and_update(image, "wait..")
				pygame.time.wait(1000)
				waiting=True
				comp_turn()


		if event.type== pygame.KEYDOWN and event.key== pygame.K_RETURN and gameEnd == True:
			user=0
			comp=0
			userScore=0
			compScore=0
			gameEnd= False
			text_show="Play!"
			end_text=""
			change_and_update(image, text_show)
			

		
			
	
	py_display.fill((153,51,255))
	
	show_image(image)
	show_text(end_text,(dispWidth/2, dispHeight/2),(0,0,255))
	display_message(text_show)
	display_score()
	
	pygame.display.update()
	clock.tick(60) 

pygame.quit()

