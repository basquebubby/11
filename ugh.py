waitinglist = []
numberofpatients = raw_input('How many patients are there: ')
number = int(numberofpatients)
while int(number) > 0:
    number = number - 1
    name = raw_input('Name: ')
    waitinglist.append(name)
length =  len(waitinglist) - 1
while int(length) >= 0:
    length = int(length) - 1
    q1 = raw_input('What is your temperature: ')
    q2 = raw_input('Have you been sick in the past 24 hours y/n: ')
    q3 = raw_input('Have you been to africa in the past week y/n: ')
    q1
    q2
    q3
    if int(q1) >= 105:
        print "Go to the hospital!"
        length
    elif int(q1) >=102 and int(q1) < 105:
        if str(q2) == str('y'):
            print 'Go to the hospital!'
            length
        elif str(q2) == str('n'):
            print "Your fine."
            length
    elif int(q1) >= 100 or str(q2) == str('y') and q3 == str('y'):
        print "Go to the hospital!"
        length
    elif int(q1) >= 100 or str(q2) == str('y') and q3 == str('n'):
        print "Your fine."
        length