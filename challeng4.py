
def check_string():
    string1 = "The quick brown fox jumps over the lazy dog" 
    string2 = "you don’t know how far you can go till you go that far"
    string3 = "the first step is the hardest ever but you have to take it"
    hstring1 = "brown fox over lazy dog"
    hstring2 = "how far     can    go" 
    hstring3 = "the step first you take it"
    print("string1  " +  check_all_words(string1,hstring1) ) 
    print("string2  " + check_all_words(string2,hstring2)) 
    print("string3  " + check_all_words(string3,hstring3)) 
def check_all_words(string,hstring):
    last_string = []
    hstring_list = hstring.split()
    #remove any word not in hstring 
    for word in string.split():
        if word in hstring_list:
            last_string.append(word)
    item_index = []
    for item in last_string:
        if item not in item_index:
            item_index.append(item)
    #check the index of each word
    for word in item_index:
        if item_index.index(word) != hstring_list.index(word):
            return "No"
    return "yes"  
check_string()