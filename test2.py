# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef97897"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)
print(translation)

# translate string
print("Translated string:", string.translate(translation))