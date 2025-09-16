from commons import Match
jeu_en_cours = True

while jeu_en_cours == True :
    match = Match()
    match.pokemon_display()
    match.pokemon_selection()
    match.game_content()
    t = input('rejouer ? (y/n) :')
    while t not in ['y', 'n'] :
        t = input('rejouer ? (y/n) :')
    else :
        jeu_en_cours == False
        pass