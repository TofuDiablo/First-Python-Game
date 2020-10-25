#This game was made by me, James La La Land.
import time
import random
import sys
def s():
    print ("")

#player base stats
p_hlth = 10
p_str = 2
p_lk = 1

#stat changes
#def st_ch():
    
#enemy combat
in_cmb = False
enemy = 0
e_sln = 1

#enemy stats
e_H = 0
e_S = 0
e_L = 0
def e_St():
    print ("Enemy Health: " + str(e_H))
    print ("Enemy Strength: " + str(e_S))
    print ("Enemy Luck: " + str(e_L))
#^display enemy stats

print ("Hello, what is your name?")
time.sleep(.5)
userName = str(input("My name is: "))
time.sleep(.5)
print ("Greetings, " + userName + "!")

s()

print ("Welcome to a one way trip to |H E C K|")
time.sleep(.5)
print ("This is basically just a game of seeing how far you can")
time.sleep(.5)
print ("get, honestly. There is no real end to the game.")
time.sleep(.5)
print ("Also, you can't save, but you can end your own run.")
time.sleep(.75)
print ("Wait, wait...")
time.sleep(2.25)
print ("Oh right!")
s()

#time.sleep(.5)
time.sleep(1)
print ("You're going to be fighting monsters and such.")
print ("So, would you like more health or more strength?")

#player choice
player_choice = ""
def pChoo():
    global player_choice
    player_choice = str(input("I choose... "))
    return player_choice

#choosing = 0

#beginning stat boost
def sA():
    global p_hlth
    global p_str
    global p_lk
    playC = pChoo()
    if playC == "health" or playC == "Health":
        print ("Tada! You get more strength!")
        p_str += 3
    elif playC == "strength" or playC == "Strength":
        print ("Tada! You get more health!")
        p_hlth += 6
    elif playC == "both" or playC == "Both":
        print ("Tada! You get easier to kill!")
        p_hlth -= 3
        p_str = 1
        p_lk = 0
    elif playC == "LaLaLand":
        p_hlth = 9001
        p_str = 9001
    else:
        print ("I said health or strength.")
        time.sleep(.5)
        sA()
time.sleep(.5)
sA()

#def norm():
    
#player menu
def menu():
    global userName
    s()
    print ("MENU:")
    time.sleep(.5)
    print ("-Stats")
    print ("-Inventory")
    print ("-Exit Menu")
    time.sleep(.5)
    s()
    print ("What would you like to do?")
    time.sleep(.5)
    playC = pChoo()
    if playC == "Stats" or playC == "stats":
        s()
        print (userName + "'s STATS:")
        print ("Health: " + str(p_hlth))
        print ("Strength: " + str(p_str))
        print ("Luck: " + str(p_lk))
        menu()
    elif playC == "Inventory" or playC == "inventory":
        #inv()
        print ("HA! You thought you had something.")
        menu()
    elif playC == "Exit" or playC == "exit":
        print ("Exiting Menu.")
    elif playC == "Exit Menu" or playC == "exit menu":
        print ("Exiting Menu.")
    else:
        print ("Choose stats, inventory, or exit.")
        time.sleep(.5)
        menu()

time.sleep(1)

level = 0

#enemy random stat generation
def dung_e():
    global e_H
    global e_S
    global e_L
    global level
    global p_lk
    global enemy
    if p_lk > 0 and p_lk < 3:
        e_L = random.randint(-p_lk,2)
    elif p_lk == 0:
        e_L = random.randint(0,2)
    if e_L == 0 or e_L < 0:
        e_H = random.randint(0, ((4 + level) - random.randint(p_lk, 2)))
    elif e_L > 0:
        e_H = random.randint(e_L, ((4 + level) - random.randint(p_lk, 2)))
    if e_L < (3 - p_lk) or e_L == (3 - p_lk):
        e_S = random.randint(e_L, (3 - p_lk))
    elif e_L > (3 - p_lk):
        e_S = (e_L, 3)
    enemy = 1

#monster fighting
def mon_fi():
    global player_choice
    global e_H
    global e_S
    global e_L
    global p_hlth
    global p_str
    global p_lk
    global in_cmb
    global enemy
    global p_atk
    global e_atk
    global p_atk_h
    global e_atk_h
    global e_sln
    global intro_fi
    s()
    if enemy == 0:
        dung_e()
    if in_cmb == False and e_H == 0:
        time.sleep(.25)
        print ("Oh my!")
        print ("You've encountered an enemy!")
        time.sleep(.5)
        s()
        print ("Wait, he's already dead...")
        time.sleep(.75)
        print ("I guess you win then.")
        s()
        intro_fi = False
        dung()
    in_cmb = True
    if p_hlth == 0 or p_hlth < 0:
        print ("you dead lol...")
    elif in_cmb == True and e_H > 0:
        mon_fi_m()
    elif in_cmb == True and e_H < 0 or e_H == 0:
        in_cmb = False
        enemy = 0
        intro_fi = False
        e_sln += 1
        print ("You won the battle!")
        dung()
    
#introduced to fight
intro_fi = False

#attacks
p_atk = 0
p_atk_h = False
e_atk = 0
e_atk_h = False

#hit or miss
def pHoM():
    justavariable = random.randint(p_lk, 1)
    if justavariable == 0:
        justavariable = False
    elif justavariable == 1:
        justavariable = True
    return justavariable
def eHoM():
    justavariable = random.randint(e_L, 2)
    if justavariable == 0 or justavariable < 0:
        justavariable = False
    elif justavariable > 0:
        justavariable = True
    return justavariable

def mon_fi_m():
    s()
    global userName
    global e_H
    global e_S
    global e_L
    global p_hlth
    global p_str
    global p_lk
    global p_atk
    global e_atk
    global p_atk_h
    global e_atk_h
    global intro_fi
    global in_cmb
    global enemy
    if intro_fi == False:
        print ("Oh my!")
        print ("You've encountered an enemy!")
        intro_fi = True
        s()
    e_St()
    s()
    print ("COMBAT:")
    time.sleep(.5)
    print ("-Fight")
    print ("-Stats")
    print ("-Inventory")
    print ("-Run")
    s()
    pChoo()
    if player_choice == "fight" or player_choice == "Fight":
        print ("The monster tries to hit you!")
        e_atk_h = eHoM()
        e_atk = random.randint(e_L, e_S)
        if e_atk_h == False:
            print ("he missed...")
            time.sleep(.5)
        elif e_atk == 0:
            print ("he missed...")
            time.sleep(.5)
        elif e_atk < 0:
            p_hlth -= e_atk
            print ("It accidentally healed you...")
            time.sleep(1)
            print ("You gain " + str(-e_atk) + " health.")
            time.sleep(.5)
        elif e_atk > 0:
            p_hlth -= e_atk
            print ("You lose " + str(e_atk) + " health.")
            time.sleep(.5)
        s()
        print ("You attempt to attack the monster!")
        p_atk_h = pHoM()
        p_atk = random.randint(p_lk, p_str)
        if p_atk_h == False:
            print ("aaaaaannnd you missed...")
            time.sleep(.5)
        elif p_atk > 0:
            e_H -= p_atk
            print ("It loses " + str(p_atk) + " health.")
            time.sleep(.5)
        mon_fi()
    elif player_choice == "stats" or player_choice == "Stats":
        s()
        print (userName + "'s STATS:")
        print ("Health: " + str(p_hlth))
        print ("Strength: " + str(p_str))
        print ("Luck: " + str(p_lk))
        mon_fi()
    elif player_choice == "inventory" or player_choice == "Inventory":
        print ("You don't magically get items, ya know.")
        mon_fi_m()
    elif player_choice == "Run" or player_choice == "run":
        ohboyihopethisaintbeenused = random.randint(p_lk, 5000)
        if ohboyihopethisaintbeenused == 1:
            print ("You got away this time, " + userName + "!")
            in_cmb = False
            enemy = 0
            intro_fi = False
        elif ohboyihopethisaintbeenused > 1:
            print ("You tried, but like, he caught up.")
            mon_fi_m()
    else:
        print ("Choose: Fight, inventory, or run")
        mon_fi_m()

#mage interactions menu
def mage_menu():
    global p_lk
    global p_hlth
    magic_hurts = pChoo()
    s()
    time.sleep(.5)
    if magic_hurts == "back away slowly" or magic_hurts == "Back away slowly":
        print ("You carefully assume the Spiderman Stance,")
        # https://drive.google.com/file/d/1dCKgsWpfAEnh2sVJFDkavHcy-jTDuD5c/view?usp=sharing
        print ("and you slowly back away from the mage.")
        s()
        time.sleep(0.5)
        print ("DUNGEON:")
        time.sleep(0.5)
        print ("-Explore")
        print ("-Menu")
        print ("-Quit Game")
        time.sleep(0.5)
        s()
        dung_m()
    elif magic_hurts == "ask for help" or magic_hurts == "Ask for help":
        print ("You beg for the mage's assistance.")
        time.sleep(.2)
        print ("Mage: ...")
        time.sleep(.75)
        qk_var = random.randint(p_lk, 2)
        if qk_var == 2:
            print ("The mage takes pity and grants you health.")
            h_gain = random.randint(p_lk + 1, 10)
            p_hlth += h_gain
            print ("Your health increases by " + str(h_gain) + " points.")
            time.sleep(.3)
            s()
            print ("He disappears in a wisp of smoke.")
        elif qk_var < 2:
            print ("The mage does not respond.")
            time.sleep(.25)
            print ("The mage disappears into a wisp of smoke.")
        s()
        time.sleep(0.5)
        print ("DUNGEON:")
        time.sleep(0.5)
        print ("-Explore")
        print ("-Menu")
        print ("-Quit Game")
        time.sleep(0.5)
        s()
        dung_m()
    elif magic_hurts == "fight" or magic_hurts == "Fight":
        print ("You challenge the mage to a fight, and he accepts.")
        time.sleep(.2)
        print ("...")
        time.sleep(.75)
        print ("Well, your life ended.")
    else:
        print ("Not a valid option.")
        time.sleep(.1)
        print ("Try again")
        mage_menu()
    

#dungeon menu
def dung_m():
    global level
    global p_lk
    playC = pChoo()
    if playC == "explore" or playC == "Explore":
        level += 1
        heylookitissomerandomvariable = random.randint(p_lk,20)
        if heylookitissomerandomvariable == 20:
            s()
            print ("You've run into a mage!")
            s()
            time.sleep(.5)
            print ("MAGE:")
            time.sleep(.25)
            print ("-Fight")
            print ("-Ask for help")
            print ("-Back away slowly")
            time.sleep(.7)
            s()
            mage_menu()
        elif heylookitissomerandomvariable == 19 or heylookitissomerandomvariable == 18:
            s()
            print ("In TRUE introverted fashion, you've avoided any sort")
            print ("of physical interaction... noice.")
            dung()
        elif heylookitissomerandomvariable < 18:
            mon_fi()
        #print "heh, not coded yet"
        #dung_m()
    elif playC == "Menu" or playC == "menu":
        menu()
        s()
        time.sleep(0.5)
        print ("DUNGEON:")
        time.sleep(0.5)
        print ("-Explore")
        print ("-Menu")
        print ("-Quit Game")
        time.sleep(0.5)
        s()
        dung_m()
    elif playC == "Quit Game" or playC == "quit game":
        time.sleep(.75)
        s()
        print ("Oh man, you got smited and died.")
        time.sleep(.25)
        print ("...")
        time.sleep(2)
        print ("Rest in peace, bud.")
    elif playC == "Quit" or playC == "quit":
        time.sleep(.75)
        s()
        print ("Oh man, you got smited and died.")
        time.sleep(.25)
        print ("...")
        time.sleep(2)
        print ("Rest in peace, bud.")
    else:
        print ("Yo, it's: explore, menu, or quit.")
        dung_m()

#heh, dung.
def dung():
    if level > 0:
        print ("Back to the dungeon!")
        s()
    elif level == 0:
        s()
        print ("On to the dungeon!")
        time.sleep(1.1)
        print ("Oh yeah, you're stuck in a dungeon and there's no exit.")
        time.sleep(.75)
        print ("Good luck and try to have fun, " + userName + "!")
    s()
    time.sleep(0.5)
    print ("DUNGEON:")
    time.sleep(0.5)
    print ("-Explore")
    print ("-Menu")
    print ("-Quit Game")
    time.sleep(0.5)
    dung_m()

d_trv = 0
e_sln = 0

dung()

d_trv = level

time.sleep(.5)
s()
print (userName + "'s Final Stats:")
time.sleep(.5)
print ("Progress Made: " + str(d_trv) + " level(s)")
time.sleep(.5)
print ("Enemies Slain: " + str(e_sln))
time.sleep(.5)
print ("Items Found: " + str(0))
time.sleep(.5)
print ("Strength: " + str(p_str))
time.sleep(.5)
print ("Luck: " + str(p_lk))
