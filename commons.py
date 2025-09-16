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

class Team:
    def __init__(self, pokemons):
        if len(pokemons) != 3:
            raise ValueError("A team must have exactly 3 Pokémon.")
        self.pokemons = pokemons
        self.active_index = 0

    @property
    def active(self):
        return self.pokemons[self.active_index]

    def switch(self, idx):
        if idx < 0 or idx >= len(self.pokemons):
            raise ValueError("Invalid Pokémon index.")
        if not self.pokemons[idx].is_alive():
            raise ValueError("Cannot switch to a fainted Pokémon.")
        self.active_index = idx

    def has_alive(self):
        return any(p.is_alive() for p in self.pokemons)

    def get_alive_indices(self):
        return [i for i, p in enumerate(self.pokemons) if p.is_alive()]

    def __str__(self):
        return " | ".join(f"[{i+1}] {p.nom} ({p.pv}/{p.pvm})" for i, p in enumerate(self.pokemons))

from config import POKEMON_CONFIG
liste = [Pokemon(**params) for params in POKEMON_CONFIG]

class Match:
    def __init__(self):
        self.pokelist = liste.copy()

    def pokemon_display(self):
        os.system('cls')
        selectionprint()

    def pokemon_selection(self):
        temp_list = self.pokelist.copy()
        indices = []
        while len(indices) < 3:
            try:
                inp = int(input(f'Choisis le numéro du Pokémon #{len(indices)+1} (0-9, unique): '))
                if inp in indices or inp < 0 or inp >= len(temp_list):
                    print("Numéro invalide ou déjà choisi.")
                    continue
                indices.append(inp)
            except ValueError:
                print("Entrée invalide.")
        team_pokemons = [temp_list[i] for i in indices]
        # Remove selected pokemons from temp_list by index (descending to avoid shifting)
        for i in sorted(indices, reverse=True):
            temp_list.pop(i)
        self.player_team = Team(team_pokemons)
        # Adversaire : sélectionne 3 pokémons restants
        adv_indices = rd.sample(range(len(temp_list)), 3)
        adv_pokemons = [temp_list[i] for i in adv_indices]
        self.enemy_team = Team(adv_pokemons)

    def game_content(self):
        playing = True
        self.log = ['','','']
        while playing:
            os.system('cls')
            l1 = self.log[-1]
            l2 = self.log[-2]
            l3 = self.log[-3]
            gameprint(
                enemy_name=self.enemy_team.active.nom,
                enemy_hp=self.enemy_team.active.pv,
                enemy_max_hp=self.enemy_team.active.pvm,
                ally_name=self.player_team.active.nom,
                ally_hp=self.player_team.active.pv,
                ally_max_hp=self.player_team.active.pvm,
                log1=l1,
                log2=l2,
                log3=l3,
                player_team_str=str(self.player_team),
                enemy_team_str=str(self.enemy_team)
            )
            t = 0
            while t not in (1,2,3,4):
                try:
                    t = int(input("👉 Que veux-tu faire ? "))
                except ValueError:
                    t = 0
            if t == 1:
                self.player_team.active.attaquer(self.enemy_team.active)
                self.log.append(f"{self.player_team.active.nom} a attaqué {self.enemy_team.active.nom}")
            elif t == 2:
                self.player_team.active.potion()
                self.log.append(f"{self.player_team.active.nom} s'est soigné")
            elif t == 3:
                self.player_team.active.passertour()
                self.log.append(f"{self.player_team.active.nom} a passé son tour")
            elif t == 4:
                alive_indices = self.player_team.get_alive_indices()
                print("Pokémon vivants:", [(i+1, self.player_team.pokemons[i].nom) for i in alive_indices])
                idx = -1
                while idx not in alive_indices:
                    try:
                        idx = int(input("Numéro du Pokémon à envoyer au combat (1-3): ")) - 1
                    except ValueError:
                        idx = -1
                self.player_team.switch(idx)
                self.log.append(f"Changement: {self.player_team.active.nom} entre en combat!")
            if not self.enemy_team.active.is_alive():
                if self.enemy_team.has_alive():
                    # Switch to next alive
                    for i in self.enemy_team.get_alive_indices():
                        if i != self.enemy_team.active_index:
                            self.enemy_team.switch(i)
                            self.log.append(f"L'adversaire envoie {self.enemy_team.active.nom}!")
                            break
                else:
                    playing = False
                    self.winner = "Victoire"
                    continue
            time.sleep(0.5)
            os.system('cls')
            # Adversaire joue
            if not self.enemy_team.active.is_alive():
                continue
            t = rd.randint(1,4)
            if t == 1:
                self.enemy_team.active.attaquer(self.player_team.active)
                self.log.append(f"{self.enemy_team.active.nom} a attaqué {self.player_team.active.nom}")
            elif t == 2:
                self.enemy_team.active.potion()
                self.log.append(f"{self.enemy_team.active.nom} s'est soigné")
            elif t == 3:
                self.enemy_team.active.passertour()
                self.log.append(f"{self.enemy_team.active.nom} a passé son tour")
            elif t == 4:
                alive_indices = self.enemy_team.get_alive_indices()
                # Adversaire change si possible
                possible = [i for i in alive_indices if i != self.enemy_team.active_index]
                if possible:
                    idx = rd.choice(possible)
                    self.enemy_team.switch(idx)
                    self.log.append(f"L'adversaire change pour {self.enemy_team.active.nom}!")
            if not self.player_team.active.is_alive():
                if self.player_team.has_alive():
                    for i in self.player_team.get_alive_indices():
                        if i != self.player_team.active_index:
                            self.player_team.switch(i)
                            self.log.append(f"Tu envoies {self.player_team.active.nom}!")
                            break
                else:
                    playing = False
                    self.winner = 'Défaite'
                    continue
            time.sleep(0.5)
        os.system('cls')
        if self.winner == "Victoire":
            winprint(self.player_team.active.nom)
        else:
            loseprint(self.enemy_team.active.nom)
