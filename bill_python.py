#Margaret Diaz
#Practice for how to split the bill

import math


#Input:
# enter the price of bill 
# the number of ppl, enter price for each dish
# enter the sales tax, automatic if nyc
# calculate the tip and display
# select option
# output what each person has to pay

#if only one person, you dont have to input food
#maybe ask how many people first, ask if you ordered more than one item
#then calculate it!

name = ''
name = input("Please enter your name: ")
while name == '': #while they don't respond
    name = input("Sorry, could you please enter your name: ")
print("Welcome ",name, "to the bill splitter!")
#1. input the price of the bill, tip, tax, # of ppl
InputBill = '' 
InputBill = input('Enter the price of the bill: ')
while InputBill == '': #while they don't respond
    InputBill = input('Sorry could you please enter the price of the bill: ')
bill = float(InputBill) #convert their string into float
Inputnum = ''
Inputnum = input('Enter the number of ppl: ') 
while Inputnum == '': #while they don't respond
    Inputnum = input('Sorry could you please enter the number of ppl: ')
num = float(Inputnum) #convert their string into float
inputTip = ''
inputTip = input('Enter the percentage of tip: ')
while inputTip == '': #while they don't respond
    inputTip = input('Sorry could you please enter the percentage of tip: ')
Tip = (float(inputTip)/100) * bill #convert their string into float, turn into percentage and multiply to bill
Nyc = ''                        
Nyc = input('Are you in NYC?, Y or N: ') 
while Nyc == '': #while they don't respond
    Nyc = input('Sorry are you in NYC?, Y or N: ')
if Nyc == 'Y' or 'y' or 'yes': #checks for multiple option
    inputTax = bill * .08875 #automatic sales tax for NYC
else:
    inputTax = input('Enter the sales tax: ')
    while inputTax == '': #while they dont respond
        inputTax = input('Sorry but could you please the sales tax: ')
tax = float(inputTax)/num
add = Tip + tax #what needs to be added to the their food cost
#2 calculate the user input
sum = 0
total = 0
inputFoods = ''
foods = [] #creating array
while inputFoods != 'done':
    ###optional if wanted to add their food name###
    #inputFoods = input("Enter the name of the food, or enter 'done': ")
    #if inputFoods != 'done':
        #foods.append(inputFoods)
        #total = float(input("Enter the price of the food: "))
        #sum += total
    inputFoods = input("Enter the price of the food, or enter 'done': ")
    while inputFoods == '':  #while they dont respond
        inputFoods = input("Sorry but could you please the price of the food, or enter 'done': ")
    if inputFoods != 'done': #if they dont select done
        foods.append(inputFoods) #add the price to the array
        total = float(inputFoods) #save their total
        sum += total #add it to the sum
#3. out put
owe = sum + add ##what they owe
print('\n',name+ "'s", "bill is")
for x in foods: #goes through each price in the array and prints it out
    print("$", x)
print("The sum of", name+"'s"," food is", round(sum,2)) #to the 100th place
print(name+"'s","tip and tax is ", round(add,2)) #to the 100th place
print(name, "needs to pay ", round(owe,2)) #to the 100th place
print("Thank you", name, "have a good rest of the day! \n")
        
    
#.8875, bill, NY state
#food not needed just price


#next steps:
#look like a recipet with coffee
#select their state