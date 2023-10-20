#Users name
name = str(input("Hello who are you?: "))
#Aquiring users detail
print ("Hello," + name + "!Please just give me a few details and I will make a great Introduction for your speech")
#Users age
age = int(input("How old are you?(e.g.27): "))
# Users Place Of Birth
POB = str(input("Where were you born?(e.g.Cape Town): "))
#Users Place Of Residence
POR = str(input("Where do you currently stay?(e.g.Stellenbosch): "))
#The topic the user will be talking about
topic = str(input("What are you going to talk about?(e.g.Climate Change): "))
#What the AI is able to generate
print("This is what I was able to create: ")
#CREATION

#Statement for if users POB = POR
if (POB) == (POR):
   #Stating name of users
   print ("Hello everyone my name is " + (name)  + ".")
   #Stating POR and POR of user
   print ("I was born in " + (POB) + " and I still stay in " + (POR) + ".")
   #Stating topic user will be talking about
   print ("Today I will be talkig about " + (topic) + ".")
   #Transition to findings(Middle) user has made
   print ("So,without further,ado lets jump right into my findings")
   
   print ("I hope this is what you were looking for,thank you for using a product of Taffy Tech™")
else:
   #Stating name of user
   print ("Hello everyone my name is " + (name)  + ".")
   #Statin POB and POR of user
   print ("I was born in " + (POB) + " but now I am currently staying in " + (POR) + ".")
   #Stating topic user will be using
   print ("Today I will be talkig about " + (topic) + ".")
   #Tansition to findings(Middle) user has made
   print ("So,without further,ado lets jump right into my findings")
   
   print ("I hope this is what you were looking for,thank you for using a product of Taffy Tech™") 
