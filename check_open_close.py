

def check(string1):
    if string1.find(" ") == -1:
        string = check_l(string1)
    else:
        string = string1.split()
        string = check_l(''.join(string))
        
    if len(string) % 2 != 0:
        return "Failed"
    else:
        length = len(string)
        i = 1
        index = 0
        for item in string:
            while i < length:
                if item =='{' or item =='(' or item =='[':
                    if item + string[i] == "()" or item + string[i] == "{}" or item + string[i] == "[]":
                        index = index + 1
                        i = i +1
                        break
                    elif item + string[length-i] == "()" or item + string[length-i] == "{}" or item + string[length-i] == "[]":
                        index = index + 1 
                        i = i +1
                        break
                    else:
                        return "failed"
                else:
                    i = i +1
                    break
        return "succ"
def check_l(string):
    newstring = ""
    le = "{}()[]"
    for item in string:
        if item in le:
            newstring = newstring + item
    return newstring
print(check("{ { {fsasdf (asdf ) } } }"))
print(check("{(){}}"))
print(check("{ { ( ( ) ) } }"))
print(check("{ { { ( ) }"))
print(check("{ { { ( } ) } }"))
