#Yu Duan
#11/05/16
#Yogg Saron simulator
#0.1.1



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
    player_health = input("Your hero's health: ")
    player_armor = input("The enemy hero's health: ")
    enemy_health = input("Your hero's armor: ")
    enemy_armor = input("The enemy hero's armor: ")
    player_deck = input("Amount of cards in your deck: ")
    enemy_deck = input ("Amount of cards in enemy deck: ")
    spell_amount = input("The amount of spells: ")
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
            print(rnd_spell)
            spellcast(rnd_spell)
        if spellclass == "target spells":
            import random
            target_spells = ["Soul Fire","Shadow Bolt","Bane of Doom"]
            rnd_spell = random.choice(target_spells)
            print(rnd_spell)
            spellcast(rnd_spell)
    
   

def spellcast(spell):
    chosen_spell = spell
    print(chosen_spell)
    
     
def main():
    intro()
    simulator()
   
    
    
main()
