import random #use Python random package to get random numbers

carType = ["sedan", "suv"] #store two possible values for answer
answer=0

while carType[0] != answer and carType[1] != answer:
  answer = input("Please choose the type of your car: sedan or suv? ")
if answer == carType[0]:
    print("Your parking spot is: ", random.randrange(1, 101, 1)) #prints random parking spot number  between 1 and 100 for car type chosen as sedan
elif answer == carType[1]:
    print("Your parking spot is: ", random.randrange(101, 201, 1)) #prints random parking spot number  between 101 and 200 for car type chosen as SUV
else:
    print("Type chosen incorrectly") 