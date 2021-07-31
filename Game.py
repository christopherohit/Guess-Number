import random as rd
import math
import sys
import time
from typing import Counter

class bstNode: # Draw a model Binary search
    def __init__(self , key):
        self.key = key
        self.right = None
        self.left = None
    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = bstNode(key)
            else:
                self.right.insert(key)
        else:
            if self.left < key:
                if self.left is None:
                    self.left = bstNode(key)
                else:
                    self.left.insert(key)

    def display(self):
        lines , *_ = self._display_aux()
        for line in lines:
            print(line)
    
    def _display_aux(self):
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1 
            middle = width // 2
            return [line], width , height , middle
    
        if self.right is None:
            lines , n , p , x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x -1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shift_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shift_lines , n + u , p + 2 , n + u // 2
        
        if self.left is None:
            lines , n , p , x = self.right._display_aux
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shift_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shift_lines, n + u, p + 2, u // 2
        
        left , n , p , x = self.left._display_aux()
        right , m , q , y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * '_'
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left , right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a,b in zipped_lines]
        return lines, n + m + u, max(p,q) + 2, n + u // 2

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
    if count > k:
        print("The number is %d" % x)
        print("Hope you are better lucky in next time !")
        print("See you")

def create_Medium_Mode():
    k = math.log(1000 - 1 + 1 , 2)
    x = rd.randint(1 , 1000)
    print("\n\tYou've only ", round(k), " chances to guess number x which random from 1 to 1000!\n")
    Anou(k , x)

def Create_Hard_Mode():
    x = rd.randint(0 , 5000)
    k = math.log(5000 - 0 + 1 , 2)
    print("\n\tYou've only ", round(k), " chances to guess number x which random from 0 to 5000!\n")
    Anou(k ,x)

args = ["N" , "N" , "Y"]
index = -1

def inputs():
    global index, args;
    index += 1 
    return args[index]

def Auto_Find_By_Binary_Search(minimum , maximum): # Computer auto generate this issues and you check result
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

def Auto_Find_Automatic(minimun , maximum): #This different with Component above that the seft will auto generate number and will be
    # guess this and don't have any action from human
    while True:
        Coun = math.log(maximum - minimun + 1 , 2)
        if minimun > maximum:
            return True
        mid = (maximum + minimun) // 2
        x = rd.randint(minimun, maximum)
        if mid == x :
            print("The number secret is " , x)
            print("Computer has use " , round(Coun) , "chance to guess number")
            time.sleep(1)
            print("Do you want to see Binary Search Level (y/n) ?")
            See = input()
            if See not in ("y" , "Y" , "N" ,"n"):
                print("Invalid Selection")
                continue
            elif See == 'Y' or See == 'y':
                b = bstNode(mid)
                for _ in range(mid):
                    b.insert(x)
                b.display()
            elif See == 'n' or See == "N":
                sys.exit()
            break
        elif x > mid:
            return Auto_Find_Automatic(mid + 1 , maximum)
        elif x < mid:
            return Auto_Find_Automatic(minimun , mid - 1)
            


