#Yu Duan
#27/05/16
#Yogg Saron simulator
#0.1.2



def intro():
    global player_health
    global player_armor
    global enemy_health
    global enemy_armor
    global player_deck
    global enemy_deck
    global spell_amount
    global playerminion_list
    global enemyminion_list
    print("Welcome to the Yogg Saron simulator")
    player_health = -1
    player_armor = -1
    enemy_health = -1
    enemy_armor = -1
    player_deck = -1
    enemy_deck = -1
    spell_amount = -1
    while player_health < 1 or player_health > 30:
        player_health = int(input("Your hero's health: "))
        if player_health > 30 or player_health < 1:
            print("Hero's health cannot be less than 1 or more than 30")
    while player_armor < 0:
        player_armor = int(input("Your hero's armor: "))
        if player_armor < 0:
            print("Hero's armor cannot be less than 0")
    
    player_deck = int(input("Amount of cards in your deck, negative amount of cards are fatigue damage: "))
   
    while enemy_health < 1 or enemy_health > 30:
        enemy_health = int(input("Enemy hero's health: "))
        if enemy_health > 30 or enemy_health < 1:
            print("Hero's health cannot be less than 1 or more than 30")
    while enemy_armor < 0:
        enemy_armor = int(input("Enemy hero's armor: "))
        if enemy_armor < 0:
            print("Hero's armor cannot be less than 0")
    enemy_deck = int(input("Amount of cards in enemy deck, negative amount of cards are fatigue damage: "))
    while spell_amount < 0:
        spell_amount = int(input("The amount of spells: "))
        if spell_amount < 0:
            print("The amount of spells cannot be less than 0")
    
    playerminion_list = []
    answer = ""
    while answer != "end":
        print ("To add no more minions type end")
        print("Your minions")
        answer = input("Minion Health: ")
        minion_health = answer
        answer = input("Minion Attack: ")
        minion_attack = answer
        minion = (minion_health),(minion_attack)
        playerminion_list.append(minion)
        print(playerminion_list)
    enemyminion_list = []
    answer = ""
    while answer != "end":
        print ("To add no more minions type 0")
        print("Enemy minions")
        answer = input("Minion Health: ")
        minion_health = answer
        answer = input("Minion Attack: ")
        minion_attack = answer
        minion = (minion_health),(minion_attack)
        enemyminion_list.append(minion)
        print(enemyminion_list)

def simulator():
    if spell_amount != 0:
        import random
        spell_class = ["summon spells", "target spells", "untarget spells", "secret spells"]
        spellclass = random.choice(spell_class)
        if spellclass == "summon spells":
            import random
            summon_spells = ["Stand against Darkness","Call of the Wild","Ball of Spiders"]
            rnd_spell = random.choice(summon_spells)
            spellcast(rnd_spell)
        if spellclass == "target spells":
            import random
            target_spells = ["Soul Fire","Shadow Bolt","Bane of Doom"]
            rnd_spell = random.choice(target_spells)
            spellcast(rnd_spell)
    
   

def spellcast(spell):
    chosen_spell = spell
    print("hello")
    
     
def main():
    intro()
    simulator()
  
    
    
main()
