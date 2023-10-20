#The user's variable
usr_inp = int(input("Please enter number to get divided: "))

#Determining if users input is divisable by 2 and 5
if usr_inp % 2 == 0 and usr_inp % 5 ==0:
    print(str((usr_inp)) + ' is divisable by 2 and 5')
#Determining if users input is divisible by 2 and not 5
elif usr_inp % 2 == 0 and usr_inp % 5 != 0:
    print(str((usr_inp)) + '  is divisable by 2,but not divisible by 5')
#Determining if users input is divisible to 5 and not 2
elif usr_inp % 2 != 0 and usr_inp % 5 == 0:
    print(str((usr_inp))  + ' is not divisable by 2,but is divisible by 5')
#Last option,shown when users input is not divisible by 2 or 5
else:
    print(str((usr_inp)) + ' is not divisable by 2 or 5 ') 