import random
#A function to shuffle all the characters

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join (tempList)

#Main program,configuring numbers using ASCII

#Obtaining 1st Uppercase Letter between A and Z
UcCh1 = chr(random.randint(65,90)) 
#Obtaining 2nd Uppercase Letter between A and Z
UcCh2 = chr(random.randint(65,90))
#Obtaining 1st Lowercase Letter between a and z
LcCh1 = chr(random.randint(97,122)) 
#Obtaning 2nd Lowercase Letter between a and z
LcCh2 = chr(random.randint(97,122)) 
#Obtaining 1st Number between 0 and 9
NuCh1 = chr(random.randint(48,57)) 
#Obtaining 2nd Number between 0 and 9
NuCh2 = chr(random.randint(48,57)) 
#Obtaining 1st Special Character
SpCh1 = chr(random.randint(32,47)) 
#Obtaining 2nd Special Character
SpCh2 = chr(random.randint(123,126))

#Password order
password = (UcCh1) + (LcCh2) + (NuCh1) + (SpCh2) + (NuCh2) + (UcCh2) + (SpCh1) + (LcCh1)
#Password shuffling
password = shuffle(password)

#Randomly generated password
print(password)






