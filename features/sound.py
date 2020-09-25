# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:48:49 2020

@author: rachana
"""
import pyttsx3
#python to sound

#1 initialise module
voice = pyttsx3.init()

#2 inbuilt method say
voice.say("coooool both of you")

#3
voice.runAndWait()
