def afficher_grille(grille):
    """Affiche la grille du morpion"""
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)


def verifier_victoire(grille, joueur):
    """Vérifie si un joueur a gagné"""

    # Vérifie les lignes
    for ligne in grille:
        if ligne.count(joueur) == 3:
            return True

    # Vérifie les colonnes
    for col in range(3):
        if grille[0][col] == joueur and grille[1][col] == joueur and grille[2][col] == joueur:
            return True

    # Vérifie les diagonales
    if grille[0][0] == joueur and grille[1][1] == joueur and grille[2][2] == joueur:
        return True
    if grille[0][2] == joueur and grille[1][1] == joueur and grille[2][0] == joueur:
        return True

    return False


def morpion():
    """Lance le jeu de morpion."""
    grille = [[" " for _ in range(3)] for _ in range(3)]
    joueur_actuel = "X"

    for _ in range(9):
        afficher_grille(grille)
        print(f"Tour du joueur {joueur_actuel}")

        # Demande la position
        while True:
            try:
                ligne = int(input("Entrez la ligne (0, 1 ou 2) : "))
                colonne = int(input("Entrez la colonne (0, 1 ou 2) : "))
                if grille[ligne][colonne] == " ":
                    grille[ligne][colonne] = joueur_actuel
                    break
                else:
                    print("Cette case est déjà occupée. Choisissez une autre case.")
            except (ValueError, IndexError):
                print("Entrée invalide. Entrez des nombres entre 0 et 2.")

        # Vérifie si le joueur actuel a gagné
        if verifier_victoire(grille, joueur_actuel):
            afficher_grille(grille)
            print(f"Le joueur {joueur_actuel} a gagné !")
            return

        # Change de joueur
        joueur_actuel = "O" if joueur_actuel == "X" else "X"

    afficher_grille(grille)
    print("Match nul !")


if __name__ == "__main__":
    morpion()
