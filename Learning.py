# This is to comment on the code...
# The line below is to simply print out text in the python program
print("Change da world, my final message, goodbye")
# math skills demo
# this is to display text and it will display a number as well, in this case being 1
print("the number of protons in hydrogen", 1)
# the line below allows you to create math, this one is adding 15 to 30 divided by 6
print("random Math", 15.0+30.0/6.0)
# the line below is also doing math, this one is subtracting 100 from 25 times 13
print("even more math", 100.0-25.0*13.0)
# the line below is giving the remainder of 2+34/2 when the answer is divided by 2
print("I am going to sleep", 2.00+34.0000/2.00 % 2.0)
# The line below is doing the same as above but with a different equation (the remainder of (3+2+1-5+4)/(2-1/4+6)
print("The length of about half of a 12 inch ruler", 3.0+2.0+1.0-5.0+4.0 % 2.0-1.0/4.0+6.0)
# The last line is calculating a large number because I don't have anything I need to calculate at the moment
print("using math to find super big numbers because I don't really have many things to calculate",(346.00*15.0**2.0)**16.0/(2.0 % 55.0))
# a floating point number is a representation of real numbers as an approximation to create a trade off between range and precision. they can be incredibly small or incredibly large numbers.

# Variables and their powers
cars = 80
SpaceInACar = 4.0
drivers = 45
passengers = 115
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capactiy = SpaceInACar * cars_driven
average_passengers_per_car = passengers / cars_driven

print("there are", cars, "cars available.")
print("there are only", drivers, "drivers available today.")
print("there will be", cars_not_driven, "empty cars today.")
print("we can transport", carpool_capactiy, "people today.")
print("We have", passengers, "to carpool today.")
print("we need to put approximately", average_passengers_per_car, "in each car.")

# more variables
myName = "Joseph"
myAge = 16
myHeight = 72 # inches
myEyes = "Blue"
myHair = "Brown"

print("let's talk about %s" % myName)
print("He's %d inches tall" % myHeight)


# My own Variable story!
PaperSheets = 3000000000
PricePerSheet = 0.01
Consumers = 1327
PaperInAPack = 500
PriceOfPack = PricePerSheet * PaperInAPack
AmountOfPacks = PaperSheets / PaperInAPack
AverageAmountOfPacksBoughtPerMonth = 123.4
AverageAmountMadeOffEachConsumer = AverageAmountOfPacksBoughtPerMonth * PriceOfPack
PotentialAmountMade = (PriceOfPack * AmountOfPacks)
CurrentAmountMade = 3 * (Consumers * AverageAmountMadeOffEachConsumer)

Print("We have", AmountOfPacks, "paper packs available, with a total of", PaperSheets, "sheets of paper.")
Print("Each pack is sold at", PriceOfPack, "dollars, with", PaperInAPack, "sheets per pack.")
Print("We sell an average of", AverageAmountOfPacksBoughtPerMonth, "for a total of", AverageAmountMadeOffEachConsumer, "dollars made per month.")
Print("We can make", PotentialAmountMade, "dollars in total, but have only made", CurrentAmountMade, "dollars so far.")

