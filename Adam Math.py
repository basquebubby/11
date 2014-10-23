print "Hello my name is Adam, what is your name?"
username = raw_input("Name: ")
print "Hello " + username + ". What can I do for you?"

def whatToDo(): #function to tell the program what to do
    print "I can add, subtract, multiply, or divide. To exit type 'end'."
    answer = raw_input("What do you want me to do?: ")
    
    def add(): #Additon function
        addone = raw_input("First Number: ")
        addtwo  = raw_input("Second Number: ")
        total = int(addone) + int(addtwo)
        print username + ", your numbers added equals " +  str(total)
        whatToDo()
    
    def subtract(): #Subtraction function
        firstnumber = raw_input("First Number: ")
        secondnumber = raw_input("Second Number: ")
        if firstnumber > secondnumber:
            total = int(firstnumber) - int(secondnumber)
        elif int(secondnumber) > int(firstnumber):
                total = int(secondnumber) - int(firstnumber)
        print username + ", your numbers subtracted equals " +  str(total)
        whatToDo()
    
    def multiply(): #Multiplication function
        firstnumber = raw_input("First Number: ")
        secondnumber = raw_input("Second Number: ")
        total = int(firstnumber) * int(secondnumber)
        print username + ", your numbers multiplied equals " +  str(total)
        whatToDo()
    
    def divide(): #Division function
        firstnumber = raw_input("First Number: ")
        secondnumber = raw_input("Second Number: ")
        if firstnumber > secondnumber:
            total = int(firstnumber) / int(secondnumber)
        elif secondnumber > firstnumber:
            total = int(secondnumber) / int(firstnumber)
        print username + ", your numbers divided rouphly equals to " + str(total)
        whatToDo()
    
    if answer == "add":
        add()
    if answer == "subtract":
        subtract()              #Tells program what command to do
    if answer == "multiply":
        multiply()
    if answer == "divide":
        divide()

import time
time.sleep(1) #Pauses the program for second to give you time to read it
whatToDo()