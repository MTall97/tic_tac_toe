import pygame
from pygame.locals import *

pygame.init()

pygame.display.set_caption("Tic Tac Toe")

screen = pygame.display.set_mode((600, 700))

"""
def drawGrid():
    backgroundColorRGB = (250, 235, 215)
    gridColorRGB = (165, 42, 42)
    screen.fill(backgroundColorRGB)
    for n in range(1, 3):
        pygame.draw.line(screen, gridColorRGB, (0, n * 200), (600, n * 200), 2)
        pygame.draw.line(screen, gridColorRGB, (n * 200, 0), (n * 200, 600), 2)
"""
def drawGrid():
    backgroundColorRGB = (250, 235, 215)
    gridColorRGB = (165, 42, 42)
    screen.fill(backgroundColorRGB)
    
    # Dessiner les lignes du quadrillage
    for n in range(1, 3):
        pygame.draw.line(screen, gridColorRGB, (0, n * 200), (600, n * 200), 2)
        pygame.draw.line(screen, gridColorRGB, (n * 200, 0), (n * 200, 600), 2)
    
    # Dessiner les bordures
    pygame.draw.rect(screen, gridColorRGB, (0, 0, 600, 600), 2)
    
    # Ajouter le texte "Score joueur X"
    font = pygame.font.Font(None, 23)
    text = font.render("Score joueur X: " + str(scoreX), True, (0, 0, 0))
    screen.blit(text, (30, 650))
    
    # Ajouter le texte "Score joueur O"
    text = font.render("Score joueur O: " + str(scoreO), True, (0, 0, 0))
    screen.blit(text, (230, 650))
    
    # Ajouter le texte "Match nul"
    text = font.render("Match nul: " + str(nul), True, (0, 0, 0))
    screen.blit(text, (450, 650))



def drawX(position):
    x, y = position
    pygame.draw.line(screen, (0, 255, 0), (x - 50, y - 50), (x + 50, y + 50), 5)
    pygame.draw.line(screen, (0, 255, 0), (x + 50, y - 50), (x - 50, y + 50), 5)
    

def drawO(position):
    pygame.draw.circle(screen, (255, 0, 0), position, 50, 5)

"""grid

playerInput(grid)"""

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
    if inp >= 1 and inp <=9 and grid[inp-1] == '-' :
        grid[inp-1] = currentPlayer
        changeplayer()
    else :
        print('Position déjà jouée')

def checkWin(grid):
    global currentPlayer, runningGame, scoreO, scoreX, nul, xo_positions
    if grid[0] == grid[1] == grid[2] and grid[0] != '-' or grid[0] == grid[3] == grid[6] and grid[0] != '-' or grid[0] == grid[4] == grid[8] and grid[0] != '-' or grid[4] == grid[1] == grid[7] and grid[1] != '-' or grid[8] == grid[5] == grid[2] and grid[2] != '-' or grid[6] == grid[4] == grid[2] and grid[2] != '-' or grid[3] == grid[4] == grid[5] and grid[3] != '-' or grid[6] == grid[7] == grid[8] and grid[6] != '-':
        print("Victoire du joueur " + currentPlayer)

        if currentPlayer == 'X' :
            scoreX = scoreX + 1
            
        elif currentPlayer == 'O' :
            scoreO = scoreO + 1
            
        printGrid(grid)
        print("Score X : " + str(scoreX))
        print("Score 0 : " + str(scoreO))
        print  ("Match nul : " + str(nul))
        resetGrid()
        xo_positions = []

    """
    else : 
        grid2 = set(grid)
        print(grid2)
        for element in grid2 :
            if element != '-' :
                nul = nul + 1 
                """

    # Si aucun joueur n'a gagné et toutes les cellules sont remplies, c'est un match nul
    if '-' not in grid:
        nul += 1
        printGrid(grid)
        print("Score X : " + str(scoreX))
        print("Score 0 : " + str(scoreO))
        print("Match nul : " + str(nul))
        resetGrid()
        xo_positions = []
        

def changeplayer():
    global currentPlayer
    if currentPlayer == "X" :
        if event.button == 1:  # Clic gauche de la souris
                xo_positions.append((cell_center, 'X'))
        checkWin(grid)
        currentPlayer = "O"
    else :
        if event.button == 1:  # Clic gauche de la souris
                xo_positions.append((cell_center, 'O'))
        checkWin(grid)
        currentPlayer = "X"


def resetGrid():
    global grid
    grid = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]




def getPositionInGrid(position):
    if position == (100, 100) :
        gridPosition = 1
        playerInput(grid, gridPosition)
    if position == (300, 100) :
        gridPosition = 2
        playerInput(grid, gridPosition)
    if position == (500, 100) :
        gridPosition = 3
        playerInput(grid, gridPosition)
    if position == (100, 300) :
        gridPosition = 4
        playerInput(grid, gridPosition)
    if position == (300, 300) :
        gridPosition = 5
        playerInput(grid, gridPosition)
    if position == (500, 300) :
        gridPosition = 6
        playerInput(grid, gridPosition)
    if position == (100, 500) :
        gridPosition = 7
        playerInput(grid, gridPosition)
    if position == (300, 500) :
        gridPosition = 8
        playerInput(grid, gridPosition)
    if position == (500, 500) :
        gridPosition = 9
        playerInput(grid, gridPosition)





runningScreen = True

xo_positions = []


while runningScreen:
    drawGrid()

    for event in pygame.event.get():
        if event.type == QUIT:
            runningScreen = False
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            cell_x = mouse_x // 200
            cell_y = mouse_y // 200
            cell_center = (cell_x * 200 + 100, cell_y * 200 + 100)
            
            getPositionInGrid(cell_center)
            checkWin(grid)

    # Dessiner les X et O à chaque itération de la boucle
    for position, xo in xo_positions:
        if xo == 'X':
            drawX(position)
        elif xo == 'O':
            drawO(position)

    pygame.display.update()
