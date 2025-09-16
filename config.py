def selectionprint():
    display = '''
        ══════════════════════════════════════════════════════════════════════════════════════
        🎮 Sélectionne ton Pokémon (1-10)
        ══════════════════════════════════════════════════════════════════════════════════════

        [1] 🌿 Boustiflor              | [6] 🌿 Bulbizarre
            🔹 Type : 🌱 Plante        |     🔹 Type : 🌱 Plante
            ❤️ PV : 150                |     ❤️ PV : 160
            ⚔️ Attaque : 55            |     ⚔️ Attaque : 50

        [2] 🔥 Salamèche              | [7] 🌿 Ortide
            🔹 Type : 🔥 Feu           |     🔹 Type : 🌱 Plante
            ❤️ PV : 120                |     ❤️ PV : 170
            ⚔️ Attaque : 60            |     ⚔️ Attaque : 45

        [3] 💧 Magicarpe              | [8] 🔥 Ponyta
            🔹 Type : 💧 Eau           |     🔹 Type : 🔥 Feu
            ❤️ PV : 80                 |     ❤️ PV : 130
            ⚔️ Attaque : 15            |     ⚔️ Attaque : 65

        [4] 💧 Léviator               | [9] 💧 Carapuce
            🔹 Type : 💧 Eau           |     🔹 Type : 💧 Eau
            ❤️ PV : 220                |     ❤️ PV : 150
            ⚔️ Attaque : 85            |     ⚔️ Attaque : 40

        [5] 🔥 Caninos                | [10] 🌿 Herbizarre
            🔹 Type : 🔥 Feu           |     🔹 Type : 🌱 Plante
            ❤️ PV : 140                |     ❤️ PV : 180
            ⚔️ Attaque : 50            |     ⚔️ Attaque : 60

        ══════════════════════════════════════════════════════════════════════════════════════
        '''
    return print(display)

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