import random as rd
import os
import time
from config import selectionprint, gameprint, winprint, loseprint, type_effect


class Pokemon:
    def __init__(self, nom, pvm, pa, type):
        self.nom: str = nom
        self.pvm: int = pvm
        self.pv: int = pvm
        self.pa: int = pa
        self.type: str = type

    def degats(self, damage: int, type: str):
        multiplier = type_effect.get(type, {}).get(self.type, 1)
        damage *= multiplier
        self.pv -= damage
        if self.pv < 0:
            self.pv = 0
        
    def attaquer(self, cible):
        cible.degats(damage=self.pa, type=self.type)
        

    def passertour(self):
        pass

    def potion(self):
        if self.pv > self.pvm - 30:
            self.pv = self.pvm
        else :
            self.pv += 30

    def is_alive(self):
        return True if self.pv > 0 else False

p1 = Pokemon(nom='Boustiflor', pvm=150, pa=55, type='plante')
p2 = Pokemon(nom='Salamèche', pvm=120, pa=60, type='feu')
p3 = Pokemon(nom='Magicarpe', pvm=80, pa=15, type='eau')
p4 = Pokemon(nom='Léviator', pvm=220, pa=85, type='eau')
p5 = Pokemon(nom='Caninos', pvm=140, pa=50, type='feu')
p6 = Pokemon(nom='Bulbizarre', pvm=160, pa=50, type='plante')
p7 = Pokemon(nom='Ortide', pvm=170, pa=45, type='plante')
p8 = Pokemon(nom='Ponyta', pvm=130, pa=65, type='feu')
p9 = Pokemon(nom='Carapuce', pvm=150, pa=40, type='eau')
p10 = Pokemon(nom='Herbizarre', pvm=180, pa=60, type='plante')

liste= [p1,p2,p3,p4,p5,p6,p7,p8,p9]
class Match:
    def __init__(self):
        
        self.pokelist = liste
    
    def pokemon_display(self):
        os.system('cls')
        selectionprint()




    def pokemon_selection(self):
        inp = ''
        while inp not in (0,1,2,3,4,5,6,7,8,9):
            inp = int(input('choisis un numéro de pokemon parmis cette liste'))
        self.Pokemonjoueur = self.pokelist [inp]
        self.pokelist.pop(inp)
        self.Pokemonadverse = self.pokelist[rd.randint(0,7)]
        

    def game_content(self):
        playing = True
        self.log = ['','','']

        while playing == True :
            os.system('cls')  # Efface la console Windows
            l1 = self.log[-1]
            l2 = self.log[-2]
            l3 = self.log[-3]
            gameprint(
                enemy_name=self.Pokemonadverse.nom,
                enemy_hp=self.Pokemonadverse.pv,
                enemy_max_hp=self.Pokemonadverse.pvm,
                ally_name=self.Pokemonjoueur.nom,
                ally_hp=self.Pokemonjoueur.pv,
                ally_max_hp=self.Pokemonjoueur.pvm,
                log1=l1,
                log2=l2,
                log3=l3
            )

            t = 0
            while t not in (1,2,3):
                try:
                    t = int(input("👉 Que veux-tu faire ? "))
                except ValueError:
                    t = 0
            if t == 1:
                self.Pokemonjoueur.attaquer(self.Pokemonadverse)
                self.log.append('le pokemon allié à attaqué')
            elif t == 2:
                self.Pokemonjoueur.potion()
                self.log.append("le pokemon allié s'est soigné")
            else:
                self.Pokemonjoueur.passertour()
                self.log.append("le pokemon allié à passé son tour")
            if not self.Pokemonadverse.is_alive():
                playing = False
                self.winner = "Victoire"
                continue

            time.sleep(0.5)
            os.system('cls')  # Efface la console avant le tour adverse

            t = rd.randint(1,3)
            if t == 1:
                self.Pokemonadverse.attaquer(self.Pokemonjoueur)
                self.log.append('le pokemon adverse à attaqué')
            elif t == 2:
                self.Pokemonadverse.potion()
                self.log.append("le pokemon adverse s'est soigné")
            else:
                self.Pokemonadverse.passertour()
                self.log.append("le pokemon adverse à passé son tour")

            if not self.Pokemonjoueur.is_alive():
                playing = False
                self.winner = 'Défaite'
                continue
            time.sleep(0.5)
        os.system('cls')
        if self.winner == "Victoire":
            winprint(self.Pokemonjoueur.nom)            
        else:
            loseprint(self.Pokemonadverse.nom)
