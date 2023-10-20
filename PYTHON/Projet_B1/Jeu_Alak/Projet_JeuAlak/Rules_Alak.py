class Alak:
    
    def __init__(self,n): 
        self.board = []  #Liste représentant le plateau du jeu 
        self.n = n  #Variable représentant la longueur n du plateau
        self.player = range(1,3) #Range ayant deux valeurs possibles 1 pour joueur 1 ou 2 pour joueur 2
        self.removed = []  #Liste représentant les pions capturés au tour précédent 
        self.empty_case = "." #Variable représentant une case vide
        self.p1_case = "x" #Variable représentant une case occupée par le joueur 1
        self.p2_case = "o" #Variable représentant une case occupée par le joueur 2

    def newBoard(self):
        """        
        Fonction représentant l'état initial du plateau de jeu, c'est-à-dire plateau vide 
        actuellement représenté par "."
        """
        self.board = []  #Réinitialisation du plateau du jeu
        for i in range(self.n):  #Initialisation de la taille du plateau en fonction de n
            self.board.append(self.empty_case) #Ajout des cases vides 
        return self.board  #Retour du tableau du jeu


    def display(self): #Fonction display qui permet l'affichage de la fonction du jeu
        """
        Fonction d'affichage du plateau du jeu dans la console.
        """
        for case in self.board: #Pour toutes cases présentes dans le plateau du jeu
            if self.player == 1: #Si c'est une case choisie/occupée par le joueur 1
                case = self.p1_case #On la remplace par p1_case = "x"
            elif self.player == 2: #Sinon si c'est une case choisie/occupée par le joueur 2
                case = self.p2_case #On la remplace par p2_case = "o"
            else: #Sinon
                case = self.empty_case #On la remplace par empty_case = "."
        print(self.board) #On affiche le plateau du jeu


    def captured(self):
        """
        Fonction qui permet d'établir la règle des pions à capturer,
        c.a.d si 
        """
        i = self.user_choice
        for case in self.board:
            if self.player == 1:
                if i-2 == self.p1_case and i-1 == self.p2_case:
                    self.removed.append(i-1) 
            if self.player == 2:
                if i-2 == self.p2_case and i-1 == self.p1_case:
                    self.removed.append(i-1)
                self.removed.remove(i-1)
        return "Liste des éléments supprimées" + str(self.removed) + "." +"\n Voici le nouveau plateau" + str(self.board)

    def possible(self,i):
        """
        Fonction permettant de déterminer si OUI ou NON il est possible pour le joueur de jouer
        sur une case i choisi.
        """
        for case in self.board: #Pour toutes les cases dans le tableau, si
            if case == self.empty_case:
                return True
        return False

    
    def select(self):
        """
        Fonction permettant au joueur d'indiquer la case sur laquelle il souhaite
        jouer. S'il est impossible d'y joueur alors on lui demande de choisir une autre case
        sinon la case séléctionner est valide.
        """
        self.user_choice = int(input("Choose a number to put your pawn: "))
        for case in self.board:
            while Alak.possible(self,self.user_choice) != True:
                self.user_choice = int(input("Sorry you can't choose this place, please choose a other number to put your pawn: "))
        return "Well, you choosed the number " + str(self.user_choice)


    def put(self):
        """
        Fonction qui permet de poser le pion sur la case séléctionné
        """
        Alak.select(self) 
        i = self.user_choice
        if self.player == 1:
            self.board[i] = "x"
            return self.board
        else:
            self.board[i] = "o"
            return self.board
        return "Impossibe de poser un pion"


    def again(self):
        for case in self.board:
            if case == self.empty_case :
                return True
        return False


    # def win(self):
    #     p1 = []
    #     p2 = [] 
    #     for case in self.board:
    #         if case == self.p1_case:
    #             p1 += 1
    #         else:
    #             p2 +=1
    #     if p1 > p2:
    #         return "Winner: Player 1 \n Looser: Player 2"
    #     else:
    #         return "Winner: Player 2 \n Looser: Player 1"