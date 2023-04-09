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

def Break20():
    notification.notify(title='Break Time!',
                        message="Look 20 Meter Away for 20 Seconds!",
                        timeout=20,
                        app_icon='Media\\App Icon.ico')
    
triggerQuote = time.ctime(time.time() + 60*random.randint(15,50))
triggerBreak = time.ctime(time.time() + 60*20)
print("Now:  ",time.ctime(),'\n'+"Quote:",triggerQuote,'\n'+"Break:",triggerBreak)

while True:
    now = time.ctime()
    if now == triggerQuote:
        print("Triggered Quote")
        triggerQuote = time.ctime(time.time() + 60*20)
        print(triggerQuote)
        Quote()
    if now == triggerBreak:
        print("Triggered Break")
        triggerBreak = time.ctime(time.time() + 60*random.randint(15,50))
        print(triggerBreak)
        Break20()
