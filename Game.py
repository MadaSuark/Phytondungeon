import random
import subprocess
eg=("Mampf","Oh yes","tasty","Schleckmaja","so creamy!","What a taste","That nutriens!","I love this food","Thats so jummy")
gg=("Wow so much money!","How beautifull this coins are","Yes, im going to be rich","Katching","Kling","Pling","Klirr","How this coins shine")
#Dungeon Spiel Adam
dungeon="....w....w...w.G.€..w..d.K...G.€...w..G.€...w...G.s...€..K.w...w...G.€..w...B.€.E"
hero="@"
herox=0
herogold=0
food=0
herohunger=-1
hitpoints=50
gorilla="G"
kobold="K"
ende="E"
bossgorillakobold="B"
level=list(dungeon)
while herohunger <30:
    herohunger+=random.choice((0,0,1,1,1,2,2,2))
    for x,c in enumerate(level):
        if x==herox:
            print(hero,end="")
        else:
            print(c,end="")
    print()
    command=input("Gold: {} Food {} Hunger {} Leben {} Was willst du jetzt tun?".format(herogold,food,herohunger,hitpoints))
    dx=0
    if command=="a":
        #herox-=1
        dx=-1
    if command=="Zaubertrank":
        if hitpoints < 51:
            hitpoints+=50
    if command=="d":
        #herox+=1
        dx=1
    if command==" ":
        #herox+=2
        dx=2
    if command=="f":
        if food > 0:
           food-=1
           herohunger-=random.choice((2,3,3,3,4,4,4,4,4))
           # print(random.choice(eg))
           g=random.choice(eg)
           subprocess.call(("espeak",g))
           print(g)
        else:
            print("Oje, ich habe kein Essen mehr!")
           #andere art
        #food -= 2
        #food = max(0,food)
    # in Monster gelaufen?
    target=level[herox+dx]
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
             level[herox+dx]="."
        else:
            print("DU VERLIERST")
            dx=0
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
             level[herox+dx]="."
        else:
            print("DU VERLIERST")
            dx=0
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
        sieg=0.3
        if random.random() < sieg:
             print("DU GEWINNST!")
             level[herox+dx]="."
        else:
            print("DU VERLIERST")
            dx=0
    #-----Bossgorillakobold ende----
    herox+=dx    
    #Aufheben
    stuff=level[herox]
    if stuff=="€":
        herogold+=1
        level[herox]="."
        #print(random.choice(gg))
        m=random.choice(gg)
        subprocess.call(("espeak",m))
    if stuff=="w":
        food+=1
        level[herox]="."
    if stuff=="s":
        food+=3
        level[herox]="."
    if stuff=="d":
        food+=2
        level[herox]="."
    if stuff=="E":
        print("Bravo du hast es Geschafft!")
        subprocess.call(("espeak","Congratulations you saved the princess and made the world a better place"))
print("Game Over")
subprocess.call(("espeak","Game Over"))
        
        
        
        
    
            
