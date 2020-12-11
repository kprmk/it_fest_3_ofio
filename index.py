'''Запускать из рабочей папки проекта!'''
import pygame
from storage import *
from strings import *
import time
import pathlib


W, H, FPS = 860, 540, 60
###########################################################

pygame.init()
app = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
###########################################################
col_in = (0, 200, 200)
col_out = (153, 204, 255)
window_col = (153, 204, 255)
text_col = (0, 10, 51)
name_window = (77, 77, 51)
name_col = (255, 255, 200)
next_in = (107, 107, 71)
next_out = name_window
score_usr = 0
usr_name = ''
score_win = 0 # Для вычесления исхода
score_answer = 0 # Для определения последующего действия
score_decor = 0 #Для ожерелья
k_x = 0 #Для анимация компаньона 1ого
###########################################################
chr_unknown = "???" #Пока поьзователь не узнал имя(для 1 компаньона и собаки)
chr_1name = "Дагфинн"
chr_2name = "Ульф"
chr_snake = "Великий Змей Алвис"
chr_tradesman = "Торговец"
###########################################################
#Sound
sound_noise = pygame.mixer.Sound(r'assets\Sounds\Шум_рынка.mp3')
sound_cave_in = pygame.mixer.Sound(r'assets\Sounds\В_пещере.mp3')
sound_search = pygame.mixer.Sound(r'assets\Sounds\выкапывание_ожерелья.mp3')
sound_moon = pygame.mixer.Sound(r'assets\Sounds\для_первой_локации.mp3')
sound_forest = pygame.mixer.Sound(r'assets\Sounds\Сверчки.mp3')
sound_crawl = pygame.mixer.Sound(r'assets\Sounds\змея _сползает.mp3')
sound_roar = pygame.mixer.Sound(r'assets\Sounds\Рычание_волка.mp3')
sound_river = pygame.mixer.Sound(r'assets\Sounds\К_реке.mp3')
sound_changing = pygame.mixer.Sound(r'assets\Sounds\Превращение_волка.mp3')
sound_cave_out = pygame.mixer.Sound(r'assets\Sounds\Перед_пещерой.mp3')
sound_before = pygame.mixer.Sound(r'assets\Sounds\Перед_Городом.mp3')
sound_hs = pygame.mixer.Sound(r'assets\Sounds\Шипение_Атака.mp3')
sound_miracle = pygame.mixer.Sound(r'assets\Sounds\Змей_в_Питона.mp3')
sound_fly = pygame.mixer.Sound(r'assets\Sounds\Полёт.mp3')
sound_around = pygame.mixer.Sound(r'assets\Sounds\Перед_Перед_пещерой.mp3')
sound_death = pygame.mixer.Sound(r'assets\Sounds\Смерть.mp3')
pygame.mixer.music.set_volume(0.1)#######SOOUUND
###########################################################
#Background
back_img1 = pygame.image.load(r'assets\Background\1.jpg')
back_img2 = pygame.image.load(r'assets\Background\2.jpg')
back_img3 = pygame.image.load(r'assets\Background\3.png')
back_img33 = pygame.image.load(r'assets\Background\33.png')
back_img4 = pygame.image.load(r'assets\Background\4.jpg')
back_img5 = pygame.image.load(r'assets\Background\5.jpg')
back_img6 = pygame.image.load(r'assets\Background\6.jpg')
back_img7 = pygame.image.load(r'assets\Background\7.jpg')
back_img8 = pygame.image.load(r'assets\Background\8.jpg')
back_img9 = pygame.image.load(r'assets\Background\9.jpg')
back_img10 = pygame.image.load(r'assets\Background\10.jpg')
back_img11= pygame.image.load(r'assets\Background\11.jpg')
###########################################################
#Characters спрайты
snake_img1 = pygame.image.load(r'assets\cheracters\piton1.png')
snake_img2 = pygame.image.load(r'assets\cheracters\piton2.png')
snake_img3 = pygame.image.load(r'assets\cheracters\piton3.png')
snake_img4 = pygame.image.load(r'assets\cheracters\piton4.png')
wolf_img1 = pygame.image.load(r'assets\cheracters\wolf10.png')
wolf_img2 = pygame.image.load(r'assets\cheracters\wolf20.png')
wolf_img3 = pygame.image.load(r'assets\cheracters\wolf30.png')
wolf_img4 = pygame.image.load(r'assets\cheracters\wolf40.png')
wolf_img5 = pygame.image.load(r'assets\cheracters\wolf50.png')
kompon_img1 = pygame.image.load(r'assets\cheracters\komp1.png')
kompon_img2 = pygame.image.load(r'assets\cheracters\komp2.png')
kompon_img3 = pygame.image.load(r'assets\cheracters\komp3.png')
kompon_img4 = pygame.image.load(r'assets\cheracters\komp4.png')
kompon_img5 = pygame.image.load(r'assets\cheracters\komp5.png')
kompon_img6 = pygame.image.load(r'assets\cheracters\komp6.png')
kompon_img7 = pygame.image.load(r'assets\cheracters\komp7.png')
dealer_img1 = pygame.image.load(r'assets\cheracters\dealer1.png')
dealer_img2 = pygame.image.load(r'assets\cheracters\dealer2.png')
###########################################################
#weapons
weapon_img1 = pygame.image.load(r'assets\weapons\A1.png')
weapon_img2 = pygame.image.load(r'assets\weapons\A2.png')
weapon_img3 = pygame.image.load(r'assets\weapons\A3.png')#Ожерелье
###########################################################
#Для перехода
black_img = pygame.image.load(r'assets\Background\black.png')
###########################################################


def update_with_mouse():
	pygame.draw.circle(app, (255, 255, 255), pygame.mouse.get_pos(), 10)
	# app.blit(cursor_img, pygame.mouse.get_pos())
	pygame.display.update()

def trans(img):
	return pygame.transform.scale(img, (860, 540))


# Функция для создания первого окна с текстом поверх спрайта персонажа + его имени
def txt_first():
	is_ready = False
	x = W
	y = 10
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img1), (0, 0))
		sound_fly.set_volume(0.1)
		sound_fly.play()
		if x > 450:
			x -= 2
		else:
			is_ready = True
			sound_fly.stop()
		app.blit(kompon_img5, (x, y)) #Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_unknown, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(A1_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(A1_2, 70, 370, font_col = text_col)
		print_text(A1_3, 70, 400, font_col = text_col)

		if is_ready is True:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action=txt_first_1)

		update_with_mouse()
		clock.tick(FPS)


def txt_first_1():
	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		if star_time > 1:
			app.blit(trans(back_img1), (0, 0))
			app.blit(kompon_img1, (450, 10))#Всавить спрайт персонажа
			pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
			pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
			print_text(chr_unknown, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
			print_text(A2_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета

			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_first_2)
			update_with_mouse()


def txt_first_2():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
				
		app.blit(trans(back_img1), (0, 0))
		button_txt(110, 140, 630, 100, 'Что ты такое?', x_sh = 30, y_sh = 30, action = txt_first_21)
		button_txt(110, 300, 630, 100, 'Как я здесь оказался?', x_sh = 30, y_sh = 30, action = txt_first_22)
		
		update_with_mouse()


def txt_first_21():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img1), (0, 0))
		app.blit(kompon_img2, (450, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_unknown, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text("Как невежливо.Похоже ты не здешний…", 70, 340, font_col = text_col) #Выведет сам текст сюжета

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_first_3)
		update_with_mouse()


def txt_first_22():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img1), (0, 0))
		app.blit(kompon_img4, (450, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_unknown, 120, 290, font_col = name_col, font_size= 30)
		print_text("Ты попаданец, ух-ты…", 70, 340, font_col = text_col)


		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_first_3)
		update_with_mouse()


def txt_first_3():

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img1), (0, 0))
		app.blit(kompon_img4, (450, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_unknown, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(A3_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(A3_2, 70, 370, font_col = text_col)
		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_first_4)

		update_with_mouse()


def txt_first_4():

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img1), (0, 0))
		app.blit(kompon_img3, (450, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text(A4_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(A4_2, 70, 370, font_col = text_col) #Выведет сам текст сюжета

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_first_5)
		update_with_mouse()


def txt_first_5():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img1), (0, 0))
		app.blit(kompon_img7, (400, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(A5_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_first_6)
		update_with_mouse()


def txt_first_6():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img1), (0, 0))
		button_txt(110, 140, 630, 100, 'Одним приключением больше? Хорошо!', x_sh = 30, y_sh = 30, action = txt_first_61 )
		button_txt(110, 300, 630, 100, F1_1, x_sh = 30, y_sh = 30, action = txt_first_62 )
		print_text(F1_2, 140, 360, font_col = text_col)
		update_with_mouse()


def txt_first_61():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img1), (0, 0))
		app.blit(kompon_img3, (450, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30)
		print_text("Вот и хорошо,", 70, 340, font_col = text_col)
		print_text(F1_3, 70, 370, font_col = text_col)

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_second, back_1=back_img1, back_2=back_img2)
		update_with_mouse()


def txt_first_62():
	global score_win
	global score_answer 
	global score_decor
	sound_moon.stop()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		score_win = 0
		score_answer = 0
		score_decor - 0

		app.blit(trans(back_img1), (0, 0))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста 
		print_text(F2_1, 70, 340, font_col = text_col)
		print_text(F2_2, 70, 370, font_col = text_col)
		button_Next(670, 460, 120, 40, 'КОНЕЦ', x_sh = 15, y_sh = 15, action = the_end)
		update_with_mouse()


def txt_second():
	is_ready = False
	x = -860
	y = 10
	
	sound_moon.stop()
	sound_forest.set_volume(0.5)
	sound_forest.play()
	sound_fly.set_volume(0.1)
	sound_fly.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img2), (0, 0))
		if x < 50:
			x += 2
		else:
			is_ready = True
			sound_fly.stop()
		app.blit(kompon_img6, (x, y))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(B1_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(B1_2, 70, 370, font_col = text_col)
		if is_ready is True:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_second_1)
		update_with_mouse()                                         


def txt_second_1():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img2), (0, 0))
		app.blit(kompon_img7, (50, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(B2_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(B2_2, 70, 370, font_col = text_col) #Выведет сам текст сюжета
		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_second_2)

		update_with_mouse()


def txt_second_2():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img2), (0, 0))
		app.blit(kompon_img3, (70, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text(B3_1, 70, 340, font_col = text_col) 
		print_text(B3_2, 70, 370, font_col = text_col)

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_second_3)
		update_with_mouse()


def txt_second_3():

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
				
		app.blit(trans(back_img2), (0, 0))
		button_txt(110, 140, 630, 100, F3_1, x_sh = 30, y_sh = 30, action = txt_second_31)
		print_text(F3_2, 140, 200, font_col = text_col)
		button_txt(110, 300, 630, 100, 'Неплохая идея, почему бы и нет.', x_sh = 30, y_sh = 30, action = txt_second_32)
			
		update_with_mouse()


def txt_second_31():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img2), (0, 0))
		app.blit(kompon_img2, (450, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(F4_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(F4_2, 70, 370, font_col = text_col) #Выведет сам текст сюжета

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fifth_0, back_1=back_img2, back_2=back_img6)
		update_with_mouse()


def txt_second_32():
	global score_win
	
	is_ready = False
	x = 450
	y = 10
	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img2), (0, 0))
		app.blit(kompon_img3, (x, y))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30)
		print_text("Ура, а то уже сил идти нету.", 70, 340, font_col = text_col)
		score_win = 5
		if x > -460:
			x -= 3
		else:
			is_ready = True
		if is_ready == True:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_third, back_1=back_img2, back_2=back_img3)
		update_with_mouse()


def txt_third():
	
	is_ready = False
	x = W
	y = 10
	
	sound_river.set_volume(0.1)
	sound_river.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img3), (0, 0))
		app.blit(kompon_img7, (x, y))
		if x > 400:
			x -= 4
		else:
			is_ready = True
			app.blit(trans(back_img3), (0, 0))
			app.blit(kompon_img2, (x, y))
			pygame.draw.rect(app, window_col, (50, 310, 760, 200)) 
			pygame.draw.rect(app, name_window, (90, 290, 150, 20)) 
			print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) 
			print_text(C1_1, 70, 340, font_col = text_col) 
		if is_ready is True:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_third_1)
		update_with_mouse()
		clock.tick(FPS)


def txt_third_1():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		sound_forest.stop()
		app.blit(trans(back_img3), (0, 0))
		app.blit(kompon_img1, (450, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(C2_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(C2_2, 70, 370, font_col = text_col)
		print_text(C2_3, 70, 400, font_col = text_col)

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_third_2)
		update_with_mouse()


def txt_third_2():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img3), (0, 0))
		app.blit(kompon_img6, (450, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text(C3_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_third_3)
		update_with_mouse()


def txt_third_3():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img33), (0, 0))
		app.blit(kompon_img7, (450, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(C4_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_third_4)
		update_with_mouse()


def txt_third_4():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img33), (0, 0))
		app.blit(kompon_img5, (400, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(C5_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_third_5)
		update_with_mouse()


def txt_third_5():
	
	is_ready = False
	x = 400
	y = 10
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img33), (0, 0))
		app.blit(kompon_img5, (x, y))
		if x > -860:
			x -= 8
		else:
			is_ready = True
			app.blit(trans(back_img33), (0, 0))
		if is_ready == True:
			button_txt(110, 140, 630, 100, 'Ваааа, бежиииим!!!', x_sh = 30, y_sh = 30, action = txt_third_52 )
			button_txt(110, 300, 630, 100, F5_1, x_sh = 30, y_sh = 30, action = txt_third_51 )
			print_text(F5_2, 170, 360, font_col = text_col)
		update_with_mouse()


def txt_third_51():
	is_ready = False
	x = 860
	y = 10
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img2), (0, 0))
		sound_changing.set_volume(0.1)
		sound_changing.play()
		if x > 50:
			x -= 6
		else:
			is_ready = True
		app.blit(trans(back_img3), (0, 0))
		app.blit(wolf_img1, (x, y))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_unknown, 120, 290, font_col = name_col, font_size= 30)
		print_text(F6_1, 70, 340, font_col = text_col)
		print_text(F6_2, 70, 370, font_col = text_col)
		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_third_6)
		update_with_mouse()


def txt_third_52():
	global score_win
	global score_answer 
	global score_decor
	is_ready = False
	x = 860
	y = 10
	sigh = 3
	sound_roar.set_volume(0.1)
	sound_roar.play()
	pygame.time.delay(2000)
	sound_roar.stop()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img2), (0, 0))
		if x > 150:
			x -= 15
			y -= sigh
			sigh *= -1
		else:
			is_ready = True
		score_win = 0
		score_answer = 0
		score_decor - 0
		app.blit(trans(back_img3), (0, 0))
		app.blit(wolf_img2, (x, y))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста 
		print_text(F7_1, 70, 340, font_col = text_col)
		print_text(F7_2, 70, 370, font_col = text_col)

		button_Next(670, 460, 120, 40, 'КОНЕЦ', x_sh = 15, y_sh = 15, action = the_end)
		update_with_mouse()


def txt_third_6():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img3), (0, 0))
		app.blit(wolf_img4, (50, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_unknown, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(C6_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(C6_2, 70, 370, font_col = text_col) #Выведет сам текст сюжета
		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_third_7)
		update_with_mouse()


def txt_third_8():
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img3), (0, 0))
		button_txt(110, 140, 630, 100, '...', x_sh = 30, y_sh = 30, action = txt_third_9)
		button_txt(110, 300, 630, 100, 'М-да...', x_sh = 30, y_sh = 30, action = txt_third_9)
		update_with_mouse()


def txt_third_7():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img3), (0, 0))
		app.blit(wolf_img3, (50, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_unknown, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(C7_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(C7_2, 70, 370, font_col = text_col)
		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_third_8)
		update_with_mouse()


def txt_third_9():
	
	is_ready = False
	x = 860
	y = 10
	sigh = 3
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img3), (0, 0))
		app.blit(kompon_img1, (x, y))
		if x > 450:
			x -= 2
			y -= sigh
			sigh *= -1
		else:
			is_ready = True
		app.blit(wolf_img3, (50, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(C8_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		if is_ready == True:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_third_10)
		update_with_mouse()


def txt_third_10():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        app.blit(trans(back_img3), (0, 0))
        app.blit(wolf_img5, (50, 10))#Всавить спрайт персонажа
        app.blit(kompon_img2, (450, 10))
        pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
        pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
        print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
        print_text(C9_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
        print_text(C9_2, 70, 370, font_col = text_col) #Выведет сам текст сюжета

        button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fourth, back_1 = back_img3, back_2= back_img4)
        update_with_mouse()


def txt_fourth():
	
	is_ready = False
	x_komp = -700
	x_wolf = -460
	y = 10
	sigh = 3
	
	sound_river.stop()
	sound_forest.set_volume(0.2)
	sound_forest.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img4), (0, 0))
		app.blit(kompon_img6, (x_komp, y))
		app.blit(wolf_img3, (x_wolf, y))
		if x_wolf < 450:
			x_komp += 4
			x_wolf += 5
		else:
			is_ready = True
		if is_ready == True:
			pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
			pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
			print_text(chr_2name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
			print_text(D1_1.format(usr_name), 70, 340, font_col = text_col) #Выведет сам текст сюжета
			print_text(D1_2, 70, 370, font_col = text_col)
			
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fourth_1)
		update_with_mouse()  


def txt_fourth_1():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
				
		app.blit(trans(back_img4), (0, 0))
		button_txt(110, 140, 630, 100, F8_3, x_sh = 30, y_sh = 30, action = txt_fourth_12)
		print_text(F8_4, 140, 200, font_col = text_col)
		button_txt(110, 300, 630, 100, F8_1, x_sh = 30, y_sh = 30, action = txt_fourth_2,back_1= back_img4, back_2= back_img5)
		print_text(F8_2, 170, 360, font_col = text_col)
		
		update_with_mouse()

def txt_fourth_2():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		sound_search.set_volume(0.2)
		sound_search.play()
		app.blit(trans(back_img5), (0, 0))
		app.blit(wolf_img4, (450, 10))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) 
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) 
		print_text(chr_2name, 120, 290, font_col = name_col, font_size= 30)
		print_text(D2_1, 70, 340, font_col = text_col) 

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fourth_3)
		update_with_mouse()      


def txt_fourth_3():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		sound_search.stop()
		app.blit(trans(back_img5), (0, 0))
		pygame.draw.rect(app, window_col, (60, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, (0, 130, 180), (340, 20, 320, 320))
		app.blit(weapon_img3, (350, 15))
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_2name, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text("Нашёл. Эмм, ожерелье?", 70, 340, font_col = text_col) #Выведет сам текст сюжета

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fourth_4)
		update_with_mouse()


def txt_fourth_4():
	global score_decor
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			
		app.blit(trans(back_img5), (0, 0))
		app.blit(wolf_img3, (450, 10))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_2name, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text(D3_1, 70, 340, font_col = text_col)
		print_text(D3_2, 70, 370, font_col = text_col) 
		print_text(D3_3, 70, 400, font_col = text_col)  #Выведет сам текст сюжета
		score_decor += 1

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fifth_0, back_1= back_img5, back_2= back_img6)
		update_with_mouse()


def txt_fourth_12():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img4), (0, 0))
		app.blit(kompon_img2, (50, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(D4_1.format(usr_name), 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(D4_2, 70, 370, font_col = text_col) 

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fifth_0, back_1= back_img4, back_2= back_img6)
		update_with_mouse()


def txt_fifth_0():
	is_ready = False
	x = -860
	y = 10
	
	sound_forest.stop()
	sound_before.set_volume(0.2)
	sound_before.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img6), (0, 0))
		app.blit(kompon_img4, (x, y))

		if x < 500:
			x += 4
		else:
			is_ready = True

		if is_ready == True:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fifth)
		update_with_mouse()


def txt_fifth():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img6), (0, 0))
		app.blit(kompon_img3, (500, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(E1_1, 70, 340, font_col = text_col)
		print_text(E1_2, 70, 370, font_col = text_col)
		print_text(E1_3, 70, 400, font_col = text_col) #Выведет сам текст сюжета

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fifth_1)

		update_with_mouse()  


def txt_fifth_1():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			
		app.blit(trans(back_img6), (0, 0))
		button_txt(110, 140, 630, 100, F9_1, x_sh = 30, y_sh = 30, action = txt_fifth_11)
		print_text(F9_2, 140, 200, font_col = text_col)
		button_txt(110, 300, 630, 100, F9_3, x_sh = 30, y_sh = 30, action = txt_fifth_12)
		print_text(F9_4, 140, 360, font_col = text_col)
			
		update_with_mouse()     


def txt_fifth_12():
	global score_win
	is_ready = False
	x = 860
	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		if score_win == 5:
			app.blit(trans(back_img6), (0, 0))
			app.blit(wolf_img3, (x, 10))

			if x > 450:
				x -= 4
			else:
				is_ready = True
				pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
				pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
				print_text(chr_2name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
				print_text(H1_1, 70, 340, font_col = text_col) 
				print_text(H1_2, 70, 370, font_col = text_col) 
			if is_ready == True:
				button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_sixth, back_1=back_img6, back_2=back_img8)
			update_with_mouse()
		else:
			app.blit(trans(back_img6), (0, 0))
			app.blit(kompon_img4, (500, 10))#Всавить спрайт персонажа
			pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
			pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
			print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
			print_text("Ну ладно", 70, 340, font_col = text_col) #Выведет сам текст сюжета

			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_sixth, back_1=back_img6, back_2=back_img8)

			update_with_mouse()


def txt_fifth_11():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img6), (0, 0))
		app.blit(kompon_img3, (450, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30)
		print_text("Вот это настрой!", 70, 340, font_col = text_col)

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fifth_02, back_1=back_img6, back_2=back_img7)
		update_with_mouse()             


def txt_fifth_02():
	
	sound_before.stop()
	sound_noise.set_volume(0.1)
	sound_noise.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img7), (0, 0))
		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fifth_2)
		update_with_mouse()


def txt_fifth_2():
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img7), (0, 0))
		app.blit(dealer_img2, (50, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_tradesman, 120, 290, font_col = name_col, font_size= 30) #Выведет имя персонажа
		print_text(E2_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(E2_2, 70, 370, font_col = text_col)
		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fifth_3)

		update_with_mouse()


def txt_fifth_3():
	is_ready = False
	x = 860
	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img7), (0, 0))
		app.blit(kompon_img4, (x, 10))
		if x > 500:
			x -= 4
		else:
			is_ready = True
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text(E3_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(E3_2, 70, 370, font_col = text_col)
		print_text(E3_3, 70, 400, font_col = text_col)
		if is_ready == True:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fifth_4)
		update_with_mouse()


def txt_fifth_4():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			
		app.blit(trans(back_img7), (0, 0))
		button_txt(110, 140, 630, 100, H2_1, x_sh = 30, y_sh = 30, action = txt_fifth_41)
		print_text(H2_2, 140, 200, font_col = text_col)
		button_txt(110, 300, 630, 100, H3_1, x_sh = 30, y_sh = 30, action = txt_fifth_42)
		print_text(H3_2, 140, 360, font_col = text_col)
			
		update_with_mouse()


def txt_fifth_41():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img7), (0, 0))
		app.blit(dealer_img2, (50, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_tradesman, 120, 290, font_col = name_col, font_size= 30)
		print_text("A жаль, такую возможность упустили.", 70, 340, font_col = text_col) #Выведет сам текст сюжета

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_sixth, back_1=back_img7, back_2=back_img8)
		update_with_mouse()


def txt_fifth_42():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img7), (0, 0))
		app.blit(dealer_img2, (50, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_tradesman, 120, 290, font_col = name_col, font_size= 30)
		print_text(E4_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(E4_2, 70, 370, font_col = text_col)
		print_text(E4_3, 70, 400, font_col = text_col)


		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fifth_5)
		update_with_mouse()


def txt_fifth_5():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			
		app.blit(trans(back_img7), (0, 0))
		button_txt(110, 140, 630, 100, 'Вот тот мощный лук выглядит надёжно.', x_sh = 30, y_sh = 30, action = txt_fifth_6)
		button_txt(110, 300, 630, 100, H4_1, x_sh = 30, y_sh = 30, action = txt_fifth_8)
		print_text(H4_2, 140, 350, font_col = text_col)
		print_text(H4_3, 140, 380, font_col = text_col)

		update_with_mouse()


def txt_fifth_6():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img7), (0, 0))
		app.blit(dealer_img1, (50, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_tradesman, 120, 290, font_col = name_col, font_size= 30)
		print_text(E5_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(E5_2, 70, 370, font_col = text_col)
		print_text(E5_3, 70, 400, font_col = text_col)

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fifth_7)
		update_with_mouse()


def txt_fifth_7():
	global score_decor

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
				
		if score_decor > 0:
			app.blit(trans(back_img7), (0, 0))
			button_txt(110, 140, 630, 100, H5_1, x_sh = 30, y_sh = 30, action = txt_fifth_090)
			print_text(H5_2, 140, 190, font_col = text_col)
			print_text(H5_3, 140, 210, font_col = text_col)
			button_txt(110, 300, 630, 100, H5_4, x_sh = 30, y_sh = 30, action = txt_fifth_8)
			print_text(H5_5, 140, 350, font_col = text_col)
			update_with_mouse()     
		else:
			app.blit(trans(back_img7), (0, 0))
			button_txt(110, 140, 630, 100, '(...Тут мог быть другой вариант...)', x_sh = 30, y_sh = 30, action = txt_fifth_8)
			print_text('Может другое?', 140, 190, font_col = text_col)
			button_txt(110, 300, 630, 100, H5_4, x_sh = 30, y_sh = 30, action = txt_fifth_8)
			print_text(H5_5, 140, 350, font_col = text_col)
			update_with_mouse() 


def txt_fifth_8():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img7), (0, 0))
		app.blit(dealer_img2, (50, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_tradesman, 120, 290, font_col = name_col, font_size= 30)
		print_text(E6_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(E6_2, 70, 370, font_col = text_col)
		print_text(E6_3, 70, 400, font_col = text_col)

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_fifth_10)
		update_with_mouse()


def txt_fifth_10():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			
		app.blit(trans(back_img7), (0, 0))
		button_txt(110, 140, 630, 100, H6_1, x_sh = 30, y_sh = 30, action = txt_fifth_41)
		print_text(H6_2, 140, 200, font_col = text_col)
		
		button_txt(110, 300, 630, 100, 'Пожалуй я возьму его', x_sh = 30, y_sh = 30, action = txt_fifth_09)
			
		update_with_mouse()


def txt_fifth_090():
    global score_decor
    score_decor = 0
    action = txt_fifth_09()


def txt_fifth_09():
	global score_win
	score_win += 1
	action = txt_fifth_9()


def txt_fifth_9():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img7), (0, 0))
		app.blit(dealer_img1, (50, 10))#Всавить спрайт персонажа
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_tradesman, 120, 290, font_col = name_col, font_size= 30)
		print_text(E7_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_sixth, back_1=back_img7, back_2=back_img8)
		update_with_mouse()


def txt_sixth():
	is_ready = False
	x = -460
	
	sound_noise.stop()
	sound_before.stop()
	sound_around.set_volume(0.2)
	sound_around.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img8), (0, 0))
		app.blit(kompon_img3, (x, 10))
		if x < 150:
			x += 3
		else:
			is_ready = True
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text(E8_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(E8_2, 70, 370, font_col = text_col)
		print_text(E8_3, 70, 400, font_col = text_col)
		print_text(E8_4, 70, 430, font_col = text_col)
		print_text(E8_5, 70, 460, font_col = text_col)
		print_text(E8_6, 70, 490, font_col = text_col)
		if is_ready == True:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_sixth_0)
		update_with_mouse()


def txt_sixth_0():
	global score_win

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		if score_win > 4:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_sixth_11)
		else:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_sixth_1, back_1=back_img8, back_2=back_img9)
		update_with_mouse()


def txt_sixth_11():
	is_ready = False
	x = 860
	
	global score_win

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		if score_win > 4:
			app.blit(trans(back_img8), (0, 0))
			app.blit(wolf_img4, (x, 10))
			if x > 450:
				x -= 2
			else:
				is_ready = True
		app.blit(kompon_img7, (50, 10))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_2name, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text(E9_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(E9_2, 70, 370, font_col = text_col)
		if is_ready == True:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_sixth_12, back_1=back_img8, back_2=back_img9)
		update_with_mouse()


def txt_sixth_12():
	
	sound_around.stop()
	sound_cave_out.set_volume(0.1)
	sound_cave_out.play()
	is_ready = False
	x_komp = -700
	x_wolf = -460
	y = 10
	sigh = 3
	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img9), (0, 0))
		app.blit(kompon_img2, (x_komp, y))
		app.blit(wolf_img5, (x_wolf, y))
		if x_wolf < 450:
			x_komp += 4
			x_wolf += 5
		else:
			is_ready = True

		if is_ready == True:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_sixth_121,  back_1=back_img9, back_2=back_img10)
		update_with_mouse()


def txt_sixth_1():
	is_ready = False
	x = -460
	
	sound_around.stop()
	sound_cave_out.set_volume(0.1)
	sound_cave_out.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img9), (0, 0))
		app.blit(kompon_img6, (x, 10))
		if x < 540:
			x += 2
		else:
			is_ready = True
		if is_ready == True:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh, back_1=back_img9, back_2=back_img10)
		update_with_mouse()


def txt_sixth_121():
	global score_win
	sound_cave_out.stop()
	sound_cave_in.set_volume(0.3)
	sound_cave_in.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			
		app.blit(trans(back_img10), (0, 0))
		app.blit(kompon_img6, (70, 10))#Всавить спрайт персонажа
		app.blit(wolf_img3, (450, 10)) 
		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_1)
		update_with_mouse()


def txt_seventh():
	is_ready = False
	x = -400
	
	sound_cave_out.stop()
	sound_cave_in.set_volume(0.3)
	sound_cave_in.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img10), (0, 0))
		app.blit(kompon_img6, (x, 10))
		if x < 70:
			x += 4
		else:
			is_ready = True
		if is_ready == True:
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_2)
		update_with_mouse()


def txt_seventh_11():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img10), (0, 0))
		app.blit(wolf_img1, (450, 10))#Всавить спрайт персонажа
		app.blit(kompon_img7, (50, 10))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_1)
		update_with_mouse()


def txt_seventh_1():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			
		app.blit(trans(back_img10), (0, 0))
		app.blit(kompon_img7, (50, 10))
		app.blit(wolf_img3, (450, 10))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_2name, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text(G1_1, 70, 340, font_col = text_col) #Выведет сам текст 
		print_text(G1_2, 70, 370, font_col = text_col)

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_2)
		update_with_mouse()


def txt_seventh_2():
	global score_win
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		if score_win > 4:   
			app.blit(trans(back_img10), (0, 0))
			app.blit(kompon_img7, (50, 10))
			app.blit(wolf_img1, (450, 10))   
			pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
			pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
			print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
			print_text(G2_1.format(usr_name), 70, 340, font_col = text_col) #Выведет сам текст сюжета
			print_text(G2_2, 70, 370, font_col = text_col)
			print_text(G2_3, 70, 400, font_col = text_col)

			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_3)
			update_with_mouse()
		else:
			app.blit(trans(back_img10), (0, 0))
			app.blit(kompon_img7, (50, 10))
			pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
			pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
			print_text(chr_1name, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
			print_text(G2_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
			print_text(G2_2, 70, 370, font_col = text_col)
			print_text(G2_3, 70, 400, font_col = text_col)
			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_3)
			update_with_mouse()


def txt_seventh_3():
	global score_win
	sound_crawl.set_volume(0.1)
	sound_crawl.play()
	pygame.time.delay(4000)
	sound_crawl.stop()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		if score_win > 4:
			app.blit(trans(back_img10), (0, 0))
			app.blit(kompon_img6, (50, 10))
			app.blit(wolf_img1, (450, 10))
			pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
			pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
			print_text(chr_unknown, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
			print_text(G3_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета

			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_4)
			update_with_mouse()
		else:
			app.blit(trans(back_img10), (0, 0))
			app.blit(kompon_img6, (50, 10))
			pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
			pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
			print_text(chr_unknown, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
			print_text(G3_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета

			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_4)
			update_with_mouse()


def txt_seventh_4():
	global score_win
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			
		app.blit(trans(back_img10), (0, 0))
		app.blit(kompon_img5, (50, 10))
		if score_win > 4:
			app.blit(wolf_img2, (450, 10))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 150, 20)) #Окно для имени говорящего 
		print_text(chr_unknown, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text(G4_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(G4_2, 70, 370, font_col = text_col)

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_5)
		update_with_mouse()


def txt_seventh_5():
	is_ready = False
	x = 700
	y = 540
	
	sound_crawl.set_volume(0.1)
	sound_crawl.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img10), (0, 0))
		app.blit(snake_img1, (x, y))
		if x > 350:
			x -= 2
			y -= 3
		else:
			is_ready = True
			sound_crawl.stop()
		if is_ready == True:
			pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
			pygame.draw.rect(app, name_window, (90, 290, 250, 20)) #Окно для имени говорящего 
			print_text(chr_snake, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
			print_text(G5_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
			print_text(G5_2, 70, 370, font_col = text_col)

			button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_6)
		update_with_mouse()
		clock.tick(FPS)


def txt_seventh_7():
	sound_hs.set_volume(0.2)
	sound_hs.play()
	pygame.time.delay(2000)
	sound_hs.stop()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img10), (0, 0))
		app.blit(snake_img2, (305, 5))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 250, 20)) #Окно для имени говорящего 
		print_text(chr_snake, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text(G8_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_81)
		update_with_mouse()


def txt_seventh_81():
	global score_win

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		if score_win > 0:
			action =  txt_seventh_end()
		else:
			action = txt_seventh_death()


def txt_seventh_8():
	global score_decor

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		if score_decor > 0:
			app.blit(trans(back_img10), (0, 0))
			button_txt(110, 140, 630, 100, H7_1, x_sh = 30, y_sh = 30, action = txt_seventh_71)
			print_text(H7_2, 140, 200, font_col = text_col)
			button_txt(110, 300, 630, 100, H7_6, x_sh = 30, y_sh = 30, action = txt_seventh_7)
			print_text(H7_7, 140, 360, font_col = text_col)
			update_with_mouse()
		elif score_decor == 0:
			app.blit(trans(back_img10), (0, 0))
			button_txt(110, 140, 630, 100, H7_3, x_sh = 30, y_sh = 30, action = txt_seventh_7)
			print_text(H7_4, 140, 190, font_col = text_col)
			print_text(H7_5, 140, 210, font_col = text_col)
			button_txt(110, 300, 630, 100, H7_6, x_sh = 30, y_sh = 30, action = txt_seventh_7)
			print_text(H7_7, 140, 360, font_col = text_col) 
			update_with_mouse() 


def txt_seventh_71():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			
		app.blit(trans(back_img10), (0, 0))
		app.blit(snake_img3, (305, 5))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 250, 20)) #Окно для имени говорящего 
		print_text(chr_snake, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text(G6_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(G6_2, 70, 370, font_col = text_col)
		print_text(G6_3, 70, 400, font_col = text_col)
		print_text(G6_4, 70, 430, font_col = text_col)

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_72)
		update_with_mouse()


def txt_seventh_72():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		sound_cave_in.stop()
		sound_miracle.set_volume(0.1)
		sound_miracle.play()
		app.blit(trans(back_img11), (0, 0))
		app.blit(snake_img4, (305, 5))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста
		pygame.draw.rect(app, name_window, (90, 290, 250, 20)) #Окно для имени говорящего 
		print_text(chr_snake, 120, 290, font_col = name_col, font_size= 30)  #Выведет имя персонажа
		print_text(G7_1, 70, 340, font_col = text_col) #Выведет сам текст сюжета
		print_text(G7_2, 70, 370, font_col = text_col)
		print_text(G7_3, 70, 400, font_col = text_col)
		print_text(G7_4, 70, 430, font_col = text_col)
		print_text(G7_5, 70, 460, font_col = text_col)

		button_Next(670, 460, 120, 40, 'Дальше', x_sh = 15, y_sh = 15, action = txt_seventh_999)
		update_with_mouse()


def txt_seventh_6():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			
		app.blit(trans(back_img10), (0, 0))
		button_txt(110, 140, 630, 100, 'Я просто хочу попасть домой,', x_sh = 30, y_sh = 30, action = txt_seventh_8)
		print_text('не хочу что бы кто-то пострадал.', 140, 190, font_col = text_col)
		button_txt(110, 300, 630, 100, 'Если мне для того, чтобы попасть домой ', x_sh = 30, y_sh = 30, action = txt_seventh_7)
		print_text('потребуется сразить тебя, то я сделаю это!', 140, 350, font_col = text_col)
			
		update_with_mouse()


def txt_seventh_end():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img10), (0, 0))
		button_txt(110, 140, 630, 100, 'Я вернусь домой любой ценой! Аaaa!!', x_sh = 30, y_sh = 30, action = txt_seventh_9)
		button_txt(110, 300, 630, 100, 'Ты падёшь от моего оружия!!!', x_sh = 30, y_sh = 30, action = txt_seventh_9)	
		update_with_mouse()


def txt_seventh_death():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(back_img10), (0, 0))
		button_txt(110, 140, 630, 100, 'ААААААААА!!!', x_sh = 30, y_sh = 30, action = txt_seventh_99)
		button_txt(110, 300, 630, 100, 'Я ВЫБИРУСЬ ОТ СЮДА!!!', x_sh = 30, y_sh = 30, action = txt_seventh_99)
		update_with_mouse()


def txt_seventh_99():
	global score_win
	global score_answer 
	global score_decor
	sound_death.set_volume(0.1)
	sound_death.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		app.blit(trans(black_img), (0, 0))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста 
		print_text(I1_1, 70, 340, font_col = text_col)
		print_text(I1_2, 70, 370, font_col = text_col)
		score_win = 0
		score_answer = 0
		score_decor = 0
		button_Next(670, 460, 120, 40, 'КОНЕЦ', x_sh = 15, y_sh = 15, action = the_end)
		update_with_mouse()


def txt_seventh_9():
	global score_win
	global score_answer 
	global score_decor
	sound_death.set_volume(0.1)
	sound_death.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img10), (0, 0))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста 
		print_text(I2_1, 70, 340, font_col = text_col)
		print_text(I2_2, 70, 370, font_col = text_col)
		score_win = 0
		score_answer = 0
		score_decor = 0

		button_Next(670, 460, 120, 40, 'КОНЕЦ', x_sh = 15, y_sh = 15, action = the_end)
		update_with_mouse()


def txt_seventh_999():
	global score_win
	global score_answer 
	global score_decor

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		
		app.blit(trans(back_img11), (0, 0))
		pygame.draw.rect(app, window_col, (50, 310, 760, 200)) #Окно для текста 
		print_text(I3_1, 70, 340, font_col = text_col)
		print_text(I3_2, 70, 370, font_col = text_col)
		print_text(I3_3, 70, 400, font_col = text_col)
		score_win = 0
		score_answer = 0
		score_decor - 0

		button_Next(670, 460, 120, 40, 'Молодец!', x_sh = 15, y_sh = 15, action=the_end(back_img11))
		update_with_mouse()


def which_answers1(answer):
	
	if answer % 2 == 0:
		pygame.draw.rect(app, window_col, (20, 220, 700, 200))
		pygame.draw.rect(app, window_col, (30, 220, 150, 20))
		app.blit(app, character_img, (780, 350))
		print_text("Ура, а то я немного утомился.", 30, 210, font_col = text_col)
		print_text(chr_1name, 32, 217, font_col = name_col, font_size= 30)
		score_answer = 2
	elif answer % 3 == 0:
		pygame.draw.rect(app, window_col, (20, 220, 700, 200))
		pygame.draw.rect(app, window_col, (30, 220, 150, 20))
		app.blit(app, character_img, (780, 350))
		print_text("И вправду, лучше держатся пути, а то вдруг что-нибудь произойдёт.", 30, 210, font_col = text_col)
		print_text(chr_1name, 32, 217, font_col = name_col, font_size= 30)
		score_answer = 3
	
	update_with_mouse()


def first_loc():
	
	sound_moon.set_volume(0.3)
	sound_moon.play()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img1), (0, 0))
		#black_change(img1 = back_img11, img2 = back_img1)# Переход...

		mouse = pygame.mouse.get_pos()
		current_time = int(time.time() - star_time)
		if current_time >= 2:
			button_txt(110, 140, 630, 100, 'Какая большая поляна, красиво….', x_sh = 30, y_sh = 30, action = txt_first)
			print_text('Стоп, а как я тут оказался?', 140, 200)
			button_txt(110, 300, 630, 100, 'Почему здесь так темно?', x_sh = 30, y_sh = 30, action = txt_first)
		
		
		#вставить второе перепутье по логике первой главы.
		update_with_mouse()
		clock.tick(FPS)


#Сама кнопка
def button_txt(x, y, w, h, mes, f_size = 30, x_sh =25, y_sh = 25, action = None, back_1=None, back_2=None):
	global score_usr
	mouse = pygame.mouse.get_pos()
	clicked = pygame.mouse.get_pressed()

	if x < mouse[0] < x + w and y < mouse[1] < y + h:
		pygame.draw.rect(app, col_in, (x, y, w, h))
		if action is not None and clicked[0] == 1:
			pygame.time.delay(250)
			score_usr += 1
			if back_1 and back_2:
				black(back_1, back_2)
			action()
	else:
		pygame.draw.rect(app, col_out, (x, y, w, h))
	
	print_text(mes, x + x_sh, y + y_sh, font_size = f_size)

#Кнопка для перехода к следующему/действию вопросу/локации(для смены)
def button_Next(x , y, w, h, mes, f_size=30, x_sh=15, y_sh=15, action=None, back_1=None, back_2=None):
	global score_usr

	mouse = pygame.mouse.get_pos()
	clicked = pygame.mouse.get_pressed()
	
	if x < mouse[0] < x + w and y < mouse[1] < y + h:
		pygame.draw.rect(app, next_in, (x, y, w, h))
		if action is not None and clicked[0] == 1:
			pygame.time.delay(250)
			score_usr += 1
			if back_1 and back_2:
				black(back_1, back_2)
			action()
	else:
		pygame.draw.rect(app, next_out, (x, y, w, h))

	print_text(mes, x + x_sh, y + y_sh, font_size = f_size)


def print_text(mes, x, y, font_col = (0, 0, 0), font_type = None, font_size = 30):
	font = pygame.font.Font(font_type, font_size)
	text_surface = font.render(mes, True, font_col)
	app.blit(text_surface, (x, y))

#Для смены локации
def black(back_1, back_2):
	x = -W
	speed = 10

	while True:
		x += speed
		if x > W:
			return 
		
		if x < 0:
			app.blit(trans(back_1), (0, 0))
		else:
			app.blit(trans(back_2), (0, 0))
		
		app.blit(trans(black_img), (x, 0))
		update_with_mouse()


def usr_name_input():
	global usr_name
	need_input	= True
	usr_name	= ''

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if need_input and event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					need_input = False
					first_loc()
				elif event.key == pygame.K_BACKSPACE:
					usr_name = usr_name[:-1]
				else:
					if len(usr_name) < 10:
						usr_name += event.unicode

		app.blit(back_img1, (0, 0))

		print_text('Пожалуйста, введи свой ник (Не более 10 знаков)', 180, 200, font_size=30, font_col=col_out)
		print_text('После нажми на ENTER', W // 3, 250, font_size=30, font_col=col_out)

		button_txt(300, 300, 200, 70, usr_name, x_sh=30, y_sh=30)
		button_txt(330, 400, 140, 70, 'ВЫХОД', x_sh=30, y_sh=30, action=exit)

		update_with_mouse()
		clock.tick(FPS // 2)


def enter_name():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img1), (0,0))
		usr_name_input()
		button_txt(300, 200, 220, 150, 'ВЫХОД', x_sh = 30, y_sh = 30, action = exit)
		update_with_mouse()
		clock.tick(FPS)


def menu():
	global score_usr

	score_usr = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back_img11), (0,0))
		button_txt(100, 200, 200, 150, 'НАЧАТЬ', x_sh = 30, y_sh = 30, action=enter_name, back_1=back_img11, back_2=back_img1)
		button_txt(300, 200, 220, 150, 'ВЫХОД', x_sh = 30, y_sh = 30, action = exit)
		update_with_mouse()
		clock.tick(FPS)


def the_end(back=back_img1):
	data.insert_into(usr_name, score_usr)
	sound_miracle.stop()
	sound_cave_in.stop()
	sound_moon.stop()
	sound_river.stop()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(trans(back), (0,0))
		if back == back_img1:
			print_text(f'{usr_name}, Ваши баллы: {score_usr}', 200, 300, font_size=50, font_col=col_out)
		else:
    		 
			print_text(f'{usr_name}, ты набрал {score_usr}', 300, 350, font_size=50, font_col=col_out)
		button_txt(650, 460, 120, 40, 'К МЕНЮ', x_sh = 15, y_sh = 15, action = menu)
		button_txt(200, 460, 120, 40, 'ТОП', x_sh = 15, y_sh = 15, action = show_list)

		update_with_mouse()


def show_list():
	global data

	list_data	= sorted(data.select_all(), key=lambda x: -x[1])[:5]
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

		app.blit(back_img1, (0, 0))

		print_text(f'Топ игроков', 300, 100, font_size=50, font_col=col_out)

		for i in range(len(list_data)):
			button_txt(W // 7 + W // 25 + 80, H // 3 + i * H // 10 - 50,\
				W // 5, H // 9, list_data[i][0], x_sh=30, y_sh=20)
			button_txt(W // 7 + W // 25 + 250, H // 3 + i * H // 10 - 50,\
				W // 5, H // 9, str(list_data[i][1]), x_sh=30, y_sh=20)
		
		button_txt(500, 450, 140, 45, 'МЕНЮ', x_sh = 30, y_sh = 20, action=menu)
		button_txt(200, 450, 140, 45, 'ВЫХОД', x_sh = 30, y_sh = 20, action=exit)

		update_with_mouse()
		clock.tick(FPS // 2)


data = Storage()
menu()