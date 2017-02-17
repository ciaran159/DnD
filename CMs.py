# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 22:05:39 2016

@author: Ciarin Martin
"""

class Character(object):
    def __init__(self,stats,mods,level,Class,weapons):
        self.str=stats[0]
        self.dex=stats[1]
        self.con=stats[2]
        self.int=stats[3]
        self.wis=stats[4]
        self.cha=stats[5]
        self.pro=stats[6]
        self.strM=mods[0]
        self.dexM=mods[1]
        self.conM=mods[2]
        self.intM=mods[3]
        self.wisM=mods[4]
        self.chaM=mods[5]
    def getStr(self):
        lst=[self.str,self.strM]
        return lst
    def getDex(self):
        lst=[self.dex,self.dexM]
        return lst
    def getCon(self):
        lst=[self.con,self.conM]
        return lst
    def getInt(self):
        lst=[self.int,self.intM]
        return lst
    def getWis(self):
        lst=[self.wis,self.wisM]
        return lst
    def getCha(self):
        lst=[self.cha,self.chaM]
        return lst
    def getPro(self):
        return self.pro

def getMod(stat):
    if stat==8 or stat==9:
        return -1
    elif stat==10 or stat==11:
        return 0
    elif stat==12 or stat==13:
        return 1
    elif stat==14 or stat==15:
        return 2
    elif stat==16 or stat==17:
        return 3
    elif stat==18 or stat==19:
        return 4
    elif stat==20 or stat==21:
        return 5
    elif stat==22 or stat==23:
        return 6

def StatModChanger(changeStats,path1):
    NewMods=[]
    for x in range(6):
        NewMods.append(getMod(changeStats[x]))
    with open(path1, 'w+') as f:
        for x in range(7):
            input=str(changeStats[x])+"\t"
            f.write(input)
        for x in range(6):
            input=str(NewMods[x])+"\t" if x<5 else str(NewMods[x])
            f.write(input)

def addProfile(path,name):
    with open(path, 'a') as f:
        f.write("\t"+name)

def initialProfile(path,name):
    with open(path, 'a') as f:
        f.write(name)

def createProfile(num):#if num==0 it's first profile
    line=[]
    import os
    print("Enter your profile name")
    Username=raw_input()
    UsernameFile=Username+".txt"
    path=os.path.abspath(UsernameFile)
    
    newStats=[]
    for x in range(1,8):
        print ("Enter stat: "+str(x)) if x<7 else ("Enter proficiency bonus")
        newStats.append(int(raw_input()))
    StatModChanger(newStats,path)
    with open(path,'r') as f:
        line=f.read().split("\t")
    if num!=0:
        addProfile(os.path.abspath("Profiles.txt"),Username)
        return line
    else:
        initialProfile(os.path.abspath("Profiles.txt"),Username)
        return line

def mainMenu():
    import os
    line=""
    stats=[]
    mods=[]
    profiles=[]
    profilePath=os.path.abspath("Profiles.txt")
    with open(profilePath,'r') as f:
        profiles=f.read().split("\t")
    if profiles[0]=="":#checking if the first string is empty string i.e file empty
        line=createProfile(0)#num is 0 if first profile only
        stats=[int(line[x]) for x in range(7)]
        mods=[int(line[x]) for x in range(7,len(line))]
    else:
        print ("Current Profiles: "),
        print profiles
        print ("Make selection 1 or 2")
        print ("1. Use profile")
        print ("2. Create new profile")
        resp=0
        while(True):
            resp=int(raw_input())
            if resp!=1 and resp!=2:
                print("Invalid selection try again")
            else:
                break;
        if resp==1:
            #USING A CURRENT PROFILE
            while(True):
                try:
                    print("Enter your profile name")
                    Username=raw_input()
                    Username=Username+".txt"
                    path=os.path.abspath(Username)
                    
                    with open(path, 'r') as f:
                        line=f.read().split("\t")
                        break;
                except IOError:
                    print("Not valid name, please try again.")
            stats=[int(line[x]) for x in range(7)]
            mods=[int(line[x]) for x in range(7,len(line))]
        elif resp==2: #CREATING A NEW PROFILE
                    line=createProfile(1)#num is 0 if first profile only
                    stats=[int(line[x]) for x in range(7)]
                    mods=[int(line[x]) for x in range(7,len(line))]
    
    print ("Your stats are "),
    print stats
    print ("Your modifiers are "),
    print mods
    
    
    while True:    #setting up changed stats
        print ("Are these correct? y/n")
        resp=raw_input()
        if resp=="n":
            changeStats=[]
            
            for x in range(1,1+len(stats)):
                y=("Enter stat: "+str(x)) if (x<7) else ("Enter proficiency bonus")
                print y
                changeStats.append(int(raw_input()))
            print changeStats
        elif resp=="y":
            break;
        else:
            print "Invalid selection, please enter only y/n"
    
    
    Player=Character(stats,mods,0,"","")#last isn't actually a string just a placeholder for now
    return Player        