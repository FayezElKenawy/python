import time
import webbrowser


def takebreak():
    t =time.ctime()
    print("this programe  start in : " +t )
    breaks = 3
    i = 0
    while i < breaks:
        time.sleep(10)
        webbrowser.open("https://www.youtube.com/watch?v=14xLVgXTceQ")
        print("this program will start again after 10 seconds")
        i = i+1
takebreak()