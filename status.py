#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
## testing auto iteration file creation and updating 
##
import random
import os

s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "rewards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "rewards", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]

def sing_sen_maker():
    '''Makes a random senctence from the different parts of speech. Uses a SINGULAR subject'''
    # if input("Would you like to add a new word?").lower() == "yes":
    #     new_word = input("Please enter a singular noun.")
    #     s_nouns.append(new_word)
    # else:
    
    while True:
    	return random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)


file_name = "test.yml" 
new_string = str(sing_sen_maker())
opened_file = open(file_name, 'a')
opened_file.write("%r\n" %new_string)
opened_file.close()
