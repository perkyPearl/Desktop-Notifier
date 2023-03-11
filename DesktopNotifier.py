from plyer import notification
import time
import random

used = []

def alert(msg):
    notification.notify(title="Desktop Notifier",
                    app_name = "Desktop",
                    app_icon='Media//App Icon.ico',
                    message=msg)

def RandomQuote():
    global used
    file = open('quotes.txt')
    quote = file.readlines()
    size = len(quote)

    if len(used) == size:
        used.clear()
    
    index = random.randint(0,size-1)
    while index in used:
        index = random.randint(0,size-1)

    used.append(index)
    return quote[index]

def Quote():
    notification.notify(title='Quote of the Minute',
                        message=RandomQuote(),
                        timeout=2,
                        app_icon='Media\\App Icon.ico')

