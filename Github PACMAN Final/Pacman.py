# Importing files
import turtle
import random
import time
import math
import winsound

# ----------Setting up window----------------------
wind = turtle.Screen()
wind.setup(450, 600)
wind.bgcolor('black')

# ----------------Graphics--------------------------
wind.addshape('game over.gif')
wind.addshape('1life.gif')
wind.addshape('2lives.gif')
wind.addshape('3lives.gif')
scoretwohundred = '200.gif'
wind.addshape(scoretwohundred)
scorefourhundred = '400.gif'
wind.addshape(scorefourhundred)
scoreeighthundred = '800.gif'
wind.addshape(scoreeighthundred)
scoresixteenhundred = '1600.gif'
wind.addshape(scoresixteenhundred)
pacpicrightopen = 'rightopen.gif'
pacpicrighthalf = 'halfright.gif'
pacpicclosed = 'closed.gif'
wind.addshape(pacpicrightopen)
wind.addshape(pacpicrighthalf)
wind.addshape(pacpicclosed)
pacpicupopen = 'upopen.gif'
pacpicuphalf = 'halfup.gif'
wind.addshape(pacpicupopen)
wind.addshape(pacpicuphalf)
pacpicleftopen = 'leftopen.gif'
pacpiclefthalf = 'halfleft.gif'
wind.addshape(pacpicleftopen)
wind.addshape(pacpiclefthalf)
pacpicdownopen = 'downopen.gif'
pacpicdownhalf = 'halfdown.gif'
wind.addshape(pacpicdownopen)
wind.addshape(pacpicdownhalf)
redright = 'redright.gif'
redleft = 'redleft.gif'
downred= 'downred.gif'
upred = 'upred.gif'
wind.addshape(downred)
wind.addshape(upred)
wind.addshape(redleft)
wind.addshape(redright)
ghostscareblue = 'ghostscareblue.gif'
wind.addshape(ghostscareblue)
blueright = 'blueright.gif'
blueleft = 'blueleft.gif'
downblue= 'bluedown.gif'
upblue = 'blueup.gif'
wind.addshape(downblue)
wind.addshape(upblue)
wind.addshape(blueleft)
wind.addshape(blueright)
pinkright = 'pinkright.gif'
pinkleft = 'pinkleft.gif'
downpink= 'pinkdown.gif'
uppink = 'pinkup.gif'
wind.addshape(downpink)
wind.addshape(uppink)
wind.addshape(pinkleft)
wind.addshape(pinkright)
yellowright = 'yellowright.gif'
yellowleft = 'yellowleft.gif'
downyellow= 'yellowdown.gif'
upyellow = 'yellowup.gif'
wind.addshape(downyellow)
wind.addshape(upyellow)
wind.addshape(yellowleft)
wind.addshape(yellowright)
wind.addshape('cherry.gif')
#-------------Creating all turtles------------------
w = turtle.Turtle()
pl = turtle.Turtle()
ready = turtle.Turtle()
scoreboardbot = turtle.Turtle()
scorebot = turtle.Turtle()
lifebar = turtle.Turtle()
blinky = turtle.Turtle()
inky = turtle.Turtle()
pinky = turtle.Turtle()
clyde = turtle.Turtle()
levelbot = turtle.Turtle()
fruitbot = turtle.Turtle()
fruitbot.shape('cherry.gif')
fruitbot.ht()
fruitbot.penup()
gameover = turtle.Turtle()
gameover.ht()
gameover.penup()
gameover.shape('game over.gif')
#---------------Intro scene------------------------
gameover.goto(0,200)
gameover.pencolor('white')
gameover.write('Pac - Man', move=False, align="center", font=("Terminal", 10, "bold"))
gameover.goto(0,100)
gameover.write('WASD to move', move=False, align="center", font=("Terminal", 10, "bold"))
gameover.goto(0,0)
gameover.write('Avoid ghosts', move=False, align="center", font=("Terminal", 10, "bold"))
gameover.goto(0, -100)
gameover.write('Collect dots and fruit', move=False, align="center", font=("Terminal", 10, "bold"))
gameover.goto(0,-200)
gameover.write('Eat bigger dots for the ability to eat the ghosts for a short while', move=False, align="center", font=("Terminal", 10, "bold"))
time.sleep(5)
gameover.clear()

# ------------Creating grid------------------------
w.fillcolor('black')
w.penup()
w.shape('square')
w.turtlesize(1, 1)
w.goto(-140, 200)
w.ht()
flags = [[]]
walls = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1],
         [14, 1], [15, 1], [1, 2], [8, 2], [15, 2], [1, 3], [3, 3], [5, 3], [6, 3], [8, 3], [10, 3], [11, 3], [13, 3],
         [15, 3], [1, 4], [15, 4], [1, 5], [3, 5], [4, 5], [5, 5], [6, 5], [8, 5], [10, 5], [11, 5], [12, 5], [13, 5],
         [15, 5], [1, 6],
         [15, 6], [1, 7], [2, 7], [4, 7], [6, 7], [7, 7], [9, 7], [10, 7], [12, 7], [14, 7], [15, 7],
         [4, 8], [12, 8], [1, 9], [2, 9], [4, 9], [6, 9], [7, 9], [8, 9], [9, 9], [10, 9], [12, 9], [14, 9], [15, 9],
         [2, 10], [6, 10], [10, 10], [14, 10], [1, 11], [2, 11], [4, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11],
         [12, 11], [14, 11], [15, 11], [4, 12], [12, 12], [1, 13], [2, 13], [4, 13], [6, 13], [7, 13], [8, 13], [9, 13],
         [10, 13], [12, 13], [14, 13], [15, 13], [1, 14], [8, 14], [15, 14], [1, 15], [3, 15], [4, 15], [6, 15],
         [8, 15], [10, 15], [12, 15], [13, 15], [15, 15], [1, 16], [4, 16], [12, 16], [15, 16], [1, 17], [2, 17],
         [6, 17], [7, 17], [8, 17], [9, 17], [10, 17], [14, 17], [15, 17], [1, 18], [4, 18], [8, 18], [12, 18],
         [15, 18], [1, 19], [3, 19], [4, 19], [5, 19], [6, 19], [8, 19], [10, 19], [11, 19], [12, 19], [13, 19],
         [15, 19], [1, 20], [15, 20], [1, 21], [2, 21], [3, 21], [4, 21], [5, 21], [6, 21], [7, 21], [8, 21], [9, 21],
         [10, 21], [11, 21], [12, 21], [13, 21], [14, 21], [15, 21]]
wind.tracer(0, 0)
y = 1
x = 1
for i in range(220, -240, -20):
    for j in range(-160, 180, 20):
        w.goto(j, i)
        if [x, y] in walls:
            w.fillcolor("blue")
            w.stamp()
            w.fillcolor("black")
        if [x, y] == [8, 9]:
            w.fillcolor("green")
            w.stamp()
            w.fillcolor("blue")
            # else:
            # w.stamp()
        temp = [j, i]
        # coords[y].append(temp)
        # print(y)
        # flags[y - 1].append([])
        flags[y - 1].append(temp)
        x += 1
    y += 1
    x = 1
    flags.append([])

# Create dots
dots = []
totaldots = 0
for j in range(0, 21, 1):
    for o in range(0, 15, 1):
        if [o + 1, j + 1] not in walls and [o, j] != [0, 9] and [o, j] != [14, 9] and [o, j] != [6, 9] and [o, j] != [7,
                                                                                                                      9] and [
            o, j] != [8, 9] and [o, j] != [1, 1] and [o, j] != [1, 19] and [o, j] != [13, 1] and [o, j] != [13, 19]:
            dots.append(turtle.Turtle())
            dots[len(dots) - 1].penup()
            dots[len(dots) - 1].goto(flags[j][o][0], flags[j][o][1])
            dots[len(dots) - 1].color('white')
            dots[len(dots) - 1].turtlesize(0.1)
            dots[len(dots) - 1].shape('circle')
            totaldots += 1
    wind.update()

powerdots = []
for j in range(0, 21, 1):
    for o in range(0, 15, 1):
        if [o, j] == [1, 1] or [o, j] == [1, 19] or [o, j] == [13, 1] or [o, j] == [13, 19]:
            powerdots.append(turtle.Turtle())
            powerdots[len(powerdots) - 1].penup()
            powerdots[len(powerdots) - 1].goto(flags[j][o][0], flags[j][o][1])
            powerdots[len(powerdots) - 1].color('white')
            powerdots[len(powerdots) - 1].turtlesize(0.4)
            powerdots[len(powerdots) - 1].shape('circle')
            totaldots += 1
wind.update()

#-------------Level loop-------------------------------------
winning = True
levelcount = 1
scattertime = 10
ghostfwdamnt = 2
while winning == True:
    # -----------Create player-----------------------------------
    pl.penup()
    pl.turtlesize(0.75, 0.75)
    pl.shape(pacpicrightopen)
    pl.color('white')
    pl.goto(flags[15][7][0], flags[15][7][1])
    wind.update()
    #------------Graphics Turtles--------------------------------
    ready.ht()
    ready.penup()
    wind.addshape('ready.gif')
    ready.shape('ready.gif')
    ready.goto(flags[11][7][0],flags[11][7][1])

    scoreboardbot.ht()
    scoreboardbot.goto(-120, 240)
    scoreboardbot.pencolor('white')

    scorebot.ht()
    scorebot.penup()
    scorebot.pencolor('#9ce5ed')

    lifebar.ht()
    lifebar.penup()
    lifebar.goto(80, 250)
    lifebar.shape('3lives.gif')
    lifebar.st()

    levelbot.ht()
    levelbot.penup()
    levelbot.goto(flags[15][7][0], -250)
    levelbot.pencolor('white')
    # -----------Create Ghosties---------------------------------
    blinky.penup()
    blinky.goto(round(flags[7][7][0]), flags[7][7][1])

    inky.penup()
    inky.goto(flags[9][7][0], flags[9][7][1])

    pinky.penup()
    pinky.goto(flags[9][8][0], flags[9][8][1])

    clyde.penup()
    clyde.goto(flags[9][6][0], flags[9][6][1])

    # -----------Functions---------------------------------------
    # Game functions
    def scoring():
        global score
        global scorethen
        if scorethen < score:
            scoreboardbot.clear()
            scoreboardbot.write(score, move=False, align="center", font=("Terminal", 12, "bold"))
            scorethen = score
    def fruitspawn():
        global lastfruitspawn
        global fruitout
        if lastfruitspawn - time.time() < -20 and fruitout == False:
            x = 1
            y = 1
            while [x,y] in walls or [x, y] == [0, 9] or [x, y] == [14, 9] or [x, y] == [6, 9] or [x, y] == [7, 9] or [x, y] == [8, 9] or [x, y] == [1, 1] or [x, y] == [1, 19] or [x, y] == [13, 1] or [x, y] == [13, 19]:
                x = random.randint(1,15)
                y = random.randint(1,21)
            fruitbot.goto(flags[y - 1][x - 1][0], flags[y - 1][x - 1][1])
            fruitbot.st()
            fruitbot.setheading(0)
            lastfruitspawn = time.time()
            fruitout = True
        if lastfruitspawn - time.time() < -10:
            fruitbot.ht()
            fruitout = False
    def fruitget():
        global fruitout
        global lastscoredisplay
        global score
        if pl.distance(fruitbot) < 15 and fruitbot.isvisible() == True:
            fruitbot.ht()
            fruitout = False
            scorebot.goto(pl.pos())
            scorebot.write('250', move=False, align="center", font=("comic sans", 9, "normal"))
            lastscoredisplay = time.time()
            score += 250
        if time.time() - lastscoredisplay > 2:
            scorebot.clear()
    # Player Functions
    def playerup():
        x = 1000
        y = 1000
        global plleft
        global plright
        global pldown
        global plup
        global uplater
        gridon = False
        x = 100
        y = 100
        ply = pl.ycor() + 20
        plx = pl.xcor()
        if uplater == True:
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i])):
                    if flags[i][j][0] == plx and flags[i][j][1] == ply:
                        x = j + 1
                        y = i + 1
                        gridon = True
            if [x, y] not in walls and gridon == True:
                # pl.goto(plx,ply)
                pldown = False
                plleft = False
                plright = False
                plup = True


    def playerleft():
        x = 1000
        y = 1000
        global plleft
        global plright
        global pldown
        global plup
        global leftlater
        gridon = False
        ply = pl.ycor()
        plx = pl.xcor() - 20
        if leftlater == True:
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i])):
                    if flags[i][j][0] == plx and flags[i][j][1] == ply:
                        x = j + 1
                        y = i + 1
                        gridon = True
            if [x, y] not in walls and gridon == True:
                # pl.goto(plx,ply)
                pldown = False
                plleft = True
                plright = False
                plup = False


    def playerright():
        x = 1000
        y = 1000
        global plleft
        global plright
        global pldown
        global plup
        global rightlater
        gridon = False
        ply = pl.ycor()
        plx = pl.xcor() + 20
        if rightlater == True:
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i])):
                    if flags[i][j][0] == plx and flags[i][j][1] == ply:
                        x = j + 1
                        y = i + 1
                        gridon = True
            if [x, y] not in walls and gridon == True:
                # pl.goto(plx, ply)
                pldown = False
                plleft = False
                plright = True
                plup = False


    def playerdown():
        x = 1000
        y = 1000
        global plleft
        global plright
        global pldown
        global plup
        global downlater
        gridon = False
        ply = pl.ycor() - 20
        plx = pl.xcor()
        if downlater == True:
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i])):
                    if flags[i][j][0] == plx and flags[i][j][1] == ply:
                        x = j + 1
                        y = i + 1
                        gridon = True
            if [x, y] not in walls and gridon == True:
                # pl.goto(plx, ply)
                pldown = True
                plleft = False
                plright = False
                plup = False


    def plleftwall(pl):
        x = 1000
        y = 1000
        global plleft
        if plleft == True:
            ply = pl.ycor()
            plx = pl.xcor() - 20
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i])):
                    if flags[i][j][0] == plx and flags[i][j][1] == ply:
                        x = j + 1
                        y = i + 1
            if [x, y] in walls:
                plleft = False


    def plrightwall(pl):
        x = 1000
        y = 1000
        global plright
        if plright == True:
            ply = pl.ycor()
            plx = pl.xcor() + 20
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i])):
                    if flags[i][j][0] == plx and flags[i][j][1] == ply:
                        x = j + 1
                        y = i + 1
            if [x, y] in walls:
                plright = False


    def pltopwall(pl):
        x = 1000
        y = 1000
        global plup
        if plup == True:
            ply = pl.ycor() + 20
            plx = pl.xcor()
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i])):
                    if flags[i][j][0] == plx and flags[i][j][1] == ply:
                        x = j + 1
                        y = i + 1
            if [x, y] in walls:
                plup = False


    def pldownwall(pl):
        x = 1000
        y = 1000
        global pldown
        if pldown == True:
            ply = pl.ycor() - 20
            plx = pl.xcor()
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i])):
                    if flags[i][j][0] == plx and flags[i][j][1] == ply:
                        x = j + 1
                        y = i + 1
            if [x, y] in walls:
                pldown = False


    def turnuplater():
        global uplater
        global leftlater
        global downlater
        global rightlater
        uplater = True
        leftlater = False
        downlater = False
        rightlater = False


    def turnleftlater():
        global uplater
        global leftlater
        global downlater
        global rightlater
        uplater = False
        leftlater = True
        downlater = False
        rightlater = False


    def turnldownlater():
        global uplater
        global leftlater
        global downlater
        global rightlater
        uplater = False
        leftlater = False
        downlater = True
        rightlater = False


    def turnrightlater():
        global uplater
        global leftlater
        global downlater
        global rightlater
        uplater = False
        leftlater = False
        downlater = False
        rightlater = True


    def playerwrap():
        if pl.xcor() > flags[1][15][0] - 16:
            pl.goto(flags[1][1][0] - 16, pl.ycor())
        if pl.xcor() < flags[1][1][0] - 16:
            pl.goto(flags[1][15][0] - 16, pl.ycor())

    def playermove():
        global plup
        global plleft
        global pldown
        global plright
        if plright == True:
            pl.goto(pl.xcor() + 2, pl.ycor())
        if plleft == True:
            pl.goto(pl.xcor() - 2, pl.ycor())
        if pldown == True:
            pl.goto(pl.xcor(), pl.ycor() - 2)
        if plup == True:
            pl.goto(pl.xcor(), pl.ycor() + 2)


    def playerdeath(player, ghost):
        global timeforspawn
        global pinkyin
        global inkyin
        global clydein
        global lives
        global plright
        global plup
        global pldown
        global plleft
        if player.distance(ghost) < 15:
            pinkyin = False
            inkyin = False
            clydein = False
            lives -= 1
            player.goto(flags[15][7][0], flags[15][7][1])
            blinky.goto(round(flags[7][7][0]), flags[7][7][1])
            blinky.setheading(0)
            pinky.setheading(180)
            inky.setheading(0)
            clyde.setheading(180)
            inky.goto(flags[9][7][0], flags[9][7][1])
            pinky.goto(flags[9][8][0], flags[9][8][1])
            clyde.goto(flags[9][6][0], flags[9][6][1])
            if lives > 0:
                ready.st()
            if lives == 2:
                lifebar.shape("2lives.gif")
            if lives == 1:
                lifebar.shape('1life.gif')
            wind.update()
            winsound.PlaySound("pacman_death.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
            time.sleep(3)
            ready.ht()
            plright = True
            plup = False
            pldown = False
            plleft = False
            timeforspawn = time.time()

    def pacmanimation():
        global plright
        global plleft
        global plup
        global pldown
        global timesinceimage
        global pacmanimageindex
        global dotsgotten
        global dotsnow

        difof2 = time.time() - timesinceimage

        if difof2 > 0.1:
            if pldown == True:
                pacmanimageindex += 1
                if pacmanimageindex == 1:
                    pl.shape(pacpicdownopen)
                    timesinceimage = time.time()
                if pacmanimageindex == 2:
                    pl.shape(pacpicdownhalf)
                    timesinceimage = time.time()
                if pacmanimageindex == 3:
                    pl.shape(pacpicclosed)
                    timesinceimage = time.time()
                if pacmanimageindex == 4:
                    pl.shape(pacpicdownhalf)
                    timesinceimage = time.time()
                    pacmanimageindex = 0

            if plleft == True:
                pacmanimageindex += 1
                if pacmanimageindex == 1:
                    pl.shape(pacpicleftopen)
                    timesinceimage = time.time()
                if pacmanimageindex == 2:
                    pl.shape(pacpiclefthalf)
                    timesinceimage = time.time()
                if pacmanimageindex == 3:
                    pl.shape(pacpicclosed)
                    timesinceimage = time.time()
                if pacmanimageindex == 4:
                    pl.shape(pacpiclefthalf)
                    timesinceimage = time.time()
                    pacmanimageindex = 0

            if plup == True:
                pacmanimageindex += 1
                if pacmanimageindex == 1:
                    pl.shape(pacpicupopen)
                    timesinceimage = time.time()
                if pacmanimageindex == 2:
                    pl.shape(pacpicuphalf)
                    timesinceimage = time.time()
                if pacmanimageindex == 3:
                    pl.shape(pacpicclosed)
                    timesinceimage = time.time()
                if pacmanimageindex == 4:
                    pl.shape(pacpicuphalf)
                    timesinceimage = time.time()
                    pacmanimageindex = 0

            if plright == True:
                pacmanimageindex += 1
                if pacmanimageindex == 1:
                    pl.shape(pacpicrightopen)
                    timesinceimage = time.time()
                if pacmanimageindex == 2:
                    pl.shape(pacpicrighthalf)
                    timesinceimage = time.time()
                if pacmanimageindex == 3:
                    pl.shape(pacpicclosed)
                    timesinceimage = time.time()
                if pacmanimageindex == 4:
                    pl.shape(pacpicrighthalf)
                    timesinceimage = time.time()
                    pacmanimageindex = 0

    def blinkyanimation():
                    if blinky.heading() == 0:
                        blinky.shape(redright)
                    if blinky.heading() == 90:
                        blinky.shape(upred)
                    if blinky.heading() == 180:
                        blinky.shape(redleft)
                    if blinky.heading() == 270:
                        blinky.shape(downred)

    def inkyanimation():
                    if inky.heading() == 0:
                        inky.shape(blueright)
                    if inky.heading() == 90:
                        inky.shape(upblue)
                    if inky.heading() == 180:
                        inky.shape(blueleft)
                    if inky.heading() == 270:
                        inky.shape(downblue)

    def pinkyanimation():
                    if pinky.heading() == 0:
                        pinky.shape(pinkright)
                    if pinky.heading() == 90:
                        pinky.shape(uppink)
                    if pinky.heading() == 180:
                        pinky.shape(pinkleft)
                    if pinky.heading() == 270:
                        pinky.shape(downpink)

    def clydeanimation():
                    if clyde.heading() == 0:
                        clyde.shape(yellowright)
                    if clyde.heading() == 90:
                        clyde.shape(upyellow)
                    if clyde.heading() == 180:
                        clyde.shape(yellowleft)
                    if clyde.heading() == 270:
                        clyde.shape(downyellow)


    # Dot functions
    def dotget(dot, pl):
        global dotsgotten
        global score
        if dot.distance(pl) < 8 and dot.isvisible() == True:
            dot.ht()
            winsound.PlaySound("pacman_chomp.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
            dotsgotten += 1
            score += 10

    def powerdotget(dot, pl):
        global frightened
        global frightenedstart
        global lastscatterchange
        global score
        global scorecounter
        global dotsgotten
        if dot.distance(pl) < 12 and dot.isvisible() == True:
            dot.ht()
            frightened = True
            frightenedstart = time.time()
            blinky.shape('ghostscareblue.gif')
            inky.shape('ghostscareblue.gif')
            pinky.shape('ghostscareblue.gif')
            clyde.shape('ghostscareblue.gif')
            score += 50
            dotsgotten += 1
        if frightenedstart - time.time() < -5 and frightened == True:
            frightened = False
            lastscatterchange = time.time()
            blinky.st()
            pinky.st()
            inky.st()
            clyde.st()
            scorecounter = 0
            ghostalign(blinky)
            ghostalign(pinky)
            ghostalign(inky)
            ghostalign(clyde)

    # Ghost functions
    def ghostwrap(ghost):
        if int(ghost.xcor()) > flags[1][15][0] - 16:
            print(ghost.pos(), '-----------------')
            ghost.goto(flags[1][1][0] - 16, ghost.ycor())
        if int(ghost.xcor()) < flags[1][1][0] - 16:
            print(ghost.pos(), '-----------------')
            ghost.goto(flags[1][15][0] - 16, ghost.ycor())

    def ghostmove(ghost):
        if ghost.isvisible() == True:
            ghost.forward(ghostfwdamnt)

    def pinkymove():
        if pl.heading() == 0:
            ghostseek(pinky, pl.xcor() + 40, pl.ycor())
            ghostwall(pinky, pl.xcor() + 40, pl.ycor())
        if pl.heading() == 90:
            ghostseek(pinky, pl.xcor(), pl.ycor() + 40)
            ghostwall(pinky, pl.xcor(), pl.ycor() + 40)
        if pl.heading() == 180:
            ghostseek(pinky, pl.xcor() - 40, pl.ycor())
            ghostwall(pinky, pl.xcor() - 40, pl.ycor())
        if pl.heading() == 270:
            ghostseek(pinky, pl.xcor(), pl.ycor() - 40)
            ghostwall(pinky, pl.xcor(), pl.ycor() - 40)

    def inkymove():
        x = pl.xcor() - blinky.xcor()
        y = pl.ycor() - blinky.ycor()
        ghostseek(inky, pl.xcor() + x, pl.ycor() + y)
        ghostwall(inky, pl.xcor() + x, pl.ycor() + y)

    def clydemove():
        if clyde.distance(pl) > 50:
            ghostseek(clyde, pl.xcor(), pl.ycor())
            ghostwall(clyde, pl.xcor(), pl.ycor())
        else:
            ghostfrightenedseek(clyde)
            ghostfrightenedwall(clyde)

    def ghostseek(ghost, playerx, playery):
        # for ghost turning on intersections
        if ghost.isvisible() == True:
            x = 100000
            y = 100000
            plx = playerx
            ply = playery
            blx = ghost.xcor()
            bly = ghost.ycor()
            x1 = plx - blx
            y1 = ply - bly
            gridon = False
            # checks to find the greater of the differences in x,y coords between pl / ghost
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i])):
                    if flags[i][j][0] == round(blx, 5) and flags[i][j][1] == round(bly, 5):
                        x = j + 1
                        y = i + 1
                        gridon = True
            if gridon == True:
                if abs(x1) > abs(y1) and x1 > 0 and (ghost.heading() == 270 or ghost.heading() == 90):
                    if [x + 1, y] not in walls:  # round(time.time(), 2) - timelastmove > 10:
                        ghost.setheading(0)
                if abs(x1) > abs(y1) and x1 < 0 and (ghost.heading() == 270 or ghost.heading() == 90):
                    if [x - 1, y] not in walls:
                        ghost.setheading(180)
                if abs(x1) < abs(y1) and y1 > 0 and (ghost.heading() == 180 or ghost.heading() == 0):
                    if [x, y - 1] not in walls:
                        ghost.setheading(90)
                if abs(x1) < abs(y1) and y1 < 0 and (ghost.heading() == 180 or ghost.heading() == 0):
                    if [x, y + 1] not in walls:
                        ghost.setheading(270)


    def ghostwall(ghost, playerx, playery):
        # Remember: x,y coords are 1 greater than their corresponding value in flags
        if ghost.isvisible() == True:
            x = 1000
            y = 1000
            gridon = False
            global ghostfwdamnt
            blx = ghost.xcor()
            bly = ghost.ycor()
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i]), 1):
                    if flags[i][j][0] == round(blx, 5) and flags[i][j][1] == round(bly, 5):
                        x = j + 1
                        y = i + 1
                        gridon = True
            if gridon == True:
                if ghost.heading() == 180:
                    if [x - 1, y] in walls:
                        if math.hypot(flags[y - 2][x - 1][0] - playerx, flags[y - 2][x - 1][1] - playery) > math.hypot(
                                        flags[y][x - 1][0] - playerx, flags[y][x - 1][1] - playery):
                            if [x, y + 1] not in walls:
                                ghost.setheading(270)
                            else:
                                ghost.setheading(90)
                        else:
                            if [x, y - 1] not in walls:
                                ghost.setheading(90)
                            else:
                                ghost.setheading(270)
                if ghost.heading() == 0:
                    if [x + 1, y] in walls:
                        if math.hypot(flags[y - 2][x - 1][0] - playerx, flags[y - 2][x - 1][1] - playery) > math.hypot(
                                        flags[y][x - 1][0] - playerx, flags[y][x - 1][1] - playery):
                            if [x, y + 1] not in walls:
                                ghost.setheading(270)
                            else:
                                ghost.setheading(90)
                        else:
                            if [x, y - 1] not in walls:
                                ghost.setheading(90)
                            else:
                                ghost.setheading(270)
                if ghost.heading() == 90:
                    if [x, y - 1] in walls:
                        if math.hypot(flags[y - 1][x - 2][0] - playerx, flags[y - 1][x - 2][1] - playery) > math.hypot(
                                        flags[y - 1][x][0] - playerx, flags[y - 1][x][1] - playery):
                            if [x + 1, y] not in walls:
                                ghost.setheading(0)
                            else:
                                ghost.setheading(180)
                        else:
                            if [x - 1, y] not in walls:
                                ghost.setheading(180)
                            else:
                                ghost.setheading(0)
                if ghost.heading() == 270:
                    if [x, y + 1] in walls:
                        if math.hypot(flags[y - 1][x - 2][0] - playerx, flags[y - 1][x - 2][1] - playery) > math.hypot(
                                        flags[y - 1][x][0] - playerx, flags[y - 1][x][1] - playery):
                            if [x + 1, y] not in walls:
                                ghost.setheading(0)
                            else:
                                ghost.setheading(180)
                        else:
                            if [x - 1, y] not in walls:
                                ghost.setheading(180)
                            else:
                                ghost.setheading(0)


    def ghostalign(ghost):
        gridon = False
        x = 10000
        y = 10000
        if round(abs(ghost.xcor()), 0) % 2 != 0:
            print(ghost.xcor())
            blx = ghost.xcor() + 21
            bly = ghost.ycor()
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i]), 1):
                    if flags[i][j][0] == round(blx, 5) and flags[i][j][1] == round(bly, 5):
                        x = j + 1
                        y = i + 1
                        gridon = True

            if [x ,y] not in walls:
                    ghost.goto(round(ghost.xcor()) + 1, ghost.ycor())
            else:
                    ghost.goto(round(ghost.xcor()) - 1, ghost.ycor())
            print(ghost.pos())
        if round(abs(ghost.ycor()), 0) % 2 != 0:
            print(ghost.ycor())
            blx = ghost.xcor()
            bly = ghost.ycor() + 21
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i]), 1):
                    if flags[i][j][0] == round(blx, 5) and flags[i][j][1] == round(bly, 5):
                        x = j + 1
                        y = i + 1
                        gridon = True

            if [x, y] not in walls:
                    ghost.goto(ghost.xcor(), ghost.ycor() + 1)
            else:
                    ghost.goto(ghost.xcor(), ghost.ycor() - 1)
            print(ghost.pos())

    def ghostfrightenedmove(ghost):
        if ghost.isvisible() == True:
            ghost.forward(ghostfwdamnt * 0.5)


    def ghostfrightenedseek(ghost):
        if ghost.isvisible() == True:
            # for ghost turning on intersections
            x = 100000
            y = 100000
            blx = ghost.xcor()
            bly = ghost.ycor()
            gridon = False
            # checks to find the greater of the differences in x,y coords between pl / ghost
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i])):
                    if flags[i][j][0] == round(blx, 5) and flags[i][j][1] == round(bly, 5):
                        x = j + 1
                        y = i + 1
                        gridon = True
            if gridon == True:
                directnum = random.randint(1, 2)
                if ghost.heading() == 0 or ghost.heading() == 180:
                    if directnum == 1:
                        if [x, y - 1] not in walls:
                            ghost.setheading(90)
                    else:
                        if [x, y + 1] not in walls:
                            ghost.setheading(270)
                if ghost.heading() == 90 or ghost.heading() == 270:
                    if directnum == 1:
                        if [x - 1, y] not in walls:
                            ghost.setheading(180)
                    else:
                        if [x + 1, y] not in walls:
                            ghost.setheading(0)


    def ghostfrightenedwall(ghost):
        # for ghost turning on intersections
        if ghost.isvisible() == True:
            x = 100000
            y = 100000
            blx = ghost.xcor()
            bly = ghost.ycor()
            gridon = False
            # checks to find the greater of the differences in x,y coords between pl / ghost
            for i in range(0, len(flags), 1):
                for j in range(0, len(flags[i])):
                    if flags[i][j][0] == round(blx, 5) and flags[i][j][1] == round(bly, 5):
                        x = j + 1
                        y = i + 1
                        gridon = True
            if gridon == True:
                directnum = random.randint(1, 2)
                if ghost.heading() == 0 and [x + 1, y] in walls:
                    if directnum == 1:
                        if [x, y - 1] not in walls:
                            ghost.setheading(90)
                        else:
                            ghost.setheading(270)
                    else:
                        if [x, y + 1] not in walls:
                            ghost.setheading(270)
                        else:
                            ghost.setheading(90)
                if ghost.heading() == 180 and [x - 1, y] in walls:
                    if directnum == 1:
                        if [x, y - 1] not in walls:
                            ghost.setheading(90)
                        else:
                            ghost.setheading(270)
                    else:
                        if [x, y + 1] not in walls:
                            ghost.setheading(270)
                        else:
                            ghost.setheading(90)
                if ghost.heading() == 90 and [x, y - 1] in walls:
                    if directnum == 1:
                        if [x + 1, y] not in walls:
                            ghost.setheading(0)
                        else:
                            ghost.setheading(180)
                    else:
                        if [x - 1, y] not in walls:
                            ghost.setheading(180)
                        else:
                            ghost.setheading(0)
                if ghost.heading() == 270 and [x, y + 1] in walls:
                    if directnum == 1:
                        if [x + 1, y] not in walls:
                            ghost.setheading(0)
                        else:
                            ghost.setheading(180)
                    else:
                        if [x - 1, y] not in walls:
                            ghost.setheading(180)
                        else:
                            ghost.setheading(0)


    def ghosteat(ghost, pl):
        global scorecounter
        global score
        global scoredisplay
        global lastscoredisplay
        global frightened
        if frightened == True:
            if pl.distance(ghost) < 15 and ghost.isvisible() == True:
                ghost.goto(round(flags[7][7][0]), flags[7][7][1])
                if ghost.heading() == 270:
                    ghost.setheading(0)
                winsound.PlaySound("pacman_eatghost.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
                ghost.ht()
                scorebot.goto(pl.pos())
                score += (2 ** scorecounter) * 200
                if scorecounter == 0:
                    scorebot.write('200', move=False, align="center", font=("comic sans", 9, "normal"))
                    lastscoredisplay = time.time()
                    scoredisplay = True
                if scorecounter == 1:
                    scorebot.write('400', move=False, align="center", font=("comic sans", 9, "normal"))
                    lastscoredisplay = time.time()
                    scoredisplay = True
                if scorecounter == 2:
                    scorebot.write('800', move=False, align="center", font=("comic sans", 9, "normal"))
                    lastscoredisplay = time.time()
                    scoredisplay = True
                if scorecounter == 3:
                    scorebot.write('1600', move=False, align="center", font=("comic sans", 9, "normal"))
                    lastscoredisplay = time.time()
                    scoredisplay = True
                    scorecounter = 0
                scorecounter += 1
        if time.time() - lastscoredisplay > 2:
                scoredisplay = False
                scorebot.clear()

    def scattercontrol():
        global lastscatterchange
        global scatter
        global scattertime
        if time.time() - lastscatterchange > 10 and scatter == True:
            scatter = False
            lastscatterchange = time.time()
        elif time.time() - lastscatterchange > 10 and scatter == False:
            scattertime = 10
            scatter = True
            lastscatterchange = time.time()

    def ghostspawn():
        global dotsgotten
        global clydein
        global inkyin
        global pinkyin
        global timeforspawn
        if time.time() - timeforspawn > 24 and clydein == False:
            clyde.goto(round(flags[7][7][0]), flags[7][7][1])
            clydein = True
        if time.time() - timeforspawn > 18 and inkyin == False:
            inky.goto(round(flags[7][7][0]), flags[7][7][1])
            inkyin = True
        if time.time() - timeforspawn > 10 and pinkyin == False:
            pinky.goto(round(flags[7][7][0]), flags[7][7][1])
            pinkyin = True

    # -----------Variables---------------------------------------
    lives = 3
    score = 0
    scorethen = 0
    scorecounter = 0
    scoredisplay = False

    plright = False
    plleft = False
    plup = False
    pldown = False
    uplater = False
    leftlater = False
    rightlater = False
    downlater = False

    ghostmaxfwd = 2
    frightened = False
    scatter = True
    lastscatterchange = time.time()
    chasetime = 10

    clydein = False
    inkyin = False
    pinkyin = False

    dotsgotten = 0

    frightenedstart = time.time()
    timeforspawn = time.time()
    lastdotchange = time.time()
    timestart = time.time()
    timesinceimage = timestart
    lastscoredisplay = time.time()

    lastfruitspawn = time.time()
    fruitout = False

    pacmanimageindex = 0

    # -----------Main Loop---------------------------------------
    wind.listen()

    wind.onkeypress(turnuplater, 'w')
    wind.onkeypress(turnleftlater, 'a')
    wind.onkeypress(turnrightlater, 'd')
    wind.onkeypress(turnldownlater, 's')

    winsound.PlaySound("pacman_beginning.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
    time.sleep(5)

    levelbot.write('Level ' + str(levelcount), move=False, align="center", font=("Terminal", 12, "bold"))

    while dotsgotten != totaldots and lives > 0:
        # game functions
        scoring()

        fruitspawn()
        if fruitout == True:
            ghostfrightenedwall(fruitbot)
            fruitbot.forward(1)
        fruitget()

        # player functionsa
        playermove()
        plleftwall(pl)
        plrightwall(pl)
        pltopwall(pl)
        pldownwall(pl)
        playerup()
        playerright()
        playerdown()
        playerleft()
        playerwrap()

        pacmanimation()


        # dot functions
        for i in range(0, len(dots), 1):
            dotget(dots[i], pl)
        for i in range(0, len(powerdots), 1):
            powerdotget(powerdots[i], pl)

        # ghost functions
        ghostspawn()
        ghostwrap(blinky)
        ghostwrap(pinky)
        ghostwrap(inky)
        ghostwrap(clyde)
        if frightened == False:
            if scatter == False:
                ghostmove(blinky)
                ghostseek(blinky, pl.xcor(), pl.ycor())
                ghostwall(blinky, pl.xcor(), pl.ycor())

                if pinkyin == True:
                    ghostmove(pinky)
                    pinkymove()

                if inkyin == True:
                    ghostmove(inky)
                    inkymove()

                if clydein == True:
                    ghostmove(clyde)
                    clydemove()


            else:
                ghostseek(blinky, -160, 200)
                ghostwall(blinky, -160, 200)
                ghostmove(blinky)
                if pinkyin == True:
                    ghostseek(pinky, 160, 200)
                    ghostwall(pinky, 160, 200)
                    ghostmove(pinky)
                if inkyin == True:
                    ghostseek(inky, -160, -200)
                    ghostwall(inky, -160, -200)
                    ghostmove(inky)
                if clydein == True:
                    ghostseek(clyde, 160, -200)
                    ghostwall(clyde, 160, -200)
                    ghostmove(clyde)
            blinkyanimation()
            pinkyanimation()
            inkyanimation()
            clydeanimation()
            playerdeath(pl, blinky)
            if pinkyin == True:
                playerdeath(pl, pinky)
            if inkyin == True:
                playerdeath(pl, inky)
            if clydein == True:
                playerdeath(pl, clyde)
        else:
            ghostfrightenedseek(blinky)
            ghostfrightenedwall(blinky)
            ghostfrightenedmove(blinky)
            if pinkyin == True:
                ghostfrightenedmove(pinky)
                ghostfrightenedseek(pinky)
                ghostfrightenedwall(pinky)


            if inkyin == True:
                ghostfrightenedmove(inky)
                ghostfrightenedseek(inky)
                ghostfrightenedwall(inky)


            if clydein == True:
                ghostfrightenedmove(clyde)
                ghostfrightenedseek(clyde)
                ghostfrightenedwall(clyde)

        ghosteat(blinky, pl)
        ghosteat(pinky, pl)
        ghosteat(inky, pl)
        ghosteat(clyde, pl)
        scattercontrol()
        time.sleep(dotsgotten / totaldots * 0.015)
        wind.update()
    if lives <= 0:
        winning = False
    else:
        levelcount += 1
        ghostfwdamnt *= 2
        scattertime *= 0.6
        for i in range(0, len(dots), 1):
            dots[i].st()
        for i in range(0, len(powerdots), 1):
            powerdots[i].st()
        wind.update()
gameover.goto(flags[11][7][0], flags[11][7][1])
gameover.st()
wind.update()


wind.exitonclick()