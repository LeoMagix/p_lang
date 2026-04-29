"""
Creates a regex file to match patterns of phone numbers and email addresses.
As a side note, the program may not reach its full potential due to our 
current inability to install pyperclip module. We will need a vitual
environment to manage that, I need more knowledge on that.
"""
#import pyperclip
import re

#Create a regex patten to match phone numbers
phoneNo = re.compile(r'''(
                     (\+234|\d{3}\d)?          #Intertanational code
                     (\s)?                       #Optional space between digits
                     (\d{3,4})                     #Next batch of numbers
                     (\s)?                       #Space separator for legibilty
                     (\d{3})                       #Next batch of numbers
                     (\s)?                       #Again optional separator
                     (\d{3,4})                     #Final batch of numbers
                     )''', re.VERBOSE)      #My first real application of the verbose method.



#Create a regex pattern to  match Email addresses
emailAdr = re.compile(r'''(
                      [a-zA-Z0-9_+%.-]+         #Username
                      @                         #Separator
                      [a-zA-Z0-9.-]+            #Host name
                      (\.[a-z0-9]{2,3})         #Domain name
                      )''', re.VERBOSE)


emails = emailAdr.findall('dahleo@gmail.com, dave_leo25@outlook.com, adah.david29@yahoo.com')
#print(emails)

ph = phoneNo.findall('+234 806 703 1285, 08035980455, 0707 963 3311')
#print(ph)

#Find all maches and store them in a list
matches = []
for email in emails:
    matches.append(email[0])

for groups in ph:
    if groups[1] != '':
        match = ' '.join([groups[1], groups[3], groups[5], groups[7]])
    else:
        match = ' '.join([groups[3], groups[5], groups[7]])
    matches.append(match)

#print(matches)
if len(matches) > 0:
    all_match = '\n'.join(matches)
    print('Found Matches:')
    print(all_match)
