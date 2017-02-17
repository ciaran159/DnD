# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 23:55:45 2016

@author: Ciarin Martin
"""
#Method Section
import CMs #holds all the methods for tidiness sake
import Actions #holds actions e.g saving throws, combat etc.

Player=CMs.mainMenu()#mainMenu returns a player object


print("Entering action section, when in menu prompt enter 'menu' to return to Character selection menu or enter 'exit' to exit")

while(True):
    print("0. Initiative")
    print("1. Combat")
    print("2. Saving Throws")
    print("3. Skill Checks")
    print ("Select an action")
    resp=raw_input()
    if resp!="0" and resp!="1" and resp!="2" and resp!="3" and resp!="exit" and resp!="menu":
        print("Invalid input")
    elif resp=="0":
        print(Actions.initiative(Player))
    elif resp=="1":
        print("combat")
    elif resp=="2":
        print("saving throws")
    elif resp=="3":
        print("ability checks")
        print(Actions.SkillCheck(Player))
    elif resp=="exit":
        break
    elif resp=="menu":
        Player=CMs.mainMenu() #will re-run with a new character if chosen

"""have it so you can go back to main menu at any time,
i.e each input be checked for esc"""

"""Completed set up, changing stats, creating new profile, using profile"""

"""Maybe add more specific character data like: level, class, weapons etc."""       

"""for saving throws and proficiencies make a list and use if <proficiency> in lst: """
"""more in depth character creation but sure fuck it"""