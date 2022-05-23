import random
import time
from tkinter import *
  
# classes
class Character(object):
    def __init__(self, name, attack, pp, hp, mp):
        self.name = name
        self.attack = attack
        self.pp = pp
        self.hp = hp
        self.mp = mp


class Enemy(object):
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp


elemental_name = ['Chi', 'Mizu', 'Ka', 'Fu']
# (name, attack, pp, hp, mp)
bartek = Character('bartek', 150, 120, 200, 120)
maciek = Character('maciek', 180, 50, 125, 120)
hubert = Character('hubert', 100, 100, 150, 300)
the_player = Character('gracz',
                       random.randint(60, 150), random.randint(50, 150),
                       random.randint(80, 150), random.randint(50, 150))
charlist = [bartek, maciek, hubert, the_player]

# bosses
monster = Enemy('Blemish', 20, random.randint(1500, 2000))
monster2 = Enemy('Orc General', 30, random.randint(2000, 2550))
monster3 = Enemy('The Dark Lord', 40, random.randint(2000, 3000))
monlist = [monster, monster2, monster3]

# enemies
ooze = Enemy('Ooze', 20, 500)
skeleton = Enemy('Skeleton', 30, 500)
orc = Enemy('Orc', 40, 3000)
small_spider = Enemy('Spider', 20, 300)
goblin = Enemy('Goblin', 60, 2000)
bats = Enemy('Bat', 14, 655)
ghost = Enemy('Hunger Ghost', 50, 700)
snakes = Enemy('Snakes', 45, 450)
rock = Enemy('Magic Rock', 5, 10)
mushroom = Enemy('Mushroom', 10, 400)
agent = Enemy('Real Estate Agent', 25, 600)


def heal(person):
    if person.pp > 0:
        recovered = (person.mp + person.attack) * 0.5
        person.pp -= 5
        return round(recovered)
    else:
        print(person.name + ' nie ma punktow sily.')


def action_statement(person, action):
    print(person.name, action + '!')


def att(p1):
    attack = p1.attack + random.randint(2,6)
    return attack


def mag(p1):
    if p1.pp > 0:
        magic = (p1.attack + p1.mp) + random.randint(2, 3)
        p1.pp -= 5
        return magic
    else:
        print(p1.name+' nie ma juz punktow sily!!')


def mon_att(mon, p1, p2, p3, p4):
    crit = random.randint(1, 100)
    turn = 0
    if crit > 20:
        num = random.randint(1, 11)

        if num == 1 or num == 5:
            dmg = att(mon)
            p1.hp -= dmg
            print('>wrog atakuje ' + p1.name)
            turn += 1
        elif num == 2 or num == 6:
            dmg = att(mon)
            p2.hp -= dmg
            print('>wrog atakuje ' + p2.name)
            turn += 1
        elif num == 3 or num == 7:
            dmg = att(mon)
            p3.hp -= dmg
            print('>wrog atakuje ' + p3.name)
            turn += 1
        elif num == 4 or num == 8:
            dmg = att(mon)
            p4.hp -= dmg
            print('>wrog atakuje ' + p4.name)
            turn += 1
        else:
            print(">wrog nie trafil!!")
            turn += 1
    else:
        dmg = mon.attack * 4
        elemental = elemental_name[random.randint(0, 3)]
        print(mon.name + ' uzyl ' + elemental + ' ataku!')
        if elemental == elemental_name[0] or elemental_name[2]:
            p1.hp -= dmg
            p3.hp -= dmg

        elif elemental == elemental_name[1] or elemental_name[3]:
            p2.hp -= dmg
            p4.hp -= dmg


def player_status(person):
    print(person.name + " | HP = " + str(person.hp)
          + " | PP = " + str(person.pp))


def player_moves(player, mon, p2, p3, p4):
    turn = True
    attack = ['a', 'attack', 'Attack']
    magic = ['m', 'magic', 'MAGIC', 'Magic']
    heals = ['h', 'heal', 'HEAL', 'Heal']
    skip = ['skip', 's', 'SKIP']
    while turn:
        if player.hp < 0:
            print(player.name+' nie moze juz walczyc.')
            turn = False
        else:
            action = input('co zrobi ' + player.name
                               + ' (Attack, Magic, Heal, Skip): ')

            if action in attack:
                damage = att(player)
                mon.hp -= damage
                print(player.name + ' zadal ' + str(damage) + ' obrazen.')
                turn = False
            elif action in magic:
                try:
                    damage = mag(player)
                    mon.hp -= damage
                    print(player.name + ' zadal ' + str(damage))
                    turn = False
                except:
                    print
            elif action in skip:
                print(player.name + ' postanowil przeczekac.')
                turn = False
            elif action in heals:
                try:
                    print("kogo bys chcial aby " + player.name + " uleczyl?")
                    print("1: bartka  |  2: macka  |  3: huberta  |  4: ciebie")

                    user_heal = input('kogo uleczy? (podaj numer): ')
                    if user_heal == 'ciebie' or user_heal == player.name or user_heal == '1':
                        recovered = heal(player)
                        player.hp += recovered
                        action_statement(player, 'uzdrowil siebie ' + ' ' + str(recovered))
                        turn = False
                    elif user_heal == p2.name or user_heal == '2':
                        recovered = heal(player)
                        p2.hp += recovered
                        action_statement(player, 'uzdrowil ' + p2.name + ' ' + str(recovered))
                        turn = False
                    elif user_heal == p3.name or user_heal == '3':
                        recovered = heal(player)
                        p3.hp += recovered
                        action_statement(player, 'uzdrowil ' + p3.name + ' ' + str(recovered))
                        turn = False
                    elif user_heal == p4.name or user_heal == '4':
                        recovered = heal(player)
                        p4.hp += recovered
                        action_statement(player, 'uzdrowil ' + p4.name + ' '+str(recovered))
                        turn = False
                    else:
                        print("rozproszyl sie i nikogo nie uleczyl!!")
                        turn = False
                except:
                    print("nie masz sily!!!")

            else:
                print("sprobuj jeszcze raz")


def battle_system(p1, p2, p3, p4, mon):
    orginalhp = mon.hp
    alive = True
    print("\nspotykasz: " + mon.name + "!")
    while alive:
        print("+--------------------------------------------+")
        print("wrog: " + mon.name + "   |   HP: "+str(mon.hp))
        print("+--------------------------------------------+")
        player_status(p1)
        player_status(p2)
        player_status(p3)
        player_status(p4)

        player_moves(p1, mon, p2, p3, p4)
        player_moves(p2, mon, p1, p3, p4)
        mon_att(mon, p1, p2, p3, p4)
        player_moves(p3, mon, p1, p2, p4)
        player_moves(p4, mon, p1, p2, p3)
        if p1.hp <= 0 and p2.hp <= 0 and p3.hp <= 0 and p4.hp <= 0:
            print('przegrywasz')
            time.sleep(3)
            alive = False
            player_status(p1)
            player_status(p2)
            player_status(p3)
            player_status(p4)
            break

        if mon.hp <= 0:
            print('''
            *******************
            *   wygrales!!!   *
            *******************
            ''')
            time.sleep(1)
            alive = False
            mon.hp = orginalhp


def area(area, num_floors, boss):
    place = True
    while place:
        ran_num = random.randint(1,100)
        print("zostaly " + str(num_floors) + " poziomy", area + "...")
        if num_floors == 1:
            print('''
            *****************
            * finalny boss! *
            *****************
            ''')
            time.sleep(2)

            battle_system(bartek, maciek, hubert, the_player, boss)
            place = False
        else:
            direction = input('napisz u(up), d(down), l(left) lub r(right) aby sie ruszyc: ')
            if direction.lower() == 'up' or direction.lower() == 'u' or direction.lower() == 'Up' or direction.lower() == 'UP':
                print('>poruszyliscie sie w gore')
                time.sleep(1)
                if ran_num <= 33:
                    battle_system(bartek, maciek, hubert, the_player, ooze)
                    num_floors -= 1
                elif ran_num > 33 and ran_num < 66:
                    num_floors -= 1
                elif ran_num >= 66:
                    battle_system(bartek, maciek, hubert, the_player, skeleton)
                    num_floors -= 1
            elif direction.lower() == 'down' or direction.lower() == 'd' or direction.lower() == 'DOWN' or direction.lower() == 'Down':
                print(">poruszyliscie sie na dol")
                time.sleep(1)
                if ran_num <= 15:
                    battle_system(bartek, maciek, hubert, the_player, orc)
                    num_floors -= 1
                elif ran_num > 15 and ran_num <= 33:
                    battle_system(bartek, maciek, hubert, the_player, ghost)
                    num_floors -= 1
                elif ran_num > 33 and ran_num < 66:
                    num_floors -= 1
                elif ran_num >= 66:
                    battle_system(bartek, maciek, hubert, the_player, goblin)
                    num_floors -= 1
            elif direction.lower() == 'left' or direction.lower() =='l' or direction.lower() == 'Left' or direction.lower() == 'LEFT':
                print('>poruszyliscie sie w lewo')
                time.sleep(1)
                if ran_num <= 33:
                    battle_system(bartek, maciek, hubert, the_player, agent)
                    num_floors -= 1
                elif ran_num >33 and ran_num <66:
                    num_floors -= 1
                elif ran_num >= 66:
                    battle_system(bartek, maciek, hubert, the_player, snakes)
                    num_floors -= 1
            elif direction.lower() == 'right' or direction.lower() =='r' or direction.lower() == 'RIGHT':
                time.sleep(1)
                print('>poruszyliscie sie w prawo')
                if ran_num <= 33:
                    battle_system(bartek, maciek, hubert, the_player, bats)
                    num_floors -= 1
                elif ran_num > 33 and ran_num <66:
                    num_floors -= 1
                elif ran_num >= 66:
                    battle_system(bartek, maciek, hubert, the_player, mushroom)
                    num_floors -= 1
            elif direction.lower() == 'cheatcode':
                game_complete()
            else:
                print('gdzie?')
                time.sleep(2)


def welcome():
    print("****")
    print("witaj w magicznej podrozy!")
    print("bedziesz pomagal bartkowi mackowi i hubertowi w ich przygodzie")
    print("powodzenia!")
    print("*****")
    time.sleep(2)



def game_complete():
    print("*****")
    print("po pokonaniu mrocznego pana jako druzyna wracacie do wioski.\n")
    print("z pewnoscia bedziecie opowiadac te historie swoim dzieciom...")
    print("dzieki za gre!")
    print("*****")

    # win= Tk()
    # new= Toplevel(win)
    # new.geometry("200x200")
    # new.title("koniec!!!!")
    # img =PhotoImage(file="zdjecie.png")
    # label =Label(win, image=img)
    # label.pack()

 
    


# main flow of the game
welcome()
print("po jakims czasie trafiasz do dungeonu.")
time.sleep(2)
area('dungeon', 3, monster)
print('zyskujecie lunearny miecz i wychodzicie z dungeonu.\n przechodzicie do nawiedzonego lasu.')
time.sleep(1)
print("dojechaliscie do lasu.")
area('woods', 5, monster2)
print('po wygranej zabieracie relikt od goblina i wychodzicie')
time.sleep(1)
print('oto ona, wieza mrocznego pana.')
area('tower', 10, monster3)
game_complete()
