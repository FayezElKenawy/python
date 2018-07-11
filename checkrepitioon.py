

def rep():
    hstring3 = "the step first you take it"
    string3 = "the first it step is the hardest ever you but you have to take it"
    last_string = []
    hstring_list = hstring3.split(" ")
    item_index = []
    #remove any word not in hstring 
    for word in string3.split(" "):
        if word in hstring_list:
            last_string.append(word)
    i = 0
    while i < len(last_string):
        j = 0
        if len(item_index) != 0:
            #item = last_string[item_index[0]]
            #last_string.remove()
            print(last_string)
            del last_string[item_index[0]]
            item_index.remove(item_index[0])
            print(last_string)
            

        while j < len(last_string):
            if i != j and i < len(hstring_list) and j < len(hstring_list):
                if last_string[i] == last_string[j]:
                    if last_string[i] == hstring_list[i]:
                        word = last_string[i]
                        if word not in item_index:
                            item_index.append(j)
                            i = -1
                            break
                    elif last_string[j] == hstring_list[j]:
                        break
                    else:
                        break
      
            j = j +1
        i = i + 1
    print(last_string)
rep()

