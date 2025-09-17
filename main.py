from classes import Match

def main():

    while True:
        # Création et déroulement d'un nouveau match
        match = Match()
        match.pokemon_display()       # Affiche l'écran de sélection
        match.pokemon_selection()     # Sélection des équipes
        match.game_content()         # Déroulement du combat
        
        while True:
            replay = input('Voulez-vous rejouer ? (y/n) : ').lower()
            if replay in ['y', 'n']:
                break
            print("Veuillez répondre par 'y' (oui) ou 'n' (non)")
        
        # Sort de la boucle si le joueur ne veut pas rejouer
        if replay == 'n':
            break

if __name__ == "__main__":
    main()