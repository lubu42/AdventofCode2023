file = open('input.txt', 'r')
lines = file.readlines()
import re

counter = 0
"""
#Part 1
for line in lines:
    for index, char in enumerate(line):
        if char.isdigit():
            firstnum = char
            break
        
    for char in reversed(line):
        if char.isdigit():
            lastnum = char
            break
    
    finalnum = (firstnum + lastnum)
    counter = counter + int(finalnum)    
"""
#Part 2
replacenum = {'one' : 'on1e', 'two' : 'tw2o', 'three' : 'thr3e','four': 'fo4ur', 'five':'fi5ve','six': 'si6x','seven': 'sev7en','eight' : 
'ei8ght','nine':'ni9ne'}

for line in lines:
    for key,value in replacenum.items():
        line = line.replace(key, value)
        print(line)
    digits = re.sub('\D','',line)
    counter += int(digits[0] + digits[-1])

print(counter)
