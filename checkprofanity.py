
import urllib
from urllib.parse import quote

def read_text():
    message = open(r"C:\Users\fayez\Desktop\sites\python\movie_quotes\movie_quotes.txt")
    read_message = message.read()
    print(read_message)
    message.close()
    check_text(read_message)


def check_text(text):
    text1 = quote(text)
    connectionr = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text1) 
    result = connectionr.read()  
    
    print (result)
    connectionr.close()
    
read_text()
