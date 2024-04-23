import socket

FORMAT = 'UTF-8'
TAILLE = 1024
PORT = 5050

IPSERVER = 'localhost'  #socket.gethostbyname(socket.gethostname())
ADRESSE = (IPSERVER, PORT)


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



def send_message(message):
    messageClient = clientsocket.sendall(message.encode(FORMAT))
    return messageClient

def receiveMessage():
    messageServeur = clientsocket.recv(TAILLE).decode(FORMAT)
    return messageServeur



if __name__ =="__main__":

    try :
        clientsocket.connect(ADRESSE)
        print("Client Connecté")

        #debut de jeu
        messageServeur = receiveMessage()
        print(messageServeur)

        #choix jouer ou non
        jouer = str(input("Votre choix : ")).upper()
        send_message(jouer)
        
        #afficher grid
        messageServeur = receiveMessage()
        print(messageServeur)
        
        while True :
            #proposition de valeur entre 1 et 9
            messageServeur = receiveMessage()
            print(messageServeur)

            #choix valeur
            position = input("Votre choix : ")
            send_message(position)

            #recuperation grid
            messageServeur = receiveMessage()
            print(messageServeur)

            #recuperation Score
            print(messageServeur)


    except :
        print("Echec de la connexion")


    finally :
        clientsocket.close()