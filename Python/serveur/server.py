import socket, random, sys


# le jeu

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

def playerInput(grid, inp):
    inp = int(inp)
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
        sendWin()
        


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


def computer(grid) :
    global currentPlayer
    while currentPlayer == 'O' :
        inp = random.randint(0,8)
        if grid[inp] == '-':
            grid[inp] = currentPlayer
            changeplayer()
            checkWin(grid)


def sendGrid(grid):
    send_message(f'\n {grid[0]} | {grid[1]} | {grid[2]} \n --------- \n {grid[3]} | {grid[4]} | {grid[5]} \n --------- \n {grid[6]} | {grid[7]} | {grid[8]} \n')

def sendWin():
    global currentPlayer, runningGame, scoreO, scoreX, nul
    if grid[0] == grid[1] == grid[2] and grid[0] != '-' or grid[0] == grid[3] == grid[6] and grid[0] != '-' or grid[0] == grid[4] == grid[8] and grid[0] != '-' or grid[4] == grid[1] == grid[7] and grid[1] != '-' or grid[8] == grid[5] == grid[2] and grid[2] != '-' or grid[6] == grid[4] == grid[2] and grid[2] != '-' or grid[3] == grid[4] == grid[5] and grid[3] != '-' or grid[6] == grid[7] == grid[8] and grid[6] != '-':
        print("Victoire du joueur " + currentPlayer)
        if currentPlayer == 'X' :
            scoreX = scoreX + 1
            
        elif currentPlayer == 'O' :
            scoreO = scoreO + 1
            
        else : 
            nul = nul + 1
    return send_message(f'\n Score X : {scoreX} \n Score O : {scoreO} \n Score nul : {nul} \n')


######################################################################################################


# le serveur

FORMAT = 'UTF-8' # format du texte
TAILLE = 1024 
PORT = 5050  # Port de connexion

IPSERVER =   'localhost'  #socket.gethostbyname(socket.gethostname()) # Adresse IP du server

ADRESSE = (IPSERVER, PORT)  # Tuple contenant Adresse IP server et Port de connexion

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #création du socket

msg_disconnected = "!Connected"

try:

    serversocket.bind(ADRESSE) #liaison du socket à une adresse précise 

except socket.error: #gestion d'erreur

  print("La liaison du socket à l'adresse choisie a échoué.")
  
  sys.exit



def send_message(message):
    messageServeur = conn.sendall(message.encode(FORMAT))
    return messageServeur

def receiveMessage():
    messageClient = conn.recv(TAILLE).decode(FORMAT)
    return messageClient


runningGame = True


print("Demarrage du serveur...")

while runningGame :
    
    try :
        print("Serveur demarré")

        try :
            serversocket.listen()
            conn, adrr = serversocket.accept()
            print("serveur en ecoute, un connecté")

            message = "Le jeu va commencer appuyer sur \n A pour continuer : \n B pour annuler : " 
            send_message(message)

            playGame = receiveMessage()

            if playGame == "A" :

                #afficher grid pour client
                sendGrid(grid)
                while True :
                    #Demander de choisir position
                    message = "Entrez un nombre 1 et 9"
                    send_message(message)

                    #position client sur grid
                    position = int(receiveMessage())
                    playerInput(grid, position)
                    
                    #position jouee par ordi
                    computer(grid)
                    printGrid(grid)
                    sendGrid(grid)

                
            elif playGame == "B" :
                print("A Bientot")

            else : 
                ("Mauvaise saisie")
            
        except :
            print("Impossible d'etablir la liaison")

    except :
        print("Echec")

        

conn.close()
serversocket.close()