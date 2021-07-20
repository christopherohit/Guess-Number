import random as rd
import math

def Anou( k , x):
    count = 0
    
    while count < k:
        count += 1

        guess = int(input("Please fill in your guess number: "))

        if x == guess:
            print("Congratulation you're got it in " , count , " chances")
            break
        
        elif x > guess:
            print("Your guess number too small!")
        elif x < guess:
            print("Your guess number too large!")
    if count >= k:
        print("The number is %d" % x)
        print("Hope you are better lucky in next time !")
        print("See you")

def create_Medium_Mode():
    k = math.log(1000 - 1 + 1 , 2)
    x = rd.randint(1 , 1000)
    print("\n\tYou've only ", round(k), " chances to guess number x!\n")
    Anou(k , x)

def Create_Hard_Mode():
    x = rd.randint(0 , 5000)
    k = math.log(5000 - 0 + 1 , 2)
    print("\n\tYou've only ", round(k), " chances to guess number x!\n")
    Anou(k ,x)

args = ["N" , "N" , "Y"]
index = -1

def input():
    global index, args;
    index += 1 
    return args[index]

def Auto_Find_By_Binary_Search(): # Computer auto generate this issues and you check result
    minimum = int(input("Please enter the lowest number to guess: "))
    maximum = int(input("Please enter the highest number to guess: "))
    if minimum > maximum:
        return True
    mid = (maximum + minimum) // 2
    
    print("Is the number is " , mid , " ?" , end= " ")
    user = input()
    print(user)
    
    if user == "Y" or user == "y":
        print("Ya!!! Computer Has to guess it")
        return False
    elif user == "N" or user == "n":
        print("Your number which you has created in your mind greater than " , mid , "?" , end= " ")
        user = input()
        print(user)
        if user == "Y" or user == "y":
            return Auto_Find_By_Binary_Search(mid + 1 , maximum)
        elif user == "N" or user == "n":
            return Auto_Find_By_Binary_Search(minimum , mid - 1)
        else:
            print("Invalid input. You just select 'Y'/'N'")
            return Auto_Find_By_Binary_Search(minimum , maximum)
    else:
        print("Invalid Input. Print 'Y'/'N'")
        return Auto_Find_By_Binary_Search(minimum , maximum)

def Auto_Find_Automatic(): #This different with Component above that the seft will auto generate number and will be
    # guess this and don't have any action from human 
     
    
    
