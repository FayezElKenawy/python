
import random


def randomPassword(pass_stat,letters):
    capital_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    small_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    symbols = ["@","#","$","%","^","&","*","_","-",")","(","+","="]
    password = ""
    if pass_stat == "strong":#return strong password
        i = 2 
        while i > 0:
            password = password + random.choice(capital_letters) + random.choice(small_letters)  + random.choice(numbers) + random.choice(symbols)
            i = i - 1
        return password + random.choice(capital_letters)
    elif pass_stat == "medium":#return medium password
        if letters == "L": #return letters only
            i = 3 
            while i > 0:
                password = password + random.choice(capital_letters) + random.choice(small_letters)
                i = i - 1
            return password + random.choice(capital_letters)
        else:#return numbers and symbols only
            i = 3 
            while i > 0:
                password = password + random.choice(numbers) + random.choice(symbols)
                i = i - 1
            return password + random.choice(symbols)
    else:#return weak passowrd
        i = 2 
        while i > 0:
            password = password + random.choice(capital_letters) + random.choice(small_letters)
            i = i - 1
        return password + random.choice(capital_letters)
        

print(randomPassword("strong"," "))   
print(randomPassword("medium","L"))
print(randomPassword("medium"," ")) 
print(randomPassword("weak",""))   
        
