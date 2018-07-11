
class inv:
    
    def inversee():
        string = "this is a very nice challenge"
        string_list = string.split()
        invers_list = []
        for word in string_list:
            inverse_word = ""
            i = len(word) - 1
            while i >= 0:
                inverse_word = inverse_word + word[i]
                i = i - 1
            
            invers_list.append(inverse_word) 
        print (" ".join(invers_list)) 
 
    inversee()           
