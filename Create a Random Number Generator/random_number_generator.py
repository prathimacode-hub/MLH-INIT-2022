#This program will give you a random number 
import random
from tkinter import *

def randomNumber():
    lowestNumber=eval(lowNumEnt.get())
    highestNumber=eval(highNumEnt.get())
    randomNumber=random.randint(lowestNumber,highestNumber)
    randNum.set(randomNumber)

    
    

#creates the title and window for the program
master=Tk()
master.title('Random Number Generator')
titlelbl=Label(master, text='Random Number Generator',font=('Century',18,'bold italic'))
titlelbl.grid(row=0,column=0,columnspan=5,sticky=N,padx=5)
titlelbl.config(bd=4, relief='sunken',width=23)

#creates a label and entry for the low number
lowNumlbl=Label(master,text='Enter the lowest number in range:',font=('Verdana',10))
lowNumlbl.grid(row=1,column=0,sticky=W,pady=10,padx=10)
lowNumEnt=Entry(master)
lowNumEnt.grid(row=1,column=1,columnspan=2,padx=10,pady=10,)


#creates a label and entry for the high number
highNumlbl=Label(master,text='Enter the highest number in range:',font=('Verdana',10))
highNumlbl.grid(row=2,column=0,sticky=NW,pady=5,padx=10,)
highNumEnt=Entry(master)
highNumEnt.grid(row=2,column=1,padx=10,pady=5,sticky=NW)


#Displays the random number
randNum=StringVar()
randomNumlbl=Label(master,text='Random Number',font=('Verdana',10))
randomNumlbl.grid(row=1,column=3,columnspan=2,pady=5,padx=40,sticky=NW)
randomEnt=Entry(state='readonly',fg='green',textvariable=randNum)
randomEnt.grid(row=1,column=3,columnspan=2,pady=30,padx=40,sticky=SW)



#Creates a button to calculate and generate the random number
calcBtn=Button(master,text='Calculate',font=('Georgia',13),command=randomNumber)
calcBtn.grid(row=2,column=3,columnspan=2,pady=10,padx=40)


    
