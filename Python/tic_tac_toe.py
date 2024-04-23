
grid = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]

def printGrid(grid):
    print('')
    print( grid[0] + ' | ' + grid[1] + ' | ' + grid[2] )
    print('---------')
    print( grid[3] + ' | ' + grid[4] + ' | ' + grid[5] )
    print('---------')
    print( grid[6] + ' | ' + grid[7] + ' | ' + grid[8] )
    print('')


currentPlayer = 'X'
nul = 0
scoreX = 0
scoreO = 0

def playerInput(grid):
    inp = int(input("Entrez un nombre entre 1 et 9 : "))
    try : 
        if inp >= 1 and inp <=9 and grid[inp-1] == '-' :
            grid[inp-1] = currentPlayer
            changeplayer()
        elif inp == 0 or inp > 9 :
            print("Valeur d'entree incorrect, Entrez un chiffre entre 1 et 9")
        else :
            print('Position déjà jouée')
    except (ValueError) :
        print("Pas de lettre(s), Entrez un chiffre entre 1 et 9")
        playerInput(grid)

def checkWin(grid):
    global currentPlayer, runningGame, scoreO, scoreX, nul
    if grid[0] == grid[1] == grid[2] and grid[0] != '-' or grid[0] == grid[3] == grid[6] and grid[0] != '-' or grid[0] == grid[4] == grid[8] and grid[0] != '-' or grid[4] == grid[1] == grid[7] and grid[1] != '-' or grid[8] == grid[5] == grid[2] and grid[2] != '-' or grid[6] == grid[4] == grid[2] and grid[2] != '-' or grid[3] == grid[4] == grid[5] and grid[3] != '-' or grid[6] == grid[7] == grid[8] and grid[6] != '-':
        print("Victoire du joueur " + currentPlayer)
        if currentPlayer == 'X' :
            scoreX = scoreX + 1
            
        elif currentPlayer == 'O' :
            scoreO = scoreO + 1
            
        else : 
            nul = nul + 1
            
        printGrid(grid)
        print("Score X : " + str(scoreX))
        print("Score 0 : " + str(scoreO))
        print  ("Match nul : " + str(nul))
        resetGrid()
        


def changeplayer():
    global currentPlayer
    if currentPlayer == "X" :
        checkWin(grid)
        currentPlayer = "O"
    else :
        checkWin(grid)
        currentPlayer = "X"

def resetGrid():
    global grid
    grid = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]


runningGame = True
print("Le jeu va commencer appuyer sur \n A pour continuer : \n B pour annuler : ")

try : 
    playGame = str(input("Votre Choix : ").upper())
    while runningGame :
        if playGame == "A":
            runningGame = True
            printGrid(grid)
            playerInput(grid)
        elif playGame == "B" :
            print("A bientot")
            break
        else :
            break   
except (ValueError):
    print("Option non valide")



