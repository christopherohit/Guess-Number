import Intro
import os
import sys
import Game

def Menu():
    while True:
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~        //===   __  __   ____   ___   ___       || ====        ~")
        print("~        || ===  ||  ||   ||__   ||__  ||__      ||  ||         ~")
        print("~        ||  ||  ||  ||   ||        ||    ||     ||  ||         ~")
        print("~         \\\_||  \\\__//   ||__    __||  __||     ||  ||         ~")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("\n")
        print("\n[1] Guess It With Medium Mode")
        print("\n[2] Guess It With Hardly Mode")
        print("\n[3] Create a Number To Computer Play")
        print("\n[4] Auto Run")
        print("\n[5] Exit Program")

        Select = input("Please Choose a mode which you want to play: ")
        if (Select not in ('1' , '2' , '3' , '4' , '5')):
            print("Invalid Answers")
            continue
        if Select == "1":
            Game.create_Medium_Mode()
            Intro.Continue()
        if Select == "2":
            Game.Create_Hard_Mode()
            Intro.Continue()
        if Select == "3":
            minimum = int(input("Please enter the lowest number to guess: "))
            maximum = int(input("Please enter the highest number to guess: "))
            Game.Auto_Find_By_Binary_Search(minimum , maximum)
            Intro.Continue()
        if Select == "4":
            minimum = int(input("Please enter the lowest number to guess: "))
            maximum = int(input("Please enter the highest number to guess: "))
            Game.Auto_Find_Automatic(minimum , maximum)
            print("Do you wanna see a model binary search of it? (y/n)")
            ss = input()
            if ss == "N" or ss == "n":
                break
            elif ss == "Y" or ss == "y":
                Intro.Continue()
        if Select == "5":
            break
    print("\nGoodBye !!!!!!!")
    print("Press any button to exit. " , input())  
    sys.exit()


