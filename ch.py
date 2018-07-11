original_string = 'the first step is the hardest it ever but you have to take it'
encrypted_string = 'the first step you take it'

def check_encryption(original, encrypted):
    orginal_words = original.split(" ")
    encrypted_words = encrypted.split(" ")

    for i in encrypted_words:
        if i in orginal_words:
            index = orginal_words.index(i)
        else:
            return "No"

    index = orginal_words.index(encrypted_words[0])
    for e in encrypted_words:
        if e in orginal_words:
            if orginal_words.index(e) < index:
                return "No"
                break
            else:
                index = orginal_words.index(e)
        else:
            return "No"
    return "Yes"

print (check_encryption(original_string, encrypted_string))