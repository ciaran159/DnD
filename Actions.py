# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 01:11:05 2016

@author: Ciarin Martin
"""

"""This is the file for actions"""
import random
def initiative(Player):
    while(True):
        print("Do you have advantage? y/n")
        resp=raw_input()
        if resp!="y" and resp!="n":
            print("Invalid input")
        elif resp=="n":
            mod=Player.getDex()[1]
            roll=random.randint(1,20)
            result=mod+roll
            return result
        elif resp=="y":
            mod=Player.getDex[1]
            rolls=[]
            rolls.append(random.randint(1,20))
            rolls.append(random.randint(1,20))
            result=mod+max(rolls)
            return result
            
def SkillCheck(Player):
    StatType=0
    while(True):
        print("Select the Ability Check from the following list")
        print("str, dex, con, int, wis, cha")
        resp0=raw_input()
        if resp0!="str" and resp0!="dex" and resp0!="con" and resp0!="int" and resp0!="wis" and resp0!="cha":
            print("Invalid input")
        elif resp0=="str":
            StatType=Player.getStr()[1]
            break
        elif resp0=="dex":
            StatType=Player.getDex()[1]
            break
        elif resp0=="con":
            StatType=Player.getCon()[1]
            break
        elif resp0=="int":
            StatType=Player.getInt()[1]
            break
        elif resp0=="wis":
            StatType=Player.getWis()[1]
            break
        elif resp0=="cha":
            StatType=Player.getCha()[1]
            break
        
    while(True):
        print("Do you have advantage? y/n")
        resp=raw_input()
        if resp!="y" and resp!="n":
            print("Invalid input")
        elif resp=="n":
            while(True):
                print("Are you proficient in this check? y/n")
                resp2=raw_input()
                if resp2!="y" and resp2!="n":
                    print("Invalid input")
                elif resp2=="n":
                    return (random.randint(1,20)+StatType)
                elif resp2=="y":
                    return (Player.getPro()+random.randint(1,20)+StatType)
        elif resp=="y":
            while(True):
                print("Are you proficient in this check? y/n")
                resp3=raw_input()
                if resp3!="y" and resp3!="n":
                    print("Invalid input")
                elif resp3=="n":
                    return (max({random.randint(1,20),random.randint(1,20)})+StatType)
                elif resp3=="y":
                    return (max({random.randint(1,20),random.randint(1,20)})+Player.getPro()+StatType)