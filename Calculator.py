def prompt_menu():
    #Variable 1
    a = float(input("Enter the 1st number: "))
    #Variable 2
    b = float(input("Enter the 2nd number: "))
    #List of different operations available to be used
    print ("""Please choose from the options below which operation you would like:
       1.Addition
       2.Subtraction
       3.Multiplication
       4.Exponentiation
       5.Division
       6.Division with remainder
        """)
    #Operation being used
    op = int(input("Enter the number of your choice: "))
    return a,b,op

def calculate():
    a, b, op = prompt_menu()
    #Formula for Addition
    if op == 1:
         print ("Sum: {} + {} = {}".format (a,a,a+b))
    #Formula for Subtraction
    elif "op" == 2:
         print ("Difference: {} - {} = {}".format(a,b,a-b))
    #Formula for Multiplication
    elif op == 3:
         print ("Product: {} * {} = {}".format(a,b,a*b))
    #Formula for Exponentiatian
    elif op == 4:
         print ("Power: {} ^ {} = {}".format(a,b,a**b))
    #Formula for Division
    elif op == 5:
         try:
             print ("Division: {} / {} = {}".format(a,b,a/b))
         except:
             print ("Division by " + (b) + " is not possible")
    #Formula for Division with remainder
    elif op == 6:
         try:
             print ("Division with remainder: {} / {} = {} Remainder: {}".format(a,b,a//b,a%b))
         except:
             print ("Division by " + (b) + " is not possible") 
         
         loop() 

def loop():
    choice = input("Do you want to do another opeation? (Y,N): ")
    if choice.upper() == "Y":
        calculate()
    elif choice.upper() == "N":
        print ("We,hope to see you again,remember to share this produt of Taffy Tech™,untill next time.")
    else:
        print ("Invalid Input")
        loop()

calculate()