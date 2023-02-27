table1 = ["_", "_", "_",
          "_", "_", "_",
          "_", "_", "_"]


def printtable():
    for i in range(1, 10):
        if i % 3 == 0:
            print(table1[i - 1], " ")
        else:
            print(table1[i-1], " ", end="")


moveposibilites = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def askformove(movecounter1):
    move = input("Give me move for you")
    if move != "":
        move = int(move)
    if move in moveposibilites:

        if (table1[move-1] != "X" and table1[move-1] != "O"):
            if movecounter1 % 2 == 0:
                table1[move - 1] = "X"
            else:
                table1[move - 1] = "O"
        else:
            print("This field is busy. Give another one")
            askformove(movecounter1)
    else:
        askformove(movecounter1)


def checkifwin(table, movecounter2):
    winningcombos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
        0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in winningcombos:
        if table[combo[0]] == table[combo[1]] and table[combo[0]] == table[combo[2]] and table[combo[0]] != "_":
            if movecounter2 % 2 == 0:
                winner = "X"
            else:
                winner = "O"
            printtable()
            print("The winner is :", winner)
            return True
    return False


def game():
    movecounter = 1
    for i in range(1, 10):
        printtable()
        askformove(movecounter)
        if checkifwin(table1, movecounter) == True:
            break
        movecounter += 1


game()
nextgame = int(input("If you want to play again input '1'"))
while (nextgame == 1):
    table1 = ["_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]
    game()
    nextgame = int(input("If you want to play again input '1'"))
