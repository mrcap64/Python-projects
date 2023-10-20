#Note on how to  enter times
print("Please enter your time as --.--.Digits to the left of the decimal point are minutes,digits to the right are seconds")
#Time taken to swim in Triathlon
swim = float(input("How much time did you take to SWIM in the Triathlon?: "))
#Time taken to cycle in Triathlon
cycle =float(input("How much time did you take to CYCLE  in the Triathlon?: "))
#Time taken to run in Triathlon
run = float(input("How much time did you take to RUN in the Triathlon?: "))
#Total time taken
total = ((swim)) + ((cycle)) + ((run))
PC = float(100.00) #Provincial Colors
PHC = float(105.00) #Provincial Half Colors
PS = float(110.00) #Provincial scroll

if (total) <= (PC):
    #Award given for total <= 100 mins
    print("Congratulations you have acquired Provincial Colours,your total time was: " + str(total) + "mins")
elif (total) > (PC) and (total) <= (PHC):
    #Award given for total <= 105 mins
    print("Congratations you have acquired Provincial half colours,your total time was: " + str(total) + "mins")
elif (total) > (PHC) and (total) <= (PS):
    #Award given for total <= 110 mins
    print("Congratulations you have acquired a Provinvial Scroll,your total time was: " + str(total) + "mins")
else: #No award given because total is too big
    print("Unfortunately you have not earned any award,your total time was: " + str(total) + "mins")
