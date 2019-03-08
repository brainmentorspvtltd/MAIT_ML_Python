from datetime import datetime
import os, random

name = input("Enter your name : ")
print("Hello ",name)

helloIntent = ['hello','hi','hey','hey there','hi there']
timeIntent = ["time please","tell me time","time"]
dateIntent = ["date please","tell me date","date"]

chat = True
while chat:
# membership operator - in, not in
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello User")
    elif msg in timeIntent:
        t = datetime.now().time()
        print(t.strftime('%H:%M:%S %p'))
    elif msg == "play song":
        os.chdir(r'C:\Users\asus\Videos\Movavi Video Editor\Media Content\Audio')
        songs = os.listdir()
        s = random.choice(songs)
        os.startfile(s)
    elif msg == "bye":
        print("Bye",name)
        chat = False
    else:
        print("I don't understand")
