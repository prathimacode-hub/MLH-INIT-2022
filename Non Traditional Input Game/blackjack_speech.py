# coding: utf-8

# In[1]:

from random import randint
import random
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from IPython.display import display
import speech_recognition as sr

def say():                                 #Function to take audio as string input
    string=""
    r = sr.Recognizer()                      # Speech recognition using Google Speech Recognition
    with sr.Microphone() as source:
        print("Say something ")
        audio = r.listen(source)
        
    try:
        string=r.recognize_google(audio)
        print("You said: " +string)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        string="unclear"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        string="unclear"
        
    return string





class Player(object):
    reserve=200
    numplayers=0
    cardsum=0
    def __init__(self,name):
        self.name=name
        Player.numplayers=Player.numplayers+1  #Changing the value of static variable
        self.id=Player.numplayers      #assigning the value of static class variable to object variable
        self.numcards=0
        self.cardsum=0
        self.cardlist=[]
        self.balance=Player.reserve
    
    def getcard(self,card):
        if (card.value==1 and self.cardsum==10 and self.numcards==1)or (self.cardsum==1 and card.value==10 and self.numcards==1):
            self.cardsum=21
        else:
            self.cardsum=self.cardsum+card.value
        self.numcards+=1
        self.cardlist.append(card.name)
        
    def bet(self,betamount):
        if betamount>self.balance:
            print "You don't have this much balance to bet"
            return -1
        self.balance=self.balance-betamount
        self.betamount=betamount
        return "betting done"
        
    def move(self, action):
        while action=="unclear":
            print "Speak again"
            action=say()
        while self.cardsum==21 and action == "hit":
            print "You have a Blackjack!!. So,no hit. Only stay. Move again"
            action=say()
            self.move(action)
        if self.numcards==2 and action=="surrender":
            self.cardsum=-1
            return "surrender"
        while self.numcards!=2 and action=="surrender":
            print "Invalid move. Can't surrender at this stage.Move again "
            action=say()
            self.move(action)
            
        if action=="stay":   
            return "stayed"
        
        if action=="hit":
            card=Card()
            self.getcard(card)
            df=DataFrame({self.name:[self.cardsum,card.name,action]},index=["New card sum","Recently included card","Action"])
            display(df)
            if self.cardsum>21:
                print self.name+"bust!!"
                return "bust"
            print card.name+" Attained. Next move now "
            action=say()
            self.move(action)
        
        
    def statusupdate(self,status):
        if status=="Surrender":
            self.balance+=(1.0/2)*self.betamount
        elif status=="Blackjack!!!"or status=="win" or status=="Dealer bust!!. Win":
            self.balance+=(5.0/2)*self.betamount
        elif status=="Push. No gain, no loss":
            self.balance+=self.betamount
        else : 
            return
            
    
    def outcome(self,dealersum):
        status=""
        if self.cardsum==-1:
            status="Surrender"
        elif dealersum>21 and self.cardsum<=21:
            status="Dealer bust!!. Win"
        elif self.cardsum>21:
            status= "bust"
        elif self.cardsum==21 and dealersum!=21:
            status= "Blackjack!!!"
        
        elif self.cardsum==dealersum:
            status= "Push. No gain, no loss"
        elif self.cardsum<dealersum:
            status ="loose"
        else: status="win"
        
        self.statusupdate(status)
        return status
        
    


# In[2]:

class Dealer(object):
    def __init__(self):
        self.numcards=0
        self.cardsum=0
        
    def getcard(self):
        card=Card()
        if (self.cardsum==1 and card.value==10)or(self.cardsum==10 and card.value==1):
            self.cardsum=21
        else:
            self.cardsum+=card.value
        self.numcards+=1
        return card
    
        
    
        
    


# In[3]:

class Card(object):
    
    suits = ('Heart','Diamond','Club','Spade')
    ranking = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
    card_val = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}
    
    def __init__(self):
       
        self.suit=random.choice(Card.suits)
        self.rank=random.choice(Card.ranking)
        self.value=Card.card_val[self.rank]
        self.name=""+self.suit+":"+self.rank


# In[6]:

def initialise():
    print "Game initialised"
    playerlist=[]
    activeplayerlist=[]
    print "Player 1, what's your name"
    name=say()
    while name=="unclear":
        print " Unclear, say again"
        name=say()
    i=2
    while name!="over":
        p=Player(name)
        activeplayerlist.append(p)
        st="Player "+str(i)+", what's your name"
        print st
        name=say()
        while name=="unclear":
            print " Unclear, say again"
            name=say()
        i+=1
    return activeplayerlist


def gameplay(activeplayerlist):
    
    
    d={}
    for player in activeplayerlist:
        d[player.name]=player.balance
    df=DataFrame(d,index=["Balances"])
    display(df)
    
    
    for player in activeplayerlist:
        if player.balance==0:
            activeplayerlist.remove(player)
            print player.name+" is out of the game"
    
    
    for player in activeplayerlist:
        player.betamount=0
        player.cardsum=0
        player.numcards=0
        player.cardlist=[]
    
    for player in activeplayerlist:
        st="Say the bet amount for "+player.name
        print st
        betamountstring=say()
        while type(betamountstring)!=unicode:
            print "Non integer bet said. Say again"
            betamountstring=say()
        betamount=(int)(betamountstring)
        b=player.bet(betamount)
        while b==-1:
            st="Say again for "+player.name
            betamountstring=say()
            while type(betamountstring)!=unicode:
                print "Non integer bet said. Say again"
                betamountstring=say()
            betamount=(int)(betamountstring)
    
    if len(activeplayerlist)==1:
        return
    
    d={}
    index=["balance","bet amount"]
    for player in activeplayerlist:
        l=[]
        l.append(player.balance)
        l.append(player.betamount)
        d[player.name]=l
    
    gamestatus=DataFrame(d,index)
    display(gamestatus)
        
        
    print "Card Distribution!!"
    print "First card distribution"
        
    for player in activeplayerlist:
        card1=Card()
        print "Fist card of"+player.name+":"+card1.name
        player.getcard(card1)
        
    print "Second Card distribution"
    
    for player in activeplayerlist:
        card2=Card()
        print "Second card of"+player.name+":"+card2.name
        player.getcard(card2)
        
    dealer=Dealer()
    dealer_first_card= dealer.getcard() 
    print "Dealer shows a "+dealer_first_card.name
    
    df=DataFrame({'Dealer':[dealer_first_card.name]},index=["Dealer's first card"])
    display(df)
    
    d={}
    index=["First card","Second Card","Card Sum"]
    for player in activeplayerlist:
        l=player.cardlist
        l.append(player.cardsum)
        d[player.name]=l
    
    gamestatus=DataFrame(d,index)
    display(gamestatus)
        
    
    
    
    for player in activeplayerlist:
        print "Player "+player.name+", Yell your decision hit/stay/surrender: "
        action=say()
        while action!="hit" and action!="stay" and action!="surrender":
            print "Invalid choice. Speak again"
            action=say()
        print player.move(action)
            
        
    dealer_second_card= dealer.getcard()       
    print "Second card of dealer"+dealer_second_card.name
    if dealer.cardsum<17:
        dealer_third_card=dealer.getcard()
        print "Since dealer's cards have sum < 17, so dealer will include one more card. Third card of dealer"+dealer_third_card.name
        df=DataFrame({'Dealer':[dealer_first_card.name,dealer_second_card.name,dealer_third_card.name,dealer_first_card.value+dealer_second_card.value+dealer_third_card.value]},index=["Dealer's first card","Dealer's second card","Dealer's third card","Dealer's sum"])
    else:
        df=DataFrame({'Dealer':[dealer_first_card.name,dealer_second_card.name,dealer_first_card.value+dealer_second_card.value]},index=["Dealer's first card","Dealer's second card","Dealer's sum"])
    display(df)
    
    
    result=[]
    namelist=[]
    balancenow=[]
    for player in activeplayerlist:
        result.append(player.outcome(dealer.cardsum))
        balancenow.append(player.balance)
        namelist.append(player.name)
    
    resultdf=DataFrame({"Result":result,"New Balance":balancenow},index=namelist)
    display(resultdf)     
        
    
    
        
        
    


# In[7]:

players=initialise()
print "Tell the  number of rounds you wanna play:"
r=say()
while type(r)!=unicode:
    print "Non integer spoken. Say again"
    r=say()
rounds=(int)(r)
while rounds>0 and len(players)>1:
    gameplay(players)
    rounds=rounds-1
winner=""
if rounds==0:
    m=-1
    for player in players:
        if player.balance>m:
            m=player.balance
            winner=player.name
else:
    winner=players[0].name
        
    
print "WINNER OF THE GAME:"+winner


# In[ ]:
