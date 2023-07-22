import pygame
import tools
import math

pygame.init()
clock = pygame.time.Clock()
height = 664
width = 996
screen = pygame.display.set_mode((width, height))
# pygame window name
pygame.display.set_caption('Pick Your Meal')

# window icon
icon = pygame.image.load('images/tray.png')
pygame.display.set_icon(icon)

# music area
pygame.mixer.music.load('resources/bgm.ogg')
pygame.mixer.music.play(loops=-1)
clickbutton = pygame.mixer.Sound('resources/clickbutton.mp3')
femalehello = pygame.mixer.Sound('resources/femalehello.mp3')
malehello = pygame.mixer.Sound('resources/malehello.mp3')
backbutton = pygame.mixer.Sound('resources/backbutton.mp3')
nextbutton = pygame.mixer.Sound('resources/nextbutton.mp3')
kaching = pygame.mixer.Sound('resources/kaching.mp3')

# GAME VARIABLES
page_state = "budget"

# FONTS
font = pygame.font.Font("resources/NanumPenScript.ttf", 40)
font_cute = pygame.font.Font("resources/CherryBombOne.ttf", 50)
font_cute1 = pygame.font.Font("resources/CherryBombOne.ttf", 33)
font_cute2 = pygame.font.Font("resources/CherryBombOne.ttf", 27)
text_font = pygame.font.SysFont("Arial", 30)

# DEFINE COLOURS
TEXT_COL = (255, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (156, 156, 156)
BROWN = (139, 69, 19)
PEACH = (188, 143, 143)


# TOOLS
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# /// ------------------------ VARIABLES -----------------------///
textstatus = False
textstatus2 = False
textstatus3 = False
textstatus4 = False
textstatus5 = False
textstatus6 = False

ts1 = False
ts2 = False
ts3 = False
ts4 = False
ts5 = False
ts6 = False

t1 = False
t2 = False
t3 = False
t4 = False
t5 = False
t6 = False

bg_img = pygame.image.load('images/background1.jpg').convert_alpha()
tray_img = pygame.image.load('images/tray.png').convert_alpha()
bg_map = pygame.image.load('images/map.png').convert_alpha()
starbee_img = pygame.image.load('images/starbee.png').convert_alpha()
htc_img = pygame.image.load('images/htc.png').convert_alpha()
bakery_img = pygame.image.load('images/bakery.png').convert_alpha()
gamebg_img = pygame.image.load('images/gamebg.png').convert_alpha()
onigiri_img = pygame.image.load('images/onigiri.png').convert_alpha()
croissant_img = pygame.image.load('images/croissant.png').convert_alpha()
donut_img = pygame.image.load('images/doughnut.png').convert_alpha()
muffin_img = pygame.image.load('images/muffin.png').convert_alpha()
burger_img = pygame.image.load('images/burger.png').convert_alpha()
watermelon_img = pygame.image.load('images/watermelon.png').convert_alpha()
maintable_img = pygame.image.load('images/maintable.png').convert_alpha()
table1_img = pygame.image.load('images/table1.png').convert_alpha()
table2_img = pygame.image.load('images/table2.png').convert_alpha()
table3_img = pygame.image.load('images/table3.png').convert_alpha()
table4_img = pygame.image.load('images/table4.png').convert_alpha()
table5_img = pygame.image.load('images/table5.png').convert_alpha()
table6_img = pygame.image.load('images/table6.png').convert_alpha()
walldecor_img = pygame.image.load('images/walldecor.png').convert_alpha()
walldecor2_img = pygame.image.load('images/walldecor2.png').convert_alpha()
wardrobe_img = pygame.image.load('images/wardrobe.png').convert_alpha()
wardrobe2_img = pygame.image.load('images/wardrobe2.png').convert_alpha()
curtain_img = pygame.image.load('images/curtain.png').convert_alpha()
fridge_img = pygame.image.load('images/fridge.png').convert_alpha()
budget_img = pygame.image.load('images/budget.png').convert_alpha()
coin_img = pygame.image.load('images/coin.png').convert_alpha()
homebutton_img = pygame.image.load('images/home_button.png').convert_alpha()
playbutton_img = pygame.image.load('images/play_button.png').convert_alpha()
closebutton_img = pygame.image.load('images/close_button.png').convert_alpha()
letter_img = pygame.image.load('images/letter.png').convert_alpha()
kopi_img = pygame.image.load('images/kopi.png').convert_alpha()
tehtarik_img = pygame.image.load('images/tehtarik.png').convert_alpha()
maggigoreng_img = pygame.image.load('images/maggigoreng.png').convert_alpha()
nasigoreng_img = pygame.image.load('images/nasigoreng.png').convert_alpha()
icecream_img = pygame.image.load('images/icecream.png').convert_alpha()
roticanai_img = pygame.image.load('images/roticanai.png').convert_alpha()
kebab_img = pygame.image.load('images/kebab.png').convert_alpha()
bao_img = pygame.image.load('images/bao.png').convert_alpha()
spaggheti_img = pygame.image.load('images/spaggheti.png').convert_alpha()
nasilemak_img = pygame.image.load('images/nasilemak.png').convert_alpha()
shavedice_img = pygame.image.load('images/shavedice.png').convert_alpha()
yeemee_img = pygame.image.load('images/yeemee.png').convert_alpha()
button_img = pygame.image.load('images/button.png').convert_alpha()
pricetag_img = pygame.image.load('images/pricetag.png').convert_alpha()
clearbutton_img = pygame.image.load('images/clear_button.png').convert_alpha()
backbutton_img = pygame.image.load('images/back_button.png').convert_alpha()
eatbutton_img = pygame.image.load('images/eatbutton.png').convert_alpha()
piechartbg_img = pygame.image.load('images/piechartbg.png').convert_alpha()
finalbg_img = pygame.image.load('images/finalbg.png').convert_alpha()
insuf_img = pygame.image.load('images/insuf.png').convert_alpha()

# /// JOEY ///
mute_img = pygame.image.load("images/mute.png").convert_alpha()
unmute_img = pygame.image.load("images/unmute.png").convert_alpha()
start_img = pygame.image.load("images/start.png").convert_alpha()
next_img = pygame.image.load("images/next.png").convert_alpha()
quit_img = pygame.image.load("images/exit.png").convert_alpha()
male_img = pygame.image.load("images/button_male.png").convert_alpha()
female_img = pygame.image.load("images/button_female.png").convert_alpha()
back_img = pygame.image.load("images/back.png").convert_alpha()
background_img = pygame.image.load("images/background.jpg").convert_alpha()
fats_img = pygame.image.load("images/fats.png").convert_alpha()
carbs_img = pygame.image.load("images/carbs.png").convert_alpha()
protein_img = pygame.image.load("images/protein.png").convert_alpha()

# ------------------------------ IMAGE INSTANCES -------------------------------------
# ///JOEY
mute_button = tools.Button(100, 20, mute_img, 0.19)
unmute_button = tools.Button(20, 20, unmute_img, 0.75)
mute_button1 = tools.Button(225, 22, mute_img, 0.22)
unmute_button1 = tools.Button(130, 22, unmute_img, 0.86)
mute_button2 = tools.Button(225, 560, mute_img, 0.22)
unmute_button2 = tools.Button(130, 560, unmute_img, 0.86)
start_button = tools.Button(370, 330, start_img, 0.7)
next_button2 = tools.Button(550, 350, next_img, 0.5)
next_button3 = tools.Button(550, 420, next_img, 0.5)
next_button4 = tools.Button(550, 350, next_img, 0.5)
back_button1 = tools.Button(200, 350, back_img, 0.6)
back_button2 = tools.Button(380, 400, back_img, 0.6)
back_button3 = tools.Button(200, 420, back_img, 0.6)
back_button4 = tools.Button(200, 350, back_img, 0.6)
quit_button = tools.Button(390, 400, quit_img, 0.5)
male_button = tools.Button(250, 230, male_img, 0.3)
female_button = tools.Button(550, 230, female_img, 0.3)
nametext = font_cute.render('Enter your NAME ', True, BROWN)
nametext2 = font.render('Remember to enter your name !!', True, BLACK)
gendertext = 'Please click your gender'
weighttext = 'Let\'s check your body measurements'
budgettext = 'Please enter your BUDGET '

# -----------------------------------
background = tools.ImageDraw(0, 0, background_img, 1)
input_box1 = pygame.Rect(350, 250, 300, 60)
input_box2 = pygame.Rect(350, 250, 300, 60)
input_box3 = pygame.Rect(350, 330, 300, 60)
input_box4 = pygame.Rect(350, 250, 300, 60)
name = ""
active1 = False
active2 = False
active3 = False
active4 = False
gender = ''
weight = ''
height = ''
budgetvalue = ''

# ///AMBER
map = tools.ImageDraw(0, 0, bg_map, 0.527)
bg = tools.ImageDraw(0, 0, bg_img, 1.12)
tray = tools.Button(280, 100, tray_img, 0.9)
starbee = tools.Button(295, 105, starbee_img, 0.135)
htc = tools.Button(755, 10, htc_img, 0.22)
bakery = tools.Button(-10, 30, bakery_img, 0.17)
gamebg = tools.ImageDraw(0, 0, gamebg_img, 0.8)
maintable = tools.ImageDraw(330, 245, maintable_img, 1.55)
b_table1 = tools.ImageDraw(30, 220, table1_img, 0.5)
b_table2 = tools.ImageDraw(30, 325, table2_img, 0.5)
b_table3 = tools.ImageDraw(30, 440, table3_img, 0.5)
b_table4 = tools.ImageDraw(175, 220, table4_img, 0.5)
b_table5 = tools.ImageDraw(175, 325, table5_img, 0.5)
b_table6 = tools.ImageDraw(175, 440, table6_img, 0.5)
walldecor = tools.ImageDraw(290, 30, walldecor_img, 0.35)
walldecor2 = tools.ImageDraw(15, 50, walldecor2_img, 0.35)
wardrobe = tools.ImageDraw(635, 50, wardrobe_img, 0.38)
wardrobe2 = tools.ImageDraw(270, 95, wardrobe2_img, 0.3)
curtain = tools.ImageDraw(490, 30, curtain_img, 0.6)
fridge = tools.ImageDraw(810, -130, fridge_img, 0.6)
budget = tools.ImageDraw(40, 545, budget_img, 0.20)
coin = tools.ImageDraw(66, 580, coin_img, 0.04)

homebutton = tools.Button(30, 20, homebutton_img, 0.35)
back = tools.Button(35, 558, backbutton_img, 0.22)
playbutton = tools.Button(0, 0, playbutton_img, 1)
closebutton = tools.Button(650, 80, closebutton_img, 0.3)
button = tools.Button(395, 520, button_img, 0.65)
eatbutton = tools.Button(785, 560, eatbutton_img, 0.66)

letter = tools.ImageDraw(250, 50, letter_img, 0.55)
pricetag = tools.ImageDraw(550, 300, pricetag_img, 0.5)
piechartbg = tools.ImageDraw(770, 70, piechartbg_img, 1.07)
finalbg = tools.ImageDraw(0, 210, finalbg_img, 1.45)

onigiri = tools.Button(58, 215, onigiri_img, 0.7)
croissant = tools.Button(58, 325, croissant_img, 0.65)
donut = tools.Button(58, 440, donut_img, 0.7)
muffin = tools.Button(205, 200, muffin_img, 0.7)
burger = tools.Button(203, 320, burger_img, 0.7)
watermelon = tools.Button(195, 420, watermelon_img, 0.7)

kopi = tools.Button(69, 210, kopi_img, 0.5)
tehtarik = tools.Button(73, 310, tehtarik_img, 0.6)
maggigoreng = tools.Button(51, 440, maggigoreng_img, 0.45)
nasigoreng = tools.Button(205, 220, nasigoreng_img, 0.5)
icecream = tools.Button(215, 320, icecream_img, 0.4)
roticanai = tools.Button(196, 447, roticanai_img, 0.65)

shavedice = tools.Button(66, 200, shavedice_img, 0.6)
bao = tools.Button(52, 325, bao_img, 0.5)
yeemee = tools.Button(56, 440, yeemee_img, 0.5)
spaggheti = tools.Button(200, 220, spaggheti_img, 0.5)
nasilemak = tools.Button(200, 325, nasilemak_img, 0.5)
kebab = tools.Button(202, 440, kebab_img, 0.5)

onigiri1 = tools.ImageDraw(440, 280, onigiri_img, 1.3)
muffin1 = tools.ImageDraw(440, 260, muffin_img, 1.3)
croissant1 = tools.ImageDraw(440, 280, croissant_img, 1)
burger1 = tools.ImageDraw(435, 270, burger_img, 1.25)
donut1 = tools.ImageDraw(435, 270, donut_img, 1.3)
watermelon1 = tools.ImageDraw(430, 250, watermelon_img, 1.225)

kopi1 = tools.ImageDraw(465, 270, kopi_img, 0.9)
tehtarik1 = tools.ImageDraw(468, 280, tehtarik_img, 0.95)
maggigoreng1 = tools.ImageDraw(420, 270, maggigoreng_img, 0.82)
nasigoreng1 = tools.ImageDraw(440, 270, nasigoreng_img, 0.95)
icecream1 = tools.ImageDraw(460, 270, icecream_img, 0.75)
roticanai1 = tools.ImageDraw(423, 290, roticanai_img, 1.1)

shavedice1 = tools.ImageDraw(450, 270, shavedice_img, 1)
spaggheti1 = tools.ImageDraw(420, 280, spaggheti_img, 1)
bao1 = tools.ImageDraw(420, 280, bao_img, 0.9)
nasilemak1 = tools.ImageDraw(430, 280, nasilemak_img, 0.85)
yeemee1 = tools.ImageDraw(430, 280, yeemee_img, 0.9)
kebab1 = tools.ImageDraw(440, 280, kebab_img, 0.9)

onigiri2 = tools.ImageDraw(500, 480, onigiri_img, 0.7)
muffin2 = tools.ImageDraw(440, 260, muffin_img, 1.3)
croissant2 = tools.ImageDraw(440, 280, croissant_img, 1)
burger2 = tools.ImageDraw(435, 270, burger_img, 1.25)
donut2 = tools.ImageDraw(435, 270, donut_img, 1.3)
watermelon2 = tools.ImageDraw(430, 250, watermelon_img, 1.225)

item1 = tools.ImageDraw(465, 270, kopi_img, 0.9)
item2 = tools.ImageDraw(468, 280, tehtarik_img, 0.95)
item3 = tools.ImageDraw(420, 270, maggigoreng_img, 0.82)
item4 = tools.ImageDraw(440, 270, nasigoreng_img, 0.95)
item5 = tools.ImageDraw(460, 270, icecream_img, 0.75)
item6 = tools.ImageDraw(423, 290, roticanai_img, 1.1)

shavedice2 = tools.ImageDraw(450, 270, shavedice_img, 1)
spaggheti2 = tools.ImageDraw(420, 280, spaggheti_img, 1)
bao2 = tools.ImageDraw(420, 280, bao_img, 0.9)
nasilemak2 = tools.ImageDraw(430, 280, nasilemak_img, 0.85)
yeemee2 = tools.ImageDraw(430, 280, yeemee_img, 0.9)
kebab2 = tools.ImageDraw(440, 280, kebab_img, 0.9)

carbs = tools.ImageDraw(390, 400, carbs_img, 0.4)
fats = tools.ImageDraw(490, 400, fats_img, 0.4)
protein = tools.ImageDraw(590, 400, protein_img, 0.4)

insuf = tools.ImageDraw(390, 420, insuf_img, 0.2)

# /// ----------------- GROUP ------------------------------///
wallpaper = [maintable, b_table1, b_table2, b_table3, b_table4, b_table5, b_table6, walldecor, walldecor2, wardrobe,
             curtain, fridge, wardrobe2, budget, coin]
wallpaperfinal = [maintable, b_table1, b_table2, b_table3, b_table4, b_table5, b_table6, walldecor, walldecor2,
                  curtain, budget, coin]

# ---------------------------- CODES ------------------------------------------

snip = font.render('', True, BROWN)
snip2 = font.render('', True, BROWN)
snip3 = font.render('', True, BROWN)
snip4 = font.render('', True, BROWN)
counter = 0
speed = 4
speed2 = 6
speed3 = 6
speed4 = 6
done = False
namestatus = False
errorstatus = False

# ----Table------
tablelist = []
pos_x = [460, 560, 630, 560, 450, 380]
pos_y = [250, 250, 310, 380, 380, 310]

posx = [400, 520, 400, 520, 400, 520]
posy = [380, 380, 300, 300, 450, 450]

moneylist = []
alist = []
blist = []
clist = []
callist = []
calshow1 = 0

# ////// pie chart //////
colors = [GRAY, BROWN, PEACH]
center_x, center_y = 880, 265
radius = 93
start_angle = 0
labels = ["Carbs", "Fat", "Protein"]

# infinite loop
running = True
while running:
    background.draw(screen)

    # ----------------input name page------------------#
    if page_state == 'name':

        if mute_button.draw(screen):
            pygame.mixer.music.pause()

        if unmute_button.draw(screen):
            pygame.mixer.music.play()

        if start_button.draw(screen):
            clickbutton.play()
            if name != "":
                page_state = 'main'
                namestatus = False
            else:
                namestatus = True

        if namestatus:
            screen.blit(nametext2, ((280, 450)))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box1.collidepoint(event.pos):
                    active1 = True
                else:
                    active1 = False

            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_RETURN:
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode

            if event.type == pygame.QUIT:
                running = False

        pygame.draw.rect(screen, PEACH, input_box1, 2)
        text_surface1 = font.render(name, True, BLACK)
        screen.blit(text_surface1, (input_box1.x + 5, input_box1.y + 10))
        screen.blit(nametext, ((280, 150)))

    # ----------------main button page----------------#
    elif page_state == 'main':

        if mute_button.draw(screen):
            pygame.mixer.music.pause()

        if unmute_button.draw(screen):
            pygame.mixer.music.play()

        message = 'Hi ,  ' + name + ' !! '
        if counter < speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        snip = font_cute.render(message[0:counter // speed], True, BROWN)
        screen.blit(snip, (330, 200))
        if back_button1.draw(screen):
            backbutton.play()
            page_state = 'name'

        if next_button2.draw(screen):
            nextbutton.play()
            page_state = 'gender'

    # ---------------gender page---------------------#
    elif page_state == 'gender':

        if mute_button.draw(screen):
            pygame.mixer.music.pause()

        if unmute_button.draw(screen):
            pygame.mixer.music.play()

        if counter < speed2 * len(gendertext):
            counter += 1
        elif counter >= speed2 * len(gendertext):
            done = True

        snip2 = font_cute.render(gendertext[0:counter // speed2], True, BROWN)
        screen.blit(snip2, (200, 130))
        if male_button.draw(screen):
            malehello.play()
            gender = 'male'
            page_state = 'weight'

        if female_button.draw(screen):
            femalehello.play()
            gender = 'female'
            page_state = 'weight'

        if back_button2.draw(screen):
            backbutton.play()
            page_state = "main"

    # -----------weight and height page-------------#
    elif page_state == 'weight':

        if mute_button.draw(screen):
            pygame.mixer.music.pause()

        if unmute_button.draw(screen):
            pygame.mixer.music.play()

        if counter < speed3 * len(weighttext):
            counter += 1
        elif counter >= speed3 * len(weighttext):
            done = True

        snip3 = font_cute.render(weighttext[0:counter // speed3], True, BROWN)
        screen.blit(snip3, (100, 150))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box2.collidepoint(event.pos):
                    active2 = True
                else:
                    active2 = False

            if event.type == pygame.KEYDOWN:
                if active2:
                    if event.key == pygame.K_RETURN:
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        weight = weight[:-1]
                    elif (event.unicode).isnumeric() == True:
                        weight += event.unicode
                    weightshow = weight

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box3.collidepoint(event.pos):
                    active3 = True
                else:
                    active3 = False

            if event.type == pygame.KEYDOWN:
                if active3:
                    if event.key == pygame.K_RETURN:
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        height = height[:-1]
                    elif (event.unicode).isnumeric() == True:
                        height += event.unicode
                    heightshow = height

            if event.type == pygame.QUIT:
                running = False

        if weight == "":
            weightshow = "Weight(kg)"
            text_surface2 = font.render(weightshow, True, PEACH)
        else:
            text_surface2 = font.render(weightshow, True, BLACK)
        if height == "":
            heightshow = "Height(cm)"
            text_surface3 = font.render(heightshow, True, PEACH)
        else:
            text_surface3 = font.render(heightshow, True, BLACK)

        pygame.draw.rect(screen, PEACH, input_box2, 2)
        pygame.draw.rect(screen, PEACH, input_box3, 2)
        screen.blit(text_surface2, (input_box2.x + 5, input_box2.y + 10))
        screen.blit(text_surface3, (input_box3.x + 5, input_box3.y + 10))

        if next_button3.drawbug(screen) and weight != "" and height != "":
            nextbutton.play()
            page_state = 'budget'

        if back_button3.drawbug(screen):
            backbutton.play()
            page_state = "gender"

    # -------------budget page---------------------#
    elif page_state == 'budget':

        if mute_button.draw(screen):
            pygame.mixer.music.pause()

        if unmute_button.draw(screen):
            pygame.mixer.music.play()

        if counter < speed4 * len(budgettext):
            counter += 1
        elif counter >= speed4 * len(budgettext):
            done = True

        snip4 = font_cute.render(budgettext[0:counter // speed4], True, BROWN)
        screen.blit(snip4, (180, 150))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #
                if input_box4.collidepoint(event.pos):
                    active4 = True
                else:
                    active4 = False

            if event.type == pygame.KEYDOWN:
                if active4:
                    if event.key == pygame.K_RETURN:
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        budgetvalue = budgetvalue[:-1]
                    elif (event.unicode).isnumeric() == True:
                        budgetvalue += event.unicode
                    budgetshow = budgetvalue

            if event.type == pygame.QUIT:
                running = False

        if budgetvalue == "":
            budgetshow = "Budget(RM)"
            text_surface4 = font.render(budgetshow, True, PEACH)
        else:
            text_surface4 = font.render(budgetshow, True, BLACK)

        pygame.draw.rect(screen, PEACH, input_box4, 2)
        screen.blit(text_surface4, (input_box4.x + 5, input_box4.y + 10))

        if next_button4.drawbug(screen) and budgetvalue != "":
            # nextbutton.play()
            page_state = 'system'

        if back_button4.drawbug(screen):
            # backbutton.play()
            page_state = "weight"

    # /// ----------------MMU MAP --------------------///

    if page_state == 'system':
        map.draw(screen)

        if starbee.draw(screen):
            clickbutton.play()
            tablelist = []
            moneylist = []
            alist = []
            blist = []
            clist = []
            callist = []
            page_state = 'starbee'
            errorstatus = False
            callshow1 = 0
        if htc.draw(screen):
            clickbutton.play()
            tablelist = []
            moneylist = []
            callist = []
            page_state = 'htc'
            errorstatus = False
        if bakery.draw(screen):
            clickbutton.play()
            tablelist = []
            moneylist = []
            nutritionlist = []
            callist = []
            page_state = 'bakery'
            errorstatus = False

        if mute_button2.draw(screen):
            pygame.mixer.music.pause()

        if unmute_button2.draw(screen):
            pygame.mixer.music.play()

        if back.draw(screen):
            page_state = 'name'

    # /// ---------------- BAKERY --------------------///

    elif page_state == "bakery":
        tableshow = []
        moneyremain = int(budgetvalue)
        ashow = 1  # carbs-gray
        bshow = 1  # fats-brown
        cshow = 1  # protein-peach
        calshow = 0
        tableshow1 = []

        gamebg.draw(screen)

        for i in wallpaper:
            i.draw(screen)

        piechartbg.draw(screen)
        draw_text("Nutrition", font_cute1, BROWN, 808, 85)
        draw_text("Chart", font_cute1, BROWN, 830, 115)

        draw_text("Calorie", font_cute1, BROWN, 832, 360)
        draw_text("Intake", font_cute1, BROWN, 833, 390)

        if eatbutton.draw(screen):
            page_state = 'final'
            clickbutton.play()

        if tablelist != []:
            for i in range(0, len(tablelist)):
                moneyremain -= moneylist[i]
                calshow += callist[i]
                tableshow.append(tools.Button(pos_x[i], pos_y[i], tablelist[i], 0.6))
                tableshow1.append(tools.Button(posx[i], posy[i], tablelist[i], 0.6))
                ashow += alist[i]
                bshow += blist[i]
                cshow += clist[i]

            for x in range(0, len(tablelist)):
                if tableshow[x].draw(screen):
                    tablelist.pop(x)
                    moneylist.pop(x)
                    alist.pop(x)
                    blist.pop(x)
                    clist.pop(x)
                    callist.pop(x)

        nutritionshow = [ashow, bshow, cshow]

        total = sum(nutritionshow)

        # Draw Pie Chart
        for i, value in enumerate(nutritionshow):
            angle = 2 * math.pi * value / total
            end_angle = start_angle + angle

            # Draw the pie slice as a filled arc
            pygame.draw.arc(screen, colors[i], (center_x - radius, center_y - radius, 2 * radius, 2 * radius),
                            start_angle, end_angle, radius)

            start_angle = end_angle

        draw_text("RM" + str(moneyremain), text_font, (0, 0, 0), 128, 578)
        draw_text(str(calshow) + ' kcal', font, (0, 0, 0), 835, 450)

        # onigiri
        if onigiri.draw(screen):
            if not textstatus:
                textstatus = True
            else:
                textstatus = False

        if textstatus:
            letter.draw(screen)
            draw_text("ONIGIRI", text_font, (0, 0, 0), 450, 120)
            draw_text('Rice stuffed with chicken filling,', text_font, (0, 0, 0), 350, 180)
            draw_text('and wrapped in dried seaweed', text_font, (0, 0, 0), 350, 220)
            pricetag.draw(screen)
            onigiri1.draw(screen)

            #food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("30g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("2g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("6g", font_cute2, PEACH, 600, 470)

            draw_text('RM5', text_font, (0, 0, 0), 630, 325)

            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 5:
                        tablelist.append(onigiri_img)
                        moneylist.append(5)
                        alist.append(30)
                        blist.append(2)
                        clist.append(6)
                        callist.append(170)
                        textstatus = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                textstatus = False
                errorstatus = False

        # muffin
        if muffin.draw(screen):
            if not textstatus2:
                textstatus2 = True
            else:
                textstatus2 = False

        if textstatus2:
            letter.draw(screen)
            draw_text("RED VELVET MUFFIN", text_font, (0, 0, 0), 380, 120)
            draw_text('Small portion of cake with', text_font, (0, 0, 0), 370, 175)
            draw_text('red velvet fillings', text_font, (0, 0, 0), 420, 210)
            pricetag.draw(screen)
            muffin1.draw(screen)

            #food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("30g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("13g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("4g", font_cute2, PEACH, 600, 470)

            draw_text('RM6.5', text_font, (0, 0, 0), 630, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 6.5:
                        tablelist.append(muffin_img)
                        moneylist.append(6.5)
                        alist.append(30)
                        blist.append(13)
                        clist.append(4)
                        callist.append(360)
                        textstatus2 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                textstatus2 = False
                errorstatus = False

        # croissant
        if croissant.draw(screen):
            if not textstatus3:
                textstatus3 = True
            else:
                textstatus3 = False

        if textstatus3:
            letter.draw(screen)
            draw_text("CROISSANT", text_font, (0, 0, 0), 450, 120)
            draw_text('French crescent-shaped roll', text_font, (0, 0, 0), 360, 175)
            draw_text('made of sweet flaky yeast dough', text_font, (0, 0, 0), 340, 210)
            pricetag.draw(screen)
            croissant1.draw(screen)

            #food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("28g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("13g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("4g", font_cute2, PEACH, 600, 470)

            draw_text('RM6.5', text_font, (0, 0, 0), 630, 325)

            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 6.5:
                        tablelist.append(croissant_img)
                        moneylist.append(6.5)
                        alist.append(28)
                        blist.append(13)
                        clist.append(4)
                        callist.append(240)
                        textstatus3 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                textstatus3 = False
                errorstatus = False

        # burger
        if burger.draw(screen):
            if not textstatus4:
                textstatus4 = True
            else:
                textstatus4 = False

        if textstatus4:
            letter.draw(screen)
            draw_text("CHICKEN BURGER", text_font, (0, 0, 0), 380, 120)
            draw_text('Flat bread with chicken patty, egg, ', text_font, (0, 0, 0), 330, 175)
            draw_text('vegetables, and sauces.', text_font, (0, 0, 0), 380, 210)
            pricetag.draw(screen)
            burger1.draw(screen)

            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("40g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("15g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("25g", font_cute2, PEACH, 600, 470)

            draw_text('RM6', text_font, (0, 0, 0), 635, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 6:
                        tablelist.append(burger_img)
                        moneylist.append(6)
                        alist.append(40)
                        blist.append(15)
                        clist.append(25)
                        callist.append(400)
                        textstatus4 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                textstatus4 = False
                errorstatus = False

        # donut
        if donut.draw(screen):
            if not textstatus5:
                textstatus5 = True
            else:
                textstatus5 = False

        if textstatus5:
            letter.draw(screen)
            draw_text("DOUGHNUT", text_font, (0, 0, 0), 440, 120)
            draw_text('Small fried cake of sweetened', text_font, (0, 0, 0), 350, 175)
            draw_text('dough in the shape of a ring', text_font, (0, 0, 0), 360, 210)
            pricetag.draw(screen)
            donut1.draw(screen)

            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("25g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("13g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("2g", font_cute2, PEACH, 600, 470)

            draw_text('RM3.5', text_font, (0, 0, 0), 635, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 3.5:
                        tablelist.append(donut_img)
                        moneylist.append(3.5)
                        alist.append(25)
                        blist.append(13)
                        clist.append(2)
                        callist.append(225)
                        textstatus5 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                textstatus5 = False
                errorstatus = False

        # watermelon juice
        if watermelon.draw(screen):
            if not textstatus6:
                textstatus6 = True
            else:
                textstatus6 = False

        if textstatus6:
            letter.draw(screen)
            draw_text("WATERMELON JUICE", text_font, (0, 0, 0), 380, 120)
            draw_text('Natural watermelon extract', text_font, (0, 0, 0), 370, 190)
            pricetag.draw(screen)
            watermelon1.draw(screen)
            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("12g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("0g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("0g", font_cute2, PEACH, 600, 470)

            draw_text('RM3', text_font, (0, 0, 0), 635, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 3:
                        tablelist.append(watermelon_img)
                        moneylist.append(3)
                        alist.append(12)
                        blist.append(0)
                        clist.append(0)
                        callist.append(60)
                        textstatus6 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                textstatus6 = False
                errorstatus = False

        if errorstatus:
            backbutton.play()
            insuf.draw(screen)
            draw_text("Insufficient Money!", text_font, (255, 0, 0), 410, 450)




    # /// ----------------- HTC ----------------------///

    elif page_state == "htc":
        tableshow = []
        tableshow1 = []
        moneyremain = int(budgetvalue)
        ashow = 10
        bshow = 10
        cshow = 10
        calshow = 0

        gamebg.draw(screen)
        for i in wallpaper:
            i.draw(screen)

        if eatbutton.draw(screen):
            page_state = 'final'
            clickbutton.play()

        piechartbg.draw(screen)
        draw_text("Nutrition", font_cute1, BROWN, 808, 85)
        draw_text("Chart", font_cute1, BROWN, 830, 115)

        draw_text("Calorie", font_cute1, BROWN, 832, 360)
        draw_text("Intake", font_cute1, BROWN, 833, 390)

        if tablelist != []:
            for i in range(0, len(tablelist)):
                moneyremain -= moneylist[i]
                tableshow.append(tools.Button(pos_x[i], pos_y[i], tablelist[i], 0.6))
                tableshow1.append(tools.Button(posx[i], posy[i], tablelist[i], 0.6))
                ashow += alist[i]
                bshow += blist[i]
                cshow += clist[i]
                calshow += callist[i]

            for x in range(0, len(tablelist)):
                if tableshow[x].draw(screen):
                    tablelist.pop(x)
                    moneylist.pop(x)
                    alist.pop(i)
                    blist.pop(i)
                    clist.pop(i)
                    callist.pop(i)

        nutritionshow = [ashow, bshow, cshow]

        total = sum(nutritionshow)

        for i, value in enumerate(nutritionshow):
            angle = 2 * math.pi * value / total
            end_angle = start_angle + angle

            # Draw the pie slice as a filled arc
            pygame.draw.arc(screen, colors[i], (center_x - radius, center_y - radius, 2 * radius, 2 * radius),
                            start_angle, end_angle, radius)

            start_angle = end_angle

        draw_text("RM" + str(moneyremain), text_font, (0, 0, 0), 128, 578)
        draw_text(str(calshow) + 'kcal', font, (0, 0, 0), 835, 450)

        # kopi
        if kopi.draw(screen):
            if not ts1:
                ts1 = True
            else:
                ts1 = False
        if ts1:
            letter.draw(screen)
            draw_text("KOPI", text_font, (0, 0, 0), 480, 120)
            draw_text('Beverage prepared from roasted', text_font, (0, 0, 0), 340, 180)
            draw_text('coffee beans', text_font, (0, 0, 0), 445, 220)
            pricetag.draw(screen)
            kopi1.draw(screen)
            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("1g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("0g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("1g", font_cute2, PEACH, 600, 470)

            draw_text('RM3', text_font, (0, 0, 0), 635, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 3:
                        tablelist.append(kopi_img)
                        moneylist.append(3)
                        alist.append(1)
                        blist.append(0)
                        clist.append(1)
                        callist.append(5)
                        ts1 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                ts1 = False
                errorstatus = False

        # nasi goreng
        if nasigoreng.draw(screen):
            if not ts2:
                ts2 = True
            else:
                ts2 = False
        if ts2:
            letter.draw(screen)
            draw_text("NASI GORENG", text_font, (0, 0, 0), 430, 120)
            draw_text('Stir fried rice with', text_font, (0, 0, 0), 425, 180)
            draw_text('eggs, vegetables, and meat', text_font, (0, 0, 0), 370, 220)
            pricetag.draw(screen)
            nasigoreng1.draw(screen)
            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("22g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("18g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("6g", font_cute2, PEACH, 600, 470)

            draw_text('RM4.5', text_font, (0, 0, 0), 635, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 4.5:
                        tablelist.append(nasigoreng_img)
                        moneylist.append(4.5)
                        alist.append(22)
                        blist.append(18)
                        clist.append(6)
                        callist.append(289)
                        ts2 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                ts2 = False
                errorstatus = False

        # tehtarik
        if tehtarik.draw(screen):
            if not ts3:
                ts3 = True
            else:
                ts3 = False
        if ts3:
            letter.draw(screen)
            draw_text("TEH TARIK", text_font, (0, 0, 0), 440, 120)
            draw_text('Black tea with sweetened', text_font, (0, 0, 0), 380, 180)
            draw_text('condensed milk', text_font, (0, 0, 0), 420, 220)
            pricetag.draw(screen)
            tehtarik1.draw(screen)

            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("283", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("7g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("4g", font_cute2, PEACH, 600, 470)

            draw_text('RM2.5', text_font, (0, 0, 0), 635, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 2.5:
                        tablelist.append(tehtarik_img)
                        moneylist.append(2.5)
                        alist.append(23)
                        blist.append(7)
                        clist.append(4)
                        callist.append(160)
                        ts3 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                ts3 = False
                errorstatus = False

        # icecream
        if icecream.draw(screen):
            if not ts4:
                ts4 = True
            else:
                ts4 = False
        if ts4:
            letter.draw(screen)
            draw_text("VANILLA ICECREAM", text_font, (0, 0, 0), 385, 120)
            draw_text('Frozen milk and cream with', text_font, (0, 0, 0), 360, 180)
            draw_text('vanilla flavoured', text_font, (0, 0, 0), 410, 220)
            pricetag.draw(screen)
            icecream1.draw(screen)

            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("20g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("10g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("4g", font_cute2, PEACH, 600, 470)

            draw_text('RM1.5', text_font, (0, 0, 0), 635, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 1.5:
                        tablelist.append(icecream_img)
                        moneylist.append(1.5)
                        alist.append(20)
                        blist.append(10)
                        clist.append(4)
                        callist.append(150)
                        ts4 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                ts4 = False
                errorstatus = False

        # maggi goreng
        if maggigoreng.draw(screen):
            if not ts5:
                ts5 = True
            else:
                ts5 = False
        if ts5:
            letter.draw(screen)
            draw_text("MAGGI GORENG", text_font, (0, 0, 0), 410, 120)
            draw_text('Stir fried noodle with', text_font, (0, 0, 0), 400, 180)
            draw_text('vegetables, eggs and meat', text_font, (0, 0, 0), 360, 220)
            pricetag.draw(screen)
            maggigoreng1.draw(screen)

            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("61g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("24g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("9g", font_cute2, PEACH, 600, 470)

            draw_text('RM4.5', text_font, (0, 0, 0), 635, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 4.5:
                        tablelist.append(maggigoreng_img)
                        moneylist.append(4.5)
                        alist.append(62)
                        blist.append(24)
                        clist.append(9)
                        callist.append(494)
                        ts5 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                ts5 = False
                errorstatus = False

        # roticanai
        if roticanai.draw(screen):
            if not ts6:
                ts6 = True
            else:
                ts6 = False
        if ts6:
            letter.draw(screen)
            draw_text("ROTI CANAI", text_font, (0, 0, 0), 440, 120)
            draw_text('Plain flatbread dough with', text_font, (0, 0, 0), 370, 180)
            draw_text('a whole lot of ghee (clarified butter)', text_font, (0, 0, 0), 325, 220)
            pricetag.draw(screen)
            roticanai1.draw(screen)

            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("20g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("10g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("3g", font_cute2, PEACH, 600, 470)

            draw_text('RM2', text_font, (0, 0, 0), 635, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 2:
                        tablelist.append(roticanai_img)
                        moneylist.append(2)
                        alist.append(20)
                        blist.append(10)
                        clist.append(3)
                        callist.append(250)
                        ts6 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                ts6 = False
                errorstatus = False

        if errorstatus:
            backbutton.play()
            insuf.draw(screen)
            draw_text("Insufficient Money!", text_font, (255, 0, 0), 410, 450)

    # /// ----------------- STARBEE ------------------///

    elif page_state == "starbee":
        tableshow = []
        tableshow1 = []
        moneyremain = int(budgetvalue)
        ashow = 10
        bshow = 10
        cshow = 10
        calshow = 0

        gamebg.draw(screen)
        for i in wallpaper:
            i.draw(screen)

        if eatbutton.draw(screen):
            clickbutton.play()
            page_state = 'final'

        piechartbg.draw(screen)
        draw_text("Nutrition", font_cute1, BROWN, 808, 85)
        draw_text("Chart", font_cute1, BROWN, 830, 115)

        draw_text("Calorie", font_cute1, BROWN, 832, 360)
        draw_text("Intake", font_cute1, BROWN, 833, 390)

        if tablelist != []:
            for i in range(0, len(tablelist)):
                moneyremain -= moneylist[i]
                tableshow.append(tools.Button(pos_x[i], pos_y[i], tablelist[i], 0.6))
                tableshow1.append(tools.Button(posx[i], posy[i], tablelist[i], 0.6))
                ashow += alist[i]
                bshow += blist[i]
                cshow += clist[i]
                calshow += callist[i]

            for x in range(0, len(tablelist)):
                if tableshow[x].draw(screen):
                    tablelist.pop(x)
                    moneylist.pop(x)
                    alist.pop(i)
                    blist.pop(i)
                    clist.pop(i)
                    callist.pop(i)

        nutritionshow = [ashow, bshow, cshow]

        total = sum(nutritionshow)

        for i, value in enumerate(nutritionshow):
            angle = 2 * math.pi * value / total
            end_angle = start_angle + angle

            # Draw the pie slice as a filled arc
            pygame.draw.arc(screen, colors[i], (center_x - radius, center_y - radius, 2 * radius, 2 * radius),
                            start_angle, end_angle, radius)

            start_angle = end_angle

        draw_text("RM" + str(moneyremain), text_font, (0, 0, 0), 128, 578)
        draw_text(str(calshow) + 'kcal', font, (0, 0, 0), 835, 450)

        # shaved ice
        if shavedice.draw(screen):
            if not t1:
                t1 = True
            else:
                t1 = False

        if t1:
            letter.draw(screen)
            draw_text("STRAWBERRY", text_font, (0, 0, 0), 410, 120)
            draw_text('SHAVED ICE', text_font, (0, 0, 0), 420, 150)
            draw_text('finely crushed ice with', text_font, (0, 0, 0), 380, 190)
            draw_text('sweet strawberry condiments ', text_font, (0, 0, 0), 340, 220)
            pricetag.draw(screen)
            shavedice1.draw(screen)

            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("30g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("0g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("0g", font_cute2, PEACH, 600, 470)

            draw_text('RM7', text_font, (0, 0, 0), 635, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 7:
                        tablelist.append(shavedice_img)
                        moneylist.append(7)
                        alist.append(30)
                        blist.append(0)
                        clist.append(0)
                        callist.append(125)
                        t1 = False

            if closebutton.draw(screen):
                t1 = False
                errorstatus = False

        # spaghetti
        if spaggheti.draw(screen):
            if not t2:
                t2 = True
            else:
                t2 = False

        if t2:
            letter.draw(screen)
            draw_text("SPAGHETTI", text_font, (0, 0, 0), 430, 120)
            draw_text('Wheat noodles with tomato sauce,', text_font, (0, 0, 0), 320, 190)
            draw_text('mushrooms, vegetables and meat ', text_font, (0, 0, 0), 320, 220)
            pricetag.draw(screen)
            spaggheti1.draw(screen)

            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("45g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("1g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("10g", font_cute2, PEACH, 600, 470)

            draw_text('RM7', text_font, (0, 0, 0), 635, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 7:
                        tablelist.append(spaggheti_img)
                        moneylist.append(7)
                        alist.append(45)
                        blist.append(1)
                        clist.append(10)
                        callist.append(220)
                        t2 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                t2 = False
                errorstatus = False

        # bao
        if bao.draw(screen):
            if not t3:
                t3 = True
            else:
                t3 = False

        if t3:
            letter.draw(screen)
            draw_text("STEAMED BUN", text_font, (0, 0, 0), 410, 130)
            draw_text('Plain flour bread ', text_font, (0, 0, 0), 410, 190)
            draw_text('with red bean fillings', text_font, (0, 0, 0), 400, 220)
            pricetag.draw(screen)
            bao1.draw(screen)

            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("25g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("7g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("8g", font_cute2, PEACH, 600, 470)

            draw_text('RM1.5', text_font, (0, 0, 0), 628, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 1.5:
                        tablelist.append(bao_img)
                        moneylist.append(1.5)
                        alist.append(25)
                        blist.append(7)
                        clist.append(8)
                        callist.append(176)
                        t3 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                t3 = False
                errorstatus = False

        # nasilemak
        if nasilemak.draw(screen):
            if not t4:
                t4 = True
            else:
                t4 = False

        if t4:
            letter.draw(screen)
            draw_text("NASI LEMAK", text_font, (0, 0, 0), 430, 130)
            draw_text('Fragrant rice cooked in', text_font, (0, 0, 0), 380, 190)
            draw_text('coconut milk and pandan leaf', text_font, (0, 0, 0), 350, 220)
            pricetag.draw(screen)
            nasilemak1.draw(screen)
            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("80g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("14g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("13g", font_cute2, PEACH, 600, 470)

            draw_text('RM4', text_font, (0, 0, 0), 628, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 4:
                        tablelist.append(nasilemak_img)
                        moneylist.append(4)
                        alist.append(80)
                        blist.append(14)
                        clist.append(13)
                        callist.append(389)
                        t4 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                t4 = False
                errorstatus = False

        # yeemee
        if yeemee.draw(screen):
            if not t5:
                t5 = True
            else:
                t5 = False

        if t5:
            letter.draw(screen)
            draw_text("YEE MEE", text_font, (0, 0, 0), 445, 130)
            draw_text('Cantonese egg noodles', text_font, (0, 0, 0), 380, 190)
            draw_text('with eggs and vegetables', text_font, (0, 0, 0), 375, 220)
            pricetag.draw(screen)
            yeemee1.draw(screen)

            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("42g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("30g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("33g", font_cute2, PEACH, 600, 470)

            draw_text('RM6.5', text_font, (0, 0, 0), 628, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 6.5:
                        tablelist.append(yeemee_img)
                        moneylist.append(6.5)
                        alist.append(42)
                        blist.append(30)
                        clist.append(33)
                        callist.append(590)
                        t5 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                t5 = False
                errorstatus = False

        # kebab
        if kebab.draw(screen):
            if not t6:
                t6 = True
            else:
                t6 = False

        if t6:
            letter.draw(screen)
            draw_text("KEBAB", text_font, (0, 0, 0), 465, 130)
            draw_text('grilled minced meat with', text_font, (0, 0, 0), 380, 190)
            draw_text('vegetables wrapped with tortilla', text_font, (0, 0, 0), 340, 220)
            pricetag.draw(screen)
            kebab1.draw(screen)

            # food info
            carbs.draw(screen)
            draw_text("Carbs", font_cute2, GRAY, 380, 440)
            draw_text("8g", font_cute2, GRAY, 390, 470)
            fats.draw(screen)
            draw_text("Fats", font_cute2, BROWN, 490, 440)
            draw_text("14g", font_cute2, BROWN, 500, 470)
            protein.draw(screen)
            draw_text("Protein", font_cute2, PEACH, 580, 440)
            draw_text("44g", font_cute2, PEACH, 600, 470)

            draw_text('RM8', text_font, (0, 0, 0), 628, 325)
            if button.draw(screen):
                if len(tablelist) < 6:
                    if moneyremain >= 8:
                        tablelist.append(kebab_img)
                        moneylist.append(8)
                        alist.append(8)
                        blist.append(14)
                        clist.append(44)
                        callist.append(329)
                        t6 = False
                    else:
                        errorstatus = True

            if closebutton.draw(screen):
                t6 = False
                errorstatus = False

        if errorstatus:
            backbutton.play()
            insuf.draw(screen)
            draw_text("Insufficient Money!", text_font, (255, 0, 0), 410, 450)

    # Final Page //////////////////////////////////////////////////////////////////////////////////////////////////
    elif page_state == "final":
        gamebg.draw(screen)
        for i in wallpaperfinal:
            i.draw(screen)

        finalbg.draw(screen)

        for i in tableshow1:
            i.draw(screen)

        spending = int(budgetvalue) - moneyremain
        draw_text("Total Spending:", font_cute1, (92, 64, 51), 700, 270)
        draw_text("RM" + str(spending), font, BROWN, 700, 340)

        draw_text("Total Calorie", font_cute1, (92, 64, 51), 700, 390)
        draw_text("Intake:", font_cute1, (92, 64, 51), 700, 430)
        draw_text(str(calshow) + "kcal", font, BROWN, 700, 490)

        draw_text("Carbohydrates", font_cute2, (92, 64, 51), 0, 250)
        draw_text("Fats", font_cute1, (92, 64, 51), 100, 370)
        draw_text("Protein", font_cute1, (92, 64, 51), 60, 500)

        draw_text(str(ashow) + "g", font, WHITE, 220, 250)
        draw_text(str(bshow) + "g", font, WHITE, 220, 370)
        draw_text(str(cshow) + "g", font, WHITE, 220, 500)

    if page_state == "bakery" or page_state == "htc" or page_state == "starbee" or page_state == "final":
        if homebutton.draw(screen):
            backbutton.play()
            page_state = 'system'

        if mute_button1.draw(screen):
            backbutton.play()
            pygame.mixer.music.pause()

        if unmute_button1.draw(screen):
            backbutton.play()
            pygame.mixer.music.play()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                input_name = True
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
