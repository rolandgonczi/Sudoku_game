"""
Sudoku game by Roland and Oliver. All rights reserved.
"""

import os
import platform
import random

with open("title.txt", "r") as f:
    cont = f.read()                                         # ASCII Title
    print(cont)

with open("sudoku-top95.txt", "r") as f:
    sudokus = f.readlines()                                 # sudoku txt import


def get_import_sudoku(x):
    with open("sudoku-top95.txt", "r") as f:
        text = f.read()
        temp = text.split("\n")
        temp.pop(len(temp)-1)
        if x == "r":
            return fill_matrix(temp[random.randint(0, len(temp) - 1)])
        elif x > 0 and x < len(temp):
            return fill_matrix(temp[x - 1])
        else:
            return fill_matrix(temp[1])


def fill_matrix(string):
    counter = 0
    MatrixList = [[0, 1, 8, 0, 0, 0, 0, 3, 0],
                 [9, 0, 0, 0, 0, 2, 0, 4, 5],
                 [7, 0, 0, 0, 0, 6, 0, 0, 0],
                 [0, 0, 0, 0, 0, 7, 1, 2, 0],
                 [0, 0, 0, 0, 5, 0, 0, 0, 0],                           # Nested lists , MATRIX
                 [0, 8, 4, 3, 0, 0, 0, 0, 0],
                 [0, 0, 0, 7, 0, 0, 0, 0, 6],
                 [8, 2, 0, 6, 0, 0, 0, 0, 9],
                 [0, 3, 0, 0, 0, 0, 5, 8, 0]]
    for y in range(0, 9):
        for x in range(0, 9):
            MatrixList[y][x] = int(string[counter])
            counter += 1
    return MatrixList


def print_sudoku2(board):  # A board a mátrix!!                             # Sudoku grid generator
    letters = tuple(("A", "B", "C", "D", "E", "F", "G", "H", "I"))
    print("            " + "  1 " + "  2 " + "  3 " + "  4 " + "  5 " + "  6 " + "  7 " + "  8 " + "  9 " + "  ")
    print("            " + "+" + "---+"*9)
    for i, row in enumerate(board):
        print(("          " + str(letters[i] + " " + "|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row])))
        if i % 3 == 2:
            print("            " + "+" + "---+"*9)
        else:
            print("            " + "+" + "   +"*9)


def newcord():
    x = input(" Enter a letter between A and I:   ").upper()
    ABC = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
    try:
        z = ABC[x]
    except KeyError:
        print("Wrong input ")
        x = input(" Enter a letter between A and I:  ")                             # coord input and new value , or clear
        z = ABC[x] 
    valid_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,)
    y = (int(input(" Enter a number between 1-9 , ( 0 for clear your mistake ):  "))) - 1
    if y not in valid_numbers:
        print("Enter a valid number between 1-9 ")
        print(MatrixList2[z][y])
    else:
        print(MatrixList2[z][y])    
    change = int(input(" Enter the new value:  "))
    if change not in valid_numbers:
        print("Enter a valid number between 1-9 ")
        change = int(input(" Enter the new value:  "))
    else:
        MatrixList2[z][y] = change
        update()


def update():
    if platform.system() == 'Linux':
        os.system('clear')                              # screen refresh after each input
        print(cont)
        print_sudoku2(MatrixList2)
        newcord()


def validation_check():

    validation_check = 0
    for i in range(0, 9):
        if len(list(filter(filter_number, MatrixList[i]))) == 9:
            validation_check += 1

    templist = []
    for i in range(0, 9):
        templist.clear()
        for i2 in range(0, 9):
            templist.append(MatrixList[i2][i])
        if len(list(filter(filter_number, templist))) == 9:
            validation_check += 1

    if validation_check == 18:
        return True
    else:
        return False


def filter_number(x):
    try:
        if 0 < x < 10:
            return True
        else:
            return False
    except: return False


def verification_check():
    verification_check = 0
    for i in range(0, 9):
        if len(set(MatrixList[i])) == len(MatrixList[i]):
            verification_check += 1

    templist = []
    for i in range(0, 9):
        templist.clear()
        for i2 in range(0, 9):
            templist.append(MatrixList[i2][i])
        if len(set(templist)) == len(templist):
            verification_check += 1

    for block in range(0, 7, 3):
        for block2 in range(0, 7, 3):
            templist.clear()
            for i in range(0, 3):
                for i2 in range(0, 3):
                    templist.append(MatrixList[i2 + block][i + block2])
            if len(set(templist)) == len(templist):
                verification_check += 1
    if verification_check == 27:
        return True
    else:
        return False


MatrixList = [\
    [0, 1, 8, 0, 0, 0, 0, 3, 0],
    [9, 0, 0, 0, 0, 2, 0, 4, 5],
    [7, 0, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 7, 1, 2, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 8, 4, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 6],
    [8, 2, 0, 6, 0, 0, 0, 0, 9],
    [0, 3, 0, 0, 0, 0, 5, 8, 0]]

MatrixList2 = MatrixList
MatrixList2 = get_import_sudoku("r")  # "r" for random sudoku


print_sudoku2(MatrixList2)


newcord()


print("\n"*6)


if validation_check() is True:
    print("Validation successful")
    if verification_check() is True:
        print("Solution accepted!")
