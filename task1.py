#Variable 1
a = int(input("What is the first number?: "))
#Variable 2
b = int(input("What is the second number: "))
#Variable 3
c = int(input("What is the third number?: "))
#List of variables
cab = str(a),str(b),str(c)

#Determing which numbers are bigger
if a > b:
    #printing V1  > V2 
    print(str(a) + " Is bigger than " + str(b))
elif a < b:
    #Printing V1 < V2
    print(str(b) + " Is bigger than " + str(a))
    
    #Determining if V1 is even or odd
if a % 2 == 0:
    #Printing V1 is even
    print (str(a) + " Is an even number")
elif a % 2 != 0:
    #Printing V1 is odd
    print (str(a) + " Is an odd number")
    
print ("The numbers in Ascending order are: ")
print (sorted(cab))
    
