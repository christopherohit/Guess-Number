import os
import sys
import Game

def Menu():
    while True:
        print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n~        //===   __  __   ____   ___   ___       || ====        ~")
        print("\n~        || ===  ||  ||   ||__   ||__  ||__      ||  ||         ~")
        print("\n~        ||  ||  ||  ||   ||        ||    ||     ||  ||         ~")
        print("\n~         \\\_||  \\\__//   ||__    __||  __||     ||  ||         ~")
        print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
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
        if Select == "2":
            Game.Create_Hard_Mode()
        if Select == "3":
            Game.Auto_Find_By_Binary_Search()
        if Select == "4":
            Game.Auto_Find_Automatic()
        if Select == "5":
            break
    print("\nGoodBye !!!!!!!")
    io = input("Press any button to exit")
    sys.exit()


