import random
import subprocess
eg=("Mampf","Oh yes","tasty","so creamy!","What a taste","That nutriens!","I love this food","Thats so jummy")
gg=("Wow so much money!","How beautifull this coins are","Yes, im going to be rich","Katching","Kling","Pling","Klirr","How this coins shine")
kg=("Du Opfer!","Ich habe dich zerstört","Du Lappen","Meine Oma könnte dich besiegen","Du Lauch","Hahahha du Schwächling","Du Hundesohn")
#Dungeon Spiel Adam
dungeon="""
############################################################################
#...................T#..................#......d.........€........d........#
###..........###############....d..#....#..€.#.......d.########............#
#<o....d...........#....#....d.....#....d....#.....#####T....s#.........s..#
##########.........#.T..#....#######################..........#....s.G.....#
#?..s....#....G....#....#..d.#.........d........s.........s...#............#
#.....####..€......#....#....#..€.############.......d...............d.....#
#..s..#........d...#...d.....#....#.T..#..s..#....s.....G..s...d....€....s.#
#.....#......................#.d..#..........#......s......................#
#..d..#..G...#################....#.s..#.....#.........#####################
#.....#...................K.....s.#....#..€...####w.s..#s..............#k..#
#.....#####..€d....s......#########....#......w........#...............###.#
#...K............#########.d...s........s.........s..s.#....s...s..........#
#.....#############....................s...€..#.......##.............B.....#
#...d.##d.........#...G......#.....G..........#.w..s............ ..........#
#?....##?...#.......€...s....#..s....s........#...........s...........s...s#
############################################################################
"""
dungeon1="""
############################################################################
#<o.........#....ss....#...ss...#....ss...#........s......d...............k#
###......w...#....ss....#...ss...#....ss...#.......................d..Z.....#
#>..........#....ss....#...ss...#....ss...#......s...s........d............#
######....######....######....######....######....##########################
#.?..#.w...#..T.#....#.T..#....#..T.#....#.?..#....#.T..#....#.T..#....#.?.#
#....#....#....#....#....#....#....#....#....#....#....#....#....#....#....#
#..w.#....#..w.#....#..w.#....#.w..#....#..w.#....#..w.#..w .#....#....#....#
#....#..K.#....#....#....#....#....#....#....#....#....#....#....#....#....#
#..K.##...##.K.##...##.K.##...##.K.##...##.K.##...##.K.##...##.K.##...##.K.#
#..w..##.w..##.w.##.d.##...##.d.##...##.d.##...##...##...##...##...##...##.#
#......##...##...##...##...##...##..w##...##...##.w.##...##...##...##..w...#
#.......##...##...##.d.##..w##.d.##...##.d.##.w.##...##w..##...##...##.....#
#....w...##...##...##...##...##...##...##...##...##...##...##...##...##....#
#...........w....w................w........w.........s....s.....s....s.....#
#............G..........K.w...........G..................G................d#
############################################################################
"""
dungeon2="""
############################################################################
#>...........d..........d...............s..........s......s............s...#
#............####....####...............###....####..........###...###.....#
#..d......d..#...s......#...............#.........#.....s....#G.....G#.s...#
#............#..........#.......dGd.....#..w......#..........#.......#.....#
##############....B.....#################....Z....############...s...#######
#............#..........#........K.....#.........#..........#.......#k....#
#.s..#...G...#K........K#.......#..#...##G.......G#......#...#K.....K#.....#
#....###.....####....####.w...###s.##...###..s.####.G...##...###...###.....#
#......#........#....#........#.....##s...#....#........#......#...s.......#
#......#####...?#..s.#?...#####......#...?#....#?...#####..#..T#......G....#
#...s......######....######..w...K....######....######......#####..........#
#........#.....K...##......s....#..#.........##......s..G.........s........#
#...K....##......####..##w##...#..#....w...####...........##################
#.........##...w....s..##.##..w####..s.....s.......########.....Z..........#
#..........##......w........w...K...........G.......o............B........E#
############################################################################
"""
hero="@"
herox=1
heroy=2
heroz=0
herogold=0
food=0
herokey=0
herohunger=-1
hitpoints=50
gorilla="G"
kobold="K"
ende="E"
bossgorillakobold="B"
trapmonster="T"
bosszombie="Z"
#level=list(dungeon)
level=[]
for d in (dungeon,dungeon1,dungeon2):
    l=[]
    for line in d.splitlines():
        l.append(list(line))
    level.append(l)
    
while herohunger <30:
    herohunger+=random.choice((0,0,0,1,1,1,2,2))
    if herohunger >25:
        subprocess.call(("espeak","EAT SOMETHING IM HUNGRY"))
    #for x,c in enumerate(level):
     #   if x==herox:
      #      print(hero,end="")
       # else:
        #    print(c,end="")
    #print()
    for y, line in enumerate(level[heroz]):
        for x,c in enumerate(line):
            if x==herox and y==heroy:
                print(hero,end="")
            else:
                print(c,end="")
        print()
    command=input("Gold: {} Food {} Hunger {} Leben {} Schlüssel {} Was willst du jetzt tun?".format(herogold,food,herohunger,hitpoints,herokey))
    dx=0
    dy=0
    if command=="a":
        #herox-=1
        dx=-1
    if command=="Zaubertrank":
        if hitpoints < 51:
            hitpoints+=50
    if command=="flyup":
        if heroz==0:
            print("Du kannst nicht weiter nach oben")
        else:
            heroz-=1
    if command=="flydown":
        if heroz==len(level)-1:
            print("Du bist schon im untersten Level")
        else:
            heroz+=1
    if command=="d":
        #herox+=1
        dx=1
    if command=="s":
        dy=1
    if command=="w":
        dy=-1
    if command==" ":
        #herox+=2
        dx=2
    if command=="f":
        if food > 0:
           food-=1
           herohunger-=random.choice((3,3,4,4,4,4,4,5,5,5,5,5))
           # print(random.choice(eg))
           g=random.choice(eg)
           subprocess.call(("espeak",g))
           print(g)
        else:
            print("Oje, ich habe kein Essen mehr!")
           #andere art
        #food -= 2
        #food = max(0,food)
        # -----in wand gelaufen-----
    target=level[heroz][heroy+dy][herox+dx]
    if target=="#":
        dx=0
        dy=0
        #print("Autsch, ich bin in eine Mauer gelaufen!")
        subprocess.call(("espeak","Autsch, i ran into a wall"))
    elif target=="o":
        if herokey > 0:
            herokey-=1
            level[heroz][heroy][herox]="."
        else:
            subprocess.call(("espeak","Autsch, i ran into a door"))
            dx=0
            dy=0
    # in Monster gelaufen?
    #target=level[herox+dx]
    #------ Gorilla anfang-----
    if target=="G":
        print("Ein Gorilla blockiert deinen Weg!")
        print("Der Gorilla schlägt dich mit einer Banane!")
        subprocess.call(("espeak","Buuuum"))
        schaden=random.randint(1,10)
        hitpoints -=schaden
        print("Du erleidest {} Schaden".format(schaden))
        if hitpoints <1:
            print("Du Stirbst! VERSAGER!")
            break
        sieg=0.5
        if random.random() < sieg:
             print("DU GEWINNST!")
             level[heroz][heroy+dy][herox+dx]="."
        else:
            print("DU VERLIERST")
            dx=0
            dy=0
    #-----Gorilla ende----
    #------ Kobold anfang-----
    if target=="K":
        print("Ein Kobold schnellt auf dich zu!")
        print("Der Kobold schlägt dich mit einem rostigen Dolch!")
        subprocess.call(("espeak","Schlitz"))
        schaden=random.randint(10,17)
        hitpoints -=schaden
        print("Du erleidest {} Schaden".format(schaden))
        if hitpoints <1:
            print("Du Stirbst! VERSAGER!")
            break
        sieg=0.7
        if random.random() < sieg:
             print("DU GEWINNST!")
             level[heroz][heroy+dy][herox+dx]="."
        else:
            subprocess.call(("espeak",random.choice(kg)))
            dx=0
            dy=0
    #-----Kobold ende----
    #------ Bossgorillakobold anfang-----
    if target=="B":
        print("Der böse Bossgorillakobold verstellt dir die Sicht auf die wunderschöne Prinzessin!")
        print("Der böse Bossgorillakobold schlägt dich mit einem rießigen Bananenbaumschwert")
        subprocess.call(("espeak","explosion over 9000"))
        schaden=random.randint(10,30)
        hitpoints -=schaden
        print("Du erleidest {} Schaden".format(schaden))
        if hitpoints <1:
            print("Du Stirbst! VERSAGER!")
            break
        sieg=0.4
        if random.random() < sieg:
             print("DU GEWINNST!")
             level[heroz][heroy+dy][herox+dx]="."
        else:
            print("DU VERLIERST")
            dx=0
            dy=0
    #-----Bossgorillakobold ende----
    #------ Trap anfang-----
    if target=="T":
        print("Nanu, die Kiste bewegt sich!!")
        print("Ein Kistenmonster springt dich an und beißt dich mit seinen Zähnen")
        subprocess.call(("espeak","oh my godness"))
        schaden=random.randint(1,30)
        hitpoints -=schaden
        print("Du erleidest {} Schaden".format(schaden))
        if hitpoints <1:
            print("Du Stirbst! VERSAGER!")
            break
        sieg=0.8
        if random.random() < sieg:
             print("DU GEWINNST!")
             level[heroz][heroy+dy][herox+dx]="."
        else:
            print("DU VERLIERST")
            dx=0
            dy=0
    #-----Trap ende----
    #------ Bosszombie anfang-----
    if target=="Z":
        print("Das böse Bosszombie breitet sich auf dem Gang aus")
        print("Das böse Bosszombie schlägt dich mit einem rostigen Hammer")
        subprocess.call(("espeak","kabuuuuuum"))
        schaden=random.randint(10,30)
        hitpoints -=schaden
        print("Du erleidest {} Schaden".format(schaden))
        if hitpoints <1:
            print("Du Stirbst! VERSAGER!")
            break
        sieg=0.35
        if random.random() < sieg:
             print("DU GEWINNST!")
             level[heroz][heroy+dy][herox+dx]="."
        else:
            print("DU VERLIERST")
            dx=0
            dy=0
    #-----Bosszombie ende----  
    herox+=dx
    heroy+=dy  
    #Aufheben
    stuff=level[heroz][heroy][herox]
    if stuff=="€":
        herogold+=1
        level[heroz][heroy][herox]="."
        #print(random.choice(gg))
        m=random.choice(gg)
        subprocess.call(("espeak",m))
    if stuff=="w":
        food+=1
        level[heroz][heroy][herox]="."
    if stuff=="s":
        food+=3
        level[heroz][heroy][herox]="."
    if stuff=="k":
        herokey+=1
        level[heroz][heroy][herox]="."
    if stuff=="<":
        c2=input("Willst du in den nächsten Dungeon gehen?")
        if c2=="yes":
            heroz+=1
    if stuff==">":
        c2=input("Willst du in den vorherigen Dungeon gehen?")
        if c2=="yes":
            heroz-=1
    if stuff=="d":
        food+=2
        level[heroz][heroy][herox]="."
    if stuff=="E":
        print("Bravo du hast es Geschafft!")
        subprocess.call(("espeak","Congratulations you saved the princess and made the world a better place"))
print("Game Over")
subprocess.call(("espeak","Game Over"))
        
        
        
        
    
            
