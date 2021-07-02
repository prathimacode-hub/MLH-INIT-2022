from WakeyCore import youtubePlayList, playerVLC
from WakeyHueAlert import *
import time

AlarmTime = input("What time shall I wake you sir? ")
#PlayList = input("Playlist? ")
#playList = "C:\\logs\\goats.txt"


def AlarmClock(Time):
    currentTime = time.strftime("%H:%M")
    if currentTime == AlarmTime:
        print("Alarm!!!!")
        hueyBlue()
        #youtubePlayList(PlayList)
        #playerVLC(playList)
        time.sleep(60)
        AlarmClock(AlarmTime)
    else:
        print(currentTime)
        time.sleep(5)
        AlarmClock(AlarmTime)

AlarmClock(AlarmTime)
