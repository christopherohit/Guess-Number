import sys
import Menu

def Intro():
    while True:
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~        //===   __  __   ____   ___   ___       || ====        ~")
        print("~        || ===  ||  ||   ||__   ||__  ||__      ||  ||         ~")
        print("~        ||  ||  ||  ||   ||        ||    ||     ||  ||         ~")
        print("~         \\\_||  \\\__//   ||__    __||  __||     ||  ||         ~")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")

        print("\n About this game:")
        print("After a stressful and tiring working time, you need to rest")
        print("because you are too tired but can't sleep because of")
        print("the stress in your body. So you need to find a form of entertainment")
        print("that helps you relieve stress, focus your mind and develop your predictive ability.")
        print("Well this is the game created to help you in that. Briefly about the game:")
        print("The game includes many different modes with increasing levels and the ability")
        print("to solve problems also decreases, but the rules of play are unchanged.")
        print("Specifically, you will have n turns corresponding to the difficulty you have chosen and")
        print("with your super brain you can deploy levels of algorithms to solve the given problem")
        print("within a given limit or use spiritual elements such as grandparents, guardian ancestors, prophesies of the universe,")
        print("space-time machine, holder of time, decider of numbers, saint of")
        print("loops, destroyer of Pythagoras, lord of only In general, you can use any method to guess the")
        print("number you need to find in a certain number of turns, you win or you lose, don't say much Ok")
        print("\n")
        Agreed = input("Do you Agreed with us (y/n)")
        if Agreed not in ("Y" , "N" , "y" , "n"):
            print("Invalid submit. Please check again !!!")
            continue
        elif Agreed == "Y" or Agreed == "y":
            Menu.Menu()
        elif Agreed == "N" or Agreed == "n":
            sys.exit()

def Continue():
    print ("Do you want continue game ? (y/n)")
    select = input()
    if select == "y" or select == "Y":
        return Menu.Menu()
    elif select == "n" or select == "N":
        return -1
    else:
        print ("Invalid answer")
        return Continue()