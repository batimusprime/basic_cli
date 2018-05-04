# -*- coding: utf-8 -*-
"""
Basic CLI
Present user options, record results, exit upon command
Demonstration of concept / learning
Created on Fri May the 4th 06:47:44 2018
@author: https://github.com/BatimusPrime
"""
#creating the simplest list
test = ['a','b','c']

#setting response variable to empty value
r = ''

#create list to display user's response selections
r_list = []

#display selection options
for t in enumerate(test):
    
    #I think +1 is correct here because I want the user to select a value not the index
    #I think it needs to be removed when indexes and values don't align, i.e. text is used
    print(t)

#keep running until user enters 'q' for quit
while r != 'q':
    #ask user for selection, save as lowercase str 'resp'
    r = input('Please select a number, enter \'q\' to quit:  ').lower()
    
    #shutdown sequqnce will run through loop final time if test for q is not performed
    if r == 'q':
        
        #shutdown message
        print('Quitting...')
    
    #only accept numbers
    elif r.isnumeric() == False:
        
        #error message
        print('enter valid selection')
    
    #make sure the user's entry is in the list
    else: 
        
        #convert to integer - cannot compare int and str with >
        r = int(r)
        
        #
        if (r > len(test)):
            print('Enter a number displayed')
        
        else:
            
            #record user's selection
            r_list.append(r)
            #print the results
            for tw in test:
                print(tw)
                

