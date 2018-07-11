


"""def product_list(list_of_numbers):
    if len(list_of_numbers) >0:
        
        if len(list_of_numbers) == 1:
            return list_of_numbers[len(list_of_numbers) - 1]
        if len(list_of_numbers) == 2:
            if list_of_numbers[0] > list_of_numbers[1]:
                return list_of_numbers[0]
            return list_of_numbers[1]
        else:
            greatest_no = list_of_numbers[0]
            i = 0 
            while i <len(list_of_numbers):
                if list_of_numbers[i] > greatest_no:
                    greatest_no = list_of_numbers[i]
                i = i + 1
            return greatest_no

    return 0

print (product_list([9,2,3,17]))
def word_in_pos(word, parts_of_speech):
    
    for item in parts_of_speech:
        if item in word:
            return item 
   


test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]

print (word_in_pos(test_cases[0], parts_of_speech))
print (word_in_pos(test_cases[1], parts_of_speech))
print (word_in_pos(test_cases[2], parts_of_speech))
print (word_in_pos(test_cases[3], parts_of_speech))"""
parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is , PLACE, no NOUN, named PERSON, We have so many, PLURALNOUN. around here.

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return word
    return None
        
def play_game(ml_string, parts_of_speech):    
    replaced = []
    items = test_string.split()
    for item in items:
        word = word_in_pos(item,parts_of_speech) 
        if word != None:
            if "," in word:
                replaced.append("corgi,")
                continue
            if "." in word:
                replaced.append("corgi.")
                continue
           
            replaced.append("corgi")

        else:
            replaced.append(item)
    return " ".join(replaced)
    
print (play_game(test_string, parts_of_speech))   """  


import os 
import string
def rename():
    file_list = os.listdir(r"C:\Users\fayez\Desktop\sites\python\alphabet")
    path = os.getcwd()
    os.chdir(r"C:\Users\fayez\Desktop\sites\python\alphabet")
    transstring = str.maketrans('','',string.digits)
    print(file_list)
    for item in file_list:
       os.rename(item,item.translate(transstring)) 
    os.chdir(path)
rename()