import random
eg=("Mampf","Mhhhm","Lecker","Schleckmaja","So Saftig!","Was für ein Geschamck","Diese Nährstoffe!","Ich liebe dieses Essen","Das ist ja soo Cremig")
gg=("Boah SO viel Geld!","So schöne Münzen","Jaaa, ich werde Reich","Katching","Kling","Pling","Klirr","Wie die Münzen funkeln!")
#Dungeon Spiel Adam
dungeon="....w....w...w.O.€..w..d....O.€...w..O.€...w...O.s...€...w...w...O.€..w...B.€.E"
hero="@"
herox=0
herogold=0
food=0
herohunger=-1
monster="O"
bossmonster="B"
ende="E"
level=list(dungeon)
while herohunger <30:
    herohunger+=random.choice((0,0,1,1,1,2))
    for x,c in enumerate(level):
        if x==herox:
            print(hero,end="")
        else:
            print(c,end="")
    print()
    command=input("Gold: {} Food {} Hunger {} Was willst du jetzt tun?".format(herogold,food,herohunger))
    if command=="a":
        herox-=1
    if command=="d":
        herox+=1
    if command==" ":
        herox+=2
    if command=="f":
        if food > 0:
           food-=1
           herohunger-=random.choice((2,2,3,3,3,4,4,4,4,4))
           print(random.choice(eg))
        else:
            print("Oje, ich habe kein Essen mehr!")
           #andere art
        #food -= 2
        #food = max(0,food)
    #Aufheben
    stuff=level[herox]
    if stuff=="€":
        herogold+=1
        level[herox]="."
        print(random.choice(gg))
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
        break
        
        
        
        
    
            
