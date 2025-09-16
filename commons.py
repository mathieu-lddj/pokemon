import random as rd

def gameprint(enemy_name, enemy_hp, enemy_max_hp, ally_name, ally_hp, ally_max_hp, log1, log2, log3):
    display = f"""
    ══════════════════════════════════════════════════════
    👾 Adversaire : {enemy_name}
    ❤️ PV : {enemy_hp}/{enemy_max_hp}
    ══════════════════════════════════════════════════════

    📜 Journal de combat :
    {log1}
    {log2}
    {log3}
    ══════════════════════════════════════════════════════

    🧑 Ton Pokémon : {ally_name}
    ❤️ PV : {ally_hp}/{ally_max_hp}

    🎮 Actions disponibles :
    [1] ⚔️ Attaquer
    [2] 🧴 Potion
    [3] ⏭️ Passer le tour
    ══════════════════════════════════════════════════════
    
    """
    return print(display)


class Pokemon:
    def __init__(self, nom, pvm, pa, type):
        self.nom: str = nom
        self.pvm: int = pvm
        self.pv: int = pvm
        self.pa: int = pa
        self.type: str = type

    def degats(self, damage: int):
        self.pv -= damage
        if self.pv < 0:
            self.pv=0
        
    def attaquer(self, cible):
        cible.degats(self.pa)
        

    def passertour(self):
        pass

    def potion(self):
        if self.pv > self.pvm - 30:
            self.pv = self.pvm
        else :
            self.pv += 30

    def is_alive(self):
        return True if self.pv > 0 else False

p1 = Pokemon(nom='Boustiflor', pvm=180, pa=40, type='plante')
p2 = Pokemon(nom='Salamèche', pvm=180, pa=40, type='feu')
p3 = Pokemon(nom='magicarpe', pvm=180, pa=40, type='eau')
p4 = Pokemon(nom='Léviator', pvm=180, pa=40, type='eau')
p5 = Pokemon(nom='caninos', pvm=180, pa=40, type='feu')
p6 = Pokemon(nom='Bulbizarre', pvm=180, pa=40, type='plante')
p7 = Pokemon(nom='magicarpe', pvm=180, pa=40, type='eau')
p8 = Pokemon(nom='Léviator', pvm=180, pa=40, type='eau')
p9 = Pokemon(nom='caninos', pvm=180, pa=40, type='feu')
p10 = Pokemon(nom='Bulbizarre', pvm=180, pa=40, type='plante')

liste= [p1,p2,p3,p4,p5,p6,p7,p8,p9]
class Match:
    def __init__(self):
        
        self.pokelist = liste
    
    def pokemmon_display(self):
        for i in range(len(self.pokelist)):
            print(f"numéro:{i}\nnom: {self.pokelist[i].nom}\npv max: {self.pokelist[i].pvm}\npuissance d'attaque: {self.pokelist[i].pa}\ntype: {self.pokelist[i].type}\n\n")


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





            t =  int(input("👉 Que veux-tu faire ?")) or 0
            while t not in (1,2,3):
                
                print("👉 Que veux-tu faire ?", end='\r')
                t= int(input())
            if t ==1 :
                self.Pokemonjoueur.attaquer(self.Pokemonadverse)
                self.log.append('le pokemon allié à attaqué')
            elif t== 2:
                self.Pokemonjoueur.potion()
                self.log.append("le pokemon allié s'est soigné")
            else :
                self.Pokemonjoueur.passertour()
                self.log.append("le pokemon allié à passé son tour")
            if not self.Pokemonadverse.is_alive():
                playing = False
                self.winner = "Vitcoire"
                pass

            t = rd.randint(1,3)

            if t ==1 :
                self.Pokemonadverse.attaquer(self.Pokemonjoueur)
                self.log.append('le pokemon adverse à attaqué')
            elif t== 2:
                self.Pokemonadverse.potion()
                self.log.append("le pokemon adverse s'est soigné")
            else :
                self.Pokemonadverse.passertour()
                self.log.append("le pokemon adverse à passé son tour")

            if not self.Pokemonjoueur.is_alive():
                playing = False
                self.winner = 'Défaite'
                pass       
        print('fin de partie') 