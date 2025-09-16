def selectionprint():
    display = '''
        ══════════════════════════════════════════════════════════════════════════════════════
        🎮 Sélectionne ton Pokémon (1-10)
        ══════════════════════════════════════════════════════════════════════════════════════

        [0] 🌿 Boustiflor              | [5] 🌿 Bulbizarre
            🔹 Type : 🌱 Plante        |     🔹 Type : 🌱 Plante
            ❤️ PV : 150                |     ❤️ PV : 160
            ⚔️ Attaque : 55            |     ⚔️ Attaque : 50

        [1] 🔥 Salamèche              | [6] 🌿 Ortide
            🔹 Type : 🔥 Feu           |     🔹 Type : 🌱 Plante
            ❤️ PV : 120                |     ❤️ PV : 170
            ⚔️ Attaque : 60            |     ⚔️ Attaque : 45

        [2] 💧 Magicarpe              | [7] 🔥 Ponyta
            🔹 Type : 💧 Eau           |     🔹 Type : 🔥 Feu
            ❤️ PV : 80                 |     ❤️ PV : 130
            ⚔️ Attaque : 15            |     ⚔️ Attaque : 65

        [3] 💧 Léviator               | [8] 💧 Carapuce
            🔹 Type : 💧 Eau           |     🔹 Type : 💧 Eau
            ❤️ PV : 220                |     ❤️ PV : 150
            ⚔️ Attaque : 85            |     ⚔️ Attaque : 40

        [4] 🔥 Caninos                | [9] 🌿 Herbizarre
            🔹 Type : 🔥 Feu           |     🔹 Type : 🌱 Plante
            ❤️ PV : 140                |     ❤️ PV : 180
            ⚔️ Attaque : 50            |     ⚔️ Attaque : 60

        ══════════════════════════════════════════════════════════════════════════════════════
        '''
    return print(display)

def gameprint(enemy_name, enemy_hp, enemy_max_hp, ally_name, ally_hp, ally_max_hp, log1, log2, log3, player_team_str, enemy_team_str):
    display = f"""
    ══════════════════════════════════════════════════════
    👾 Adversaire : {enemy_name}
    ❤️ PV : {enemy_hp}/{enemy_max_hp}
    Équipe adverse : {enemy_team_str}
    ══════════════════════════════════════════════════════

    📜 Journal de combat :
    {log1}
    {log2}
    {log3}
    ══════════════════════════════════════════════════════

    🧑 Ton Pokémon : {ally_name}
    ❤️ PV : {ally_hp}/{ally_max_hp}
    Ton équipe : {player_team_str}

    🎮 Actions disponibles :
    [1] ⚔️ Attaquer
    [2] 🧴 Potion
    [3] ⏭️ Passer le tour
    [4] 🔄 Changer Pokémon
    ══════════════════════════════════════════════════════
    """
    return print(display)

def winprint(Pokemonjoueurnom):
    display = f'''
    ══════════════════════════════════════════════════════════════
    🏆  FIN DE PARTIE 🏆
    ══════════════════════════════════════════════════════════════

    🎉 Le grand vainqueur est :
    {Pokemonjoueurnom} 🎉

    ✨ Bravo, ton équipe remporte la victoire ! ✨

    ══════════════════════════════════════════════════════════════
    '''
    return print(display)

def loseprint(Pokemonadversenom):
    display = f'''
            ══════════════════════════════════════════════════════════════
            💀  FIN DE PARTIE 💀
            ══════════════════════════════════════════════════════════════

            🥀 Le vainqueur est :
            {Pokemonadversenom}

            😢 Ton équipe a été vaincue... Retente ta chance !
            ══════════════════════════════════════════════════════════════
            '''
    return print(display)

type_effect = {
    'feu': {'plante': 2, 'eau': 0.5, 'feu': 1},
    'eau': {'feu': 2, 'plante': 0.5, 'eau': 1},
    'plante': {'eau': 2, 'feu': 0.5, 'plante': 1}
}

POTION_HEAL = 30

# Pokémon parameters centralized here
POKEMON_CONFIG = [
    {'nom': 'Boustiflor', 'pvm': 150, 'pa': 55, 'type': 'plante'},
    {'nom': 'Salamèche', 'pvm': 120, 'pa': 60, 'type': 'feu'},
    {'nom': 'Magicarpe', 'pvm': 80, 'pa': 15, 'type': 'eau'},
    {'nom': 'Léviator', 'pvm': 220, 'pa': 85, 'type': 'eau'},
    {'nom': 'Caninos', 'pvm': 140, 'pa': 50, 'type': 'feu'},
    {'nom': 'Bulbizarre', 'pvm': 160, 'pa': 50, 'type': 'plante'},
    {'nom': 'Ortide', 'pvm': 170, 'pa': 45, 'type': 'plante'},
    {'nom': 'Ponyta', 'pvm': 130, 'pa': 65, 'type': 'feu'},
    {'nom': 'Carapuce', 'pvm': 150, 'pa': 40, 'type': 'eau'},
    {'nom': 'Herbizarre', 'pvm': 180, 'pa': 60, 'type': 'plante'},
]