from plyer import notification
import time

messages = ['We got you Covered! Just Never Slow Down',"How you doin'?","Keep your Head up!"]

def alert(msg):
    notification.notify(title="Desktop Notifier",
                    app_name = "Desktop",
                    app_icon='Media//App Icon.ico',
                    message=msg)

#For Testing Phase only!
for i in range(3):
    alert(messages[i])
    time.sleep(20)