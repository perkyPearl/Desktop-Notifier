from plyer import notification
import time
import random
import requests
import json

class Settings:
    BreakTime = 20
    quoteTime = random.randint(15,50)
    WaterTime = 60
    quoteFile = "quotes.txt"
    AppIcon = "Media\\App Icon.ico"
    BreakIcon = "Media\\App Icon.ico"
    WaterBreakIcon = "Media\\App Icon.ico"
    QuoteIcon = "Media\\App Icon.ico"

class Features:
    Quotes = True
    Break = True
    Water_Reminder = True

# A API by lukePeavey
# https://github.com/lukePeavey/quotable
api = "https://api.quotable.io/random"

used = []

def alert(msg):
    notification.notify(title="Desktop Notifier",
                    app_name = "Desktop",
                    app_icon=Settings.AppIcon,
                    message=msg)

def fetchQuotes():
    n = len(open(Settings.quoteFile,"r").readlines())
    if n <= 100:
        print("Importing New Quotes......")
        file = open(Settings.quoteFile,"a")
        i = n
        while i<100:
            try:
                req = requests.get(api)
                if req.status_code == 200:
                    quote = req.json()['content']
                    print(quote)
                    file.write(f"{quote}\n")
                    i+=1
            except:
                pass
    file.close()

def RandomQuote():
    global used
    file = open(Settings.quoteFile,"r")
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
                        app_icon=Settings.QuoteIcon)

def Break():
    notification.notify(title='Break Time!',
                        message="Look 20 Meter Away for 20 Seconds!",
                        timeout=20,
                        app_icon=Settings.BreakIcon)

def WaterReminder():
    notification.notify(title='Break Time!',
                        message="Drink Water",
                        timeout=20,
                        app_icon=Settings.WaterBreakIcon)

def Test(title,msg,appIcon):
    notification.notify(title=title,
                        message=msg,
                        timeout=20,
                        app_icon=appIcon)

if __name__ == "__main__":
    print("Now:  ",time.ctime())
    if Features.Quotes:
        fetchQuotes()
        triggerQuote = time.ctime(time.time() + 60*Settings.quoteTime)
        print("Quote:",triggerQuote)
    if Features.Break:
        triggerBreak = time.ctime(time.time() + 60*Settings.BreakTime)
        print("Break:",triggerBreak)
    if Features.Water_Reminder:
        triggerWater = time.ctime(time.time() + 60*Settings.WaterTime)
        print("Water Break:",triggerWater)
    while True:
        now = time.ctime()

        if Features.Water_Reminder:
            if now == triggerWater:
                print("Triggered Water Reminder")
                triggerWater = time.ctime(time.time() + 60*Settings.waterTime)
                print(triggerWater)
                WaterReminder()
        if Features.Quotes:
            if now == triggerQuote:
                print("Triggered Quote")
                triggerQuote = time.ctime(time.time() + 60*Settings.quoteTime)
                print(triggerQuote)
                Quote()
        if Features.Break:
            if now == triggerBreak:
                print("Triggered Break")
                triggerBreak = time.ctime(time.time() + 60*Settings.BreakTime)
                print(triggerBreak)
                Break()