from WakeyCore import youtubePlayList, playerVLC
from tkinter import *

# GlobalVars
filePath = "c:\\logs\\"  # Windows Path

# MainWindow
root = Tk()
root.title("Youtube Player")

# Playlist Entry Box
v = StringVar()
e = Entry(root, textvariable=v, width=60)
e.pack()


# YouTube Callback(WakeyCore)
def youTube(event):
    playList = filePath + "playList.txt"
    youList = Entry.get(e)
    print(youList)
    youtubePlayList(youList)
    playerVLC(playList)


# Buttons
button_1 = Button(root, text="Start Playlist")
button_1.bind("<Button-1>", youTube)
button_1.pack()

root.mainloop()
