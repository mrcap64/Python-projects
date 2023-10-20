T = int(input("""What would you like the foundation to be? 
          1.a Square
          2.a Rectangle
          3.a Circle
          :"""))

if T == 1:
    L = float(input("What do you want the Length to be(Metres): "))
    print("The are of your building is: " + 
          str(L ** 2) + "m")

elif T == 2:
    L = float(input("What do you want the Length to be(Metres): "))
    W = float(input("What do you want the Width to be(Metres): "))
    print("The area of your building is: " + str(L * W) + "m")
elif T == 3:
    import math
    R = float(input("What do you want the Radius to be(Metres)?: "))
    print ("The area of your building will be: " + str(math.pi * R**2) + "m")