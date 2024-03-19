def viewgro():   # for new customer/admin/Existing Customer view groceries detail
    x = True
    while x:
        print('\n----------------------------------   VIEW GROCERIES PAGE 🛒  ---------------------------------')
        ask2 = str(input('Do you want to view \n1.All groceries \n2.Household groceries \n3.Meat groceries \n4.Vegetable groceries \n:'))  # separate groceries into three categories: household /meat /vegetable
        if (ask2 == '1'): # view all groceries details
            print('\n-----------------------------   VIEW ALL GROCERIES DETAILS   ------------------------------')
            file = open('grocerydetail.txt', 'r') #open the file and read the line by line and split the line into each element
            for line in file.readlines():
                data = line.split(",")
                groceryname = str(data[0])
                amount = str(data[1])
                weight = str(data[2])
                price = str(data[3])
                print('Grocery name:' + groceryname + (' ' * (20 - len(groceryname))) + 'Amount:' + amount +(' ' * (10 - len(amount))) + 'Weight (g):' + weight + (' ' * (10 - len(weight))) + 'Price:' + price)
            file.close()
            while x:
                ask3 = str(input('\nDo you want to view other type of grocery (Yes/No): ')).lower()  # ask user want to see other categories groceries if yes looping will continue if no will stop this function
                if (ask3 == 'yes'):
                    break   # to continue line 3 : while loop
                elif (ask3 == 'no'):
                    x = False # stop looping
                else:
                    print('please input yes or no')
                    continue
        elif (ask2 == '2'):   # view household groceries details
            print('\n--------------------------   VIEW HOUSEHOLD GROCERIES DETAILS   ---------------------------')
            file = open('household.txt', 'r') #open the file and read the line by line and split the line into each element
            for line in file.readlines():
                data = line.split(",")
                groceryname = data[0]
                amount = str(data[1])
                weight = str(data[2])
                price = str(data[3])
                print('Grocery name:' + groceryname + (' ' * (20 - len(groceryname))) + 'Amount:' + amount + (' ' * (10 - len(amount))) + 'Weight (g):' + weight + (' ' * (10 - len(weight))) + 'Price:' + price)
            file.close()
            while x:
                ask3 = str(input('\nDo you want to view other type of grocery (Yes/No) : ')).lower()   # ask user want to see other categories groceries if yes looping will continue if no will stop this function
                if (ask3 == 'yes'):
                    break   # to continue line 3 : while loop
                elif (ask3 == 'no'):
                    x = False   # stop looping
                else:
                    print('please input yes or no')
                    continue
        elif (ask2 == '3'):   # view meat groceries details
            print('\n---------------------------   VIEW MEAT GROCERIES DETAILS   ----------------------------')
            file = open('meat.txt', 'r') #open the file and read the line by line and split the line into each element
            for line in file.readlines():
                data = line.split(",")
                groceryname = data[0]
                amount = str(data[1])
                weight = str(data[2])
                price = str(data[3])
                print('Grocery name:' + groceryname + (' ' * (20 - len(groceryname))) + 'Amount:' + amount + (' ' * (10 - len(amount))) + 'Weight (g):' + weight + (' ' * (10 - len(weight))) + 'Price:' + price)
            file.close()
            while x:
                ask3 = str(input('\nDo you want to view other type of grocery (Yes/No): ')).lower() # ask user want to see other categories groceries if yes looping will continue if no will stop this function
                if (ask3 == 'yes'):
                    break # to continue line 3 : while loop
                elif (ask3 == 'no'):
                    x = False # stop looping
                else:
                    print('please input yes or no')
                    continue
        elif (ask2 == '4'): # view vegetable groceries details
            print('\n-----------------------   VIEW VEGETABLE GROCERIES DETAILS   -----------------------')
            file = open('vegetable.txt', 'r')  #open the file and read the line by line and split the line into each element
            for line in file.readlines():  
                data = line.split(",")
                groceryname = data[0]
                amount = str(data[1])
                weight = str(data[2])
                price = str(data[3])
                print('Grocery name:' + groceryname + (' ' * (20 - len(groceryname))) + 'Amount:' + amount + (' ' * (10 - len(amount))) + 'Weight (g):' + weight + (' ' * (10 - len(weight))) + 'Price:' + price)
            file.close()
            while x:
                ask3 = str(input('\nDo you want to view other type of grocery (Yes/No): ')).lower() # ask user want to see other categories groceries if yes looping will continue if no will stop this function
                if (ask3 == 'yes'):
                    break   # to continue line 3 : while loop
                elif (ask3 == 'no'):
                    x = False  # stop looping
                else:
                    print('please input yes or no')
                    continue
        else: # if user enter wrongly will continue line 3: while loop
            print('please enter a number from 1 to 4')
            continue
#have three add grocery functions separate by category
def vegetable():  # add vegetable groceries
    x = True
    while x:
        list = []     # save all new groceries detail in this list
        list2 = []   # save existing groceries details
        file = open('grocerydetail.txt', 'r')  # open the file and read the line by line and split the line into each element and append groceries name to list2
        for line in file.readlines():  
            data = line.split(',')
            groname = data[0]
            list2.append(groname)
        while x:   # line 102-108 groceries name validation
            groname = str(input('Grocery Name:'))
            if (groname!=''):
                if (groname in list2):  # if new groceries name same with groceries name in list2 will print line 104 and continue looping line101 for enter new groceries name
                    print('This item already in store.')
                    continue
                else:
                    list.append(groname + ',')   # if new groceries name not same with groceries name in list2 will append to list
                    break   # break to continue enter other grocery details
            else:
                print('Please enter groname.')
        while True:  # from Line 109-129 enter amount/weight/price and do validation for each
            try:
                amount = str(int(input('Amount:')))
                break
            except:
                print('please enter a number.')
        list.append(amount + ',')
        while True:
            try:
                weight = str(float(input('Weight (g):')))
                break
            except:
                print('please enter a number.')
        list.append(weight + ',')
        while True:
            try:
                price = str(float(input('Price(RM):')))
                break
            except:
                print('please enter a number.')
        list.append(price)
        while x:
            ask3 = input('Do you still need to enter vegetable grocery detail (Yes/No):').lower()  # ask admin want to continue enter vegetable groceries details or not
            if (ask3 =='yes'):   # if yes : append the details of new groceries to txt file, and continue looping line 93
                for word in list:
                    file = open('vegetable.txt', 'a')        # have four txt file to save groceries details  
                    file.write(word)                            # one: all groceries details txt file  
                file.write('\n')                                   # second/third/fourth : household/meat/vegetable grocery details txt files
                file.close()
                for word in list:
                    file = open('grocerydetail.txt', 'a')
                    file.write(word)
                file.write('\n')
                file.close()
                break
            elif (ask3 == 'no'):  # if no : append the details of new groceries to txt file, and stop loop this function
                for word in list:
                    file = open('vegetable.txt', 'a')
                    file.write(word)
                file.write('\n')
                file.close()
                for word in list:
                    file = open('grocerydetail.txt', 'a')
                    file.write(word)
                file.write('\n')
                file.close()
                x = False
            else:
                print('please enter yes or no.')
                x = True

def meat():
    x = True
    while x:
        list = [] # save all new groceries details in this list
        list2 = [] # save existing groceries details
        file = open('grocerydetail.txt', 'r') # open the file and read the line by line and split the line into each element and append groceries name to list2
        for line in file.readlines(): 
            data = line.split(',') 
            groname = data[0]
            list2.append(groname)
        while x:
            groname = str(input('Grocery Name:')) # Line 171-177 groceries name validation
            if (groname != ''):
                if (groname in list2):  # if new groceries name same with groceries name in list2 will print line 173 and continue loop line170 for enter new groceries name
                    print('this item already in store.')
                    continue
                else:
                    list.append(groname + ',') # if new groceries name not same with groceries name in list2 will append to list
                    break # break to continue enter other grocery details
            else:
                print('Please enter groname.')
        while True: # from Line 179-198 enter amount/weight/price and do validation for each
            try:
                amount = str(int(input('Amount:')))
                break
            except:
                print('please enter a number.')
        list.append(amount + ',')
        while True:
            try:
                weight = str(float(input('Weight (g):')))
                break
            except:
                print('please enter a number.')
        list.append(weight + ',')
        while True:
            try:
                price = str(float(input('Price(RM):')))
                break
            except:
                print('please enter a number.')
        list.append(price)
        while x:
            ask3 = input('Do you still need to enter meat grocery detail (Yes/No):').lower()   # ask admin want to continue enter meat groceries details or not
            if (ask3 ==  'yes'):  # if yes : save the details of new groceries to txt file, and continue loop line162
                for word in list:
                    file = open('meat.txt', 'a')
                    file.write(word)
                file.write('\n')
                file.close()
                for word in list:
                    file = open('grocerydetail.txt', 'a')
                    file.write(word)
                file.write('\n')
                file.close()
                break
            elif (ask3 == 'no'):  # if no : save the details of new groceries to txt file, and stop looping
                for word in list:
                    file = open('meat.txt', 'a')
                    file.write(word)
                file.write('\n')
                file.close()
                for word in list:
                    file = open('grocerydetail.txt', 'a')
                    file.write(word)
                file.write('\n')
                file.close()
                x = False
            else:
                print('Please enter yes or no.')
                x = True

def household():
    x = True
    while x:
        list = [] # save all new groceries detail in this list
        list2 = [] # Save existing groceries details
        file = open('grocerydetail.txt', 'r')  # open the file and read the line by line and split the line into each element and append groceries name to list2
        for line in file.readlines():  
            data = line.split(',')
            groname = data[0]  
            list2.append(groname)
        while x:
            groname = str(input('Grocery Name:')) # Line 241-246 groceries name validation
            if (groname != ''):
                if (groname in list2): # if new groceries name same with groceries name in list2 will print line 243 and continue looping for enter new groceries name
                    print('this item already in store.')
                    continue
                else:
                    list.append(groname + ',') # if new groceries name not same with groceries name in list2 will append to list
                    break # break to continue enter other groceries details
            else:
                print('Please enter groname.')
        while True:  # from Line 247-267 enter amount/weight/price and do validation for each
            try:
                amount = str(int(input('Amount:')))
                break
            except:
                print('please enter a number.')
        list.append(amount + ',')
        while True:
            try:
                weight = str(float(input('Weight (g):')))
                break
            except:
                print('please enter a number.')
        list.append(weight + ',')
        while True:
            try:
                price = str(float(input('Price(RM):')))
                break
            except:
                print('please enter a number.')
        list.append(price)
        while x:
            ask3 = input('Do you still need to enter household grocery detail (Yes/No):').lower() # ask admin want to continue enter groceries details or not
            if (ask3 == 'yes'):  # if yes : save the details of new groceries to txt file, and continue looping
                for word in list:
                    file = open('household.txt', 'a')
                    file.write(word)
                file.write('\n')
                file.close()
                for word in list:
                    file = open('grocerydetail.txt', 'a')
                    file.write(word)
                file.write('\n')
                file.close()
                break
            elif (ask3 ==  'no'):  # if no : save the details of new groceries to txt file, and stop looping
                for word in list:
                    file = open('household.txt', 'a')
                    file.write(word)
                file.write('\n')
                file.close()
                for word in list:
                    file = open('grocerydetail.txt', 'a')
                    file.write(word)
                file.write('\n')
                file.close()
                x = False
            else:
                print('Please enter yes or no.')
                x = True

def searchgro():  # this function for admin search specific groceries details
    x = True
    while x:
        a = True
        print('\n-----------------------------  SEARCH GROCERY PAGE  ------------------------------')
        file = open('grocerydetail.txt', 'r') # open all groceries detail txt file
        search_gro = input('\nEnter the grocery you want to search (press enter to end): ')  # enter groceries' name to search groceries detail
        if (search_gro != ''):
            for data in file.readlines():  # read the line by line and split the line into each element
                data = data.rstrip()
                data = data.split(",")  
                groceryname = str(data[0])      
                amount = str(data[1])             
                weight = str(data[2])                
                price = str(data[3])                    # line313 (search_gro) is enter by admin that what admin need to search 
                if search_gro == groceryname:   # if admin enter groceries name same with the groceries name in the txt file that print the result
                    print('\nGrocery name:' + groceryname + (' ' * (20 - len(groceryname))) + 'Amount:' + amount + (' ' * (10 - len(amount))) + 'Weight (g):' + weight + (' ' * (10 - len(weight))) + 'Price:' + price)
                    a=False   # to stop run line 318
                else:
                    continue
            if a:
                print('Not this item.')  #  if admin enter randomly or the txt file does not have this groceries name will print this line
        else:  # admin press enter to stop looping and exit
            x = False
        file.close()

def deletegrocery():   # for admin delete specific groceries details
    x =a = True
    while x:
        print('\n-----------------------------   VIEW ALL GROCERY DETAILS   ------------------------------')
        file = open ('grocerydetail.txt', 'r')          # Show details of all groceries, so admin knows what that one want to remove
        for line in file.readlines():   # open the file and read the line by line and split the line into each element
            data = line.split(",")
            groceryname = data[0]
            amount = str(data[1])
            weight = str(data[2])
            price = str(data[3])
            print('Grocery name:' + groceryname + (' ' * (20 - len(groceryname))) + 'Amount:' + amount + (' ' * (10 - len(amount))) + 'Weight (g):' + weight + (' ' * (10 - len(weight))) + 'Price:' + price)
        file.close()
        while x:
            print('\n-----------------------------  DELETE GROCERY SYSTEM  ------------------------------')
            ask_delete = str(input('\nWhat you want to delete, please enter grocery name. (If you want to stop pls enter x):'))
            file = open('grocerydetail.txt', 'r')
            if (ask_delete != ' ' and ask_delete != 'x'):  # if  input not equal blank and x (x is mean to stop running this function) then run the code under if
                for data in file.readlines():  # read the line by line and split the line into each element
                    data = data.rstrip()
                    data = data.split(",")
                    groceryname = str(data[0])
                    amount = str(data[1])
                    weight = str(data[2])
                    price = str(data[3])  # line313 (search_gro) is enter by admin that what admin need to search
                    if ask_delete == groceryname:
                        print('\nGrocery name:' + groceryname + (' ' * (20 - len(groceryname))) + 'Amount:' + amount + (' ' * (10 - len(amount))) + 'Weight (g):' + weight + (' ' * (10 - len(weight))) + 'Price:' + price)
                        print('\nThis groceries successful be deleted.')

                        newlist = []    #  open a new list to save all groceries Except the groceries that is to be removed
                        file = open('grocerydetail.txt', 'r')
                        for line in file.readlines():
                            data = line.split(",")
                            groceryname = data[0]
                            if ask_delete != groceryname:  # if groceries name not equal to item want to be remove then append to the newlist (line341)
                                newlist.append(line)
                        file = open('grocerydetail.txt', 'w')  # after looping and append all item in the txt file then read the newlist and write into the txt file
                        for text in newlist:
                            file.write(str(text))   # add string because text is a list cannot be written into txt file
                        file.close()

                        newlist1 = []                                                 # line 353-387 is the same code with line341-351
                        file1 = open('vegetable.txt', 'r')                       # beacause i separate txt file into three category so i need to read and write 3times with different txt files
                        for line in file1.readlines():
                            data = line.split(",")
                            groceryname = data[0]
                            if ask_delete != groceryname:
                                newlist1.append(line)
                        file1 = open('vegetable.txt', 'w')
                        for text in newlist1:
                            file1.write(str(text))
                        file1.close()

                        newlist2 = []
                        file2 = open('meat.txt', 'r')
                        for line in file2.readlines():
                            data = line.split(",")
                            groceryname = data[0]
                            if ask_delete != groceryname:
                                newlist2.append(line)
                        file2 = open('meat.txt', 'w')
                        for text in newlist2:
                            file2.write(str(text))
                        file2.close()

                        newlist3 = []
                        file3 = open('household.txt', 'r')
                        for line in file3.readlines():
                            data = line.split(",")
                            groceryname = data[0]
                            if ask_delete != groceryname:
                                newlist3.append(line)
                        file3 = open('household.txt', 'w')
                        for text in newlist3:
                            file3.write(str(text))
                        file3.close()
                        a=False
                    else:
                        continue
                if a:
                    print('No this item.')
            elif (ask_delete == 'x'):    # if admin enter x is mean to stop running this function
                x = False
            file.close()

def modifygro():
    print('\n-----------------------------   VIEW ALL GROCERY DETAILS   ------------------------------')
    file = open('grocerydetail.txt', 'r')
    for line in file.readlines():  # open the file , read the line by line and split the line into each element
        data = line.split(",")
        groceryname = data[0]
        amount = str(data[1])
        weight = str(data[2])
        price = str(data[3])
        print('Grocery name:' + groceryname + (' ' * (20 - len(groceryname))) + 'Amount:' + amount +
              (' ' * (10 - len(amount))) + 'Weight (g):' + weight + (' ' * (10 - len(weight))) + 'Price:' + price)
    file.close()

    print('\n------------------------------   MODIFY GROCERIES PAGE   -------------------------------\n')
    grolist=[]  # this list save original groceries details
    file=open('grocerydetail.txt','r')    # read the file and append to the list 
    for i in file.readlines():
        grolist.append(i.strip().split(','))
    file.close()

    #start modify groceries
    x=True
    a=True
    while x or a:
        new_list = []  # this list save after modify groceries details
        x=True
        ask_modify=str(input('\nPlease enter the grocery name that need to modify (if you want to stop press enter key):'))
        count=-1 # list starting from 0 so here enter count=-1
        if (ask_modify!=''):
            for i in grolist:
                count = count + 1   # this count lets me know the number of groceries that want to modify
                if ask_modify in i :
                    groname=i[0]
                    amount=i[1]
                    weight=i[2]
                    price=i[3]
                    new_list.append(i)    # if  item need to modify in grolist then display to the admin
                    print('\nGrocery name:' + groname + '\t' + 'Amount:' + str(amount) + '\t' + 'Weight:' + str( weight) + '\t' + 'Price:' + str(price))
                    print('\n--------------------------------------------------------------------------------------')
                    a=False  # to stop running line434
                    break
            if a :   # if  admin enter that item not in grolist (line408) will display line435 and continue while loop (line417)
                print('not this item')
                continue

            while x:  # if admin enter that groceries have in grolist will run this loop
                ask2_modify=str(input('\nWhich part need to modify \nA.Grocery name \nB.Amount \nC.Weight \nD.Price \n:'))
                ask2_modify=ask2_modify.lower()
                if (ask2_modify=='a'):      # modify groceries name
                    while x:
                        print('\n---------------------------------   MODIFY GROCERIES NAME   ---------------------------------')
                        groname_modify=str(input('New Grocery Name:'))
                        if (groname_modify!='' ):   # line 449-456 valid new groceries name
                            list = []
                            file = open('grocerydetail.txt', 'r')   # read all groceries name from txt file and append to list (line447) 
                            for line in file.readlines():
                                data = line.split(',')
                                groname = data[0]
                                list.append(groname)
                            file.close()
                            if groname_modify in list:  # if modify groceries name same as existing groceries name will display this line
                                print('this item name already been used')
                                continue
                            else:
                                new_list[0][0] = groname_modify  # in new_list first line first element (groceries name) == groname_modify (new groceries name)
                                grolist[count] = new_list[0]          # count the modify groceries in grolist which line then replace it 
                                print('\n-------------------------------  AFTER MODIFY GROCERIES NAME   -------------------------------')
                                for i in new_list:      # print the result after modify
                                    groname = i[0]
                                    amount = i[1]
                                    weight = i[2]
                                    price = i[3]
                                    print('Grocery name:' + groname + (' ' * (20 - len(groname))) + 'Amount:' + amount +(' ' * (10 - len(amount))) + 'Weight (g):' + weight + (' ' * (10 - len(weight))) + 'Price:' + price)

                                file=open('grocerydetail.txt','w')      # write all groceries to txt file from grolist
                                for line in grolist:
                                    for line2 in line:
                                        file.writelines(str(line2).strip())
                                        file.write(',')
                                    file.write('\n')
                                file.close()

                                list2=[]                                                # line476-490 is solve a problem then after modify txt file at the end every that will keep adding commas,
                                file = open('grocerydetail.txt', 'r')           # like modify one time have one comma, modify second times become to two commas,
                                for line in file.readlines():                    # so i read the txt file put in the element that i want into list2 and write into txt file
                                    data=line.split(',')  # read the line by line and split the line into each element
                                    groname=data[0]
                                    amount=data[1]
                                    weight=data[2]
                                    price=data[3]
                                    list2.append(groname+','+amount+','+weight+','+price+'\n')
                                file.close()

                                file=open('grocerydetail.txt','w')
                                for i in list2:
                                    file.write(i)
                                file.close()

                                while x:
                                    ask_continue = str(input('\nDo you want to modify other grocery (Yes/No):')).lower()
                                    if (ask_continue == 'yes'):   
                                        a = True    # continue line 417 while loop
                                        x = False   # to stop all (while x: ) loop but a=True so can continue looping
                                    elif (ask_continue == 'no'):
                                        x = False   # stop all looping and stop the function
                                        a = False
                                    else:
                                        print('Please enter Yes or No')

                        else:
                            print('please enter a grocery name .')
                            continue

                elif(ask2_modify=='b'):  # modify groceries amount
                    x = True

                    print('\n---------------------------------   MODIFY GROCERIES AMOUNT   ---------------------------------')
                    while x:
                        try:
                            amount_modify = int(input('New Amount:'))   # using try/except method to do amount validation
                            break
                        except:
                            print('Please enter number')
                            continue

                    new_list[0][1] = amount_modify  # in new_list first line second element (amount) == amount_modify (new amount)
                    grolist[count] = new_list[0]        # count the modify groceries in grolist which line then replace it

                    print('\n-------------------------------  AFTER MODIFY GROCERIES AMOUNT   -------------------------------')
                    for i in new_list:              # write all groceries to txt file from grolist
                        groname = i[0]
                        amount = i[1]
                        weight = i[2]
                        price = i[3]
                        print('\nGrocery name:' + groname + '\t' + 'Amount:' + str(amount) + '\t' + 'Weight:' + str(weight) + '\t' + 'Price:' + str(price))

                    file = open('grocerydetail.txt', 'w')        # write all groceries to txt file from grolist
                    for line in grolist:
                        for line2 in line:
                            file.writelines(str(line2).strip())
                            file.write(',')
                        file.write('\n')
                    file.close()

                    list = []
                    file = open('grocerydetail.txt', 'r')          # line538-552 is solve a problem then after modify txt file at the end every that will keep adding commas,
                    for line in file.readlines():                    # like modify one time have one comma, modify second times become to two commas,
                        data = line.split(',')                          # so i read the txt file put in the element that i want into list and write into txt file
                        groname = data[0]
                        amount = data[1]
                        weight = data[2]
                        price = data[3]
                        list.append(groname + ',' + amount + ',' + weight + ',' + price.strip() + '\n')
                    file.close()

                    file = open('grocerydetail.txt', 'w')
                    for i in list:
                        file.write(i)
                    file.close()

                    while x:
                        ask_continue = str(input('\nDo you want to modify other grocery (Yes/No):'))
                        ask_continue = ask_continue.lower()
                        if (ask_continue == 'yes'):
                            a = True        # continue line 417 while loop
                            x = False       # to stop all (while x: ) loop but (a=True) so can continue looping LINE 417
                        elif (ask_continue == 'no'):
                            x = False       # stop all looping and stop the function
                            a = False
                        else:
                            print('Please enter Yes or No')


                elif (ask2_modify == 'c'):      # modify groceries weight
                    x = True

                    print('\n---------------------------------   MODIFY GROCERIES WEIGHT   ---------------------------------')
                    while x:
                        try:            # using try/except method to do weight validation
                            weight_modify = float(input('New Weight:'))
                            break
                        except:
                            print('Please enter number')
                            continue

                    new_list[0][2] = weight_modify      # in new_list first line third element (weight) == weight_modify (new weight)
                    grolist[count] = new_list[0]            # count the modify groceries in grolist which line then replace it
                    print('\n-------------------------------  AFTER MODIFY GROCERIES WEIGHT   -------------------------------')
                    for i in new_list:      # print groceries details after modify
                        groname = i[0]
                        amount = i[1]
                        weight = i[2]
                        price = i[3]
                        print('\nGrocery name:' + groname + '\t' + 'Amount:' + str(amount) + '\t' + 'Weight:' + str(weight) + '\t' + 'Price:' + str(price))
                    file = open('grocerydetail.txt', 'w')           # write all groceries to txt file from grolist
                    for line in grolist:
                        for line2 in line:
                            file.writelines(str(line2).strip())
                            file.write(',')
                        file.write('\n')
                    file.close()

                    list = []                                                # line596-610 is solve a problem then after modify txt file at the end every that will keep adding commas,
                    file = open('grocerydetail.txt', 'r')           # like modify one time have one comma, modify second times become to two commas,
                    for line in file.readlines():                     # so i read the txt file put in the element that i want into list and write into txt file
                        data = line.split(',')   # read the line by line and split the line into each element
                        groname = data[0]
                        amount = data[1]
                        weight = data[2]
                        price = data[3]
                        list.append(groname + ',' + amount + ',' + weight + ',' + price.strip() + '\n')
                    file.close()

                    file = open('grocerydetail.txt', 'w')
                    for i in list:
                        file.write(i)
                    file.close()

                    while x:
                        ask_continue = str(input('\nDo you want to modify other grocery (Yes/No):'))
                        ask_continue = ask_continue.lower()
                        if (ask_continue == 'yes'):
                            a = True        # continue line 417 while loop
                            x = False       # to stop all (while x: ) loop but (a=True) so can continue looping LINE 417
                        elif (ask_continue == 'no'):
                            x = False       # stop all looping and stop the function
                            a = False
                        else:
                            print('Please enter Yes or No')


                elif (ask2_modify == 'd'):
                    x = True

                    print('\n---------------------------------   MODIFY GROCERIES PRICE   ---------------------------------')
                    while x:
                        try:        # using try/except method to do price validation
                            price_modify = float(input('New Price:'))
                            break
                        except:
                            print('Please enter number')
                            continue

                    new_list[0][3] = price_modify       # in new_list first line fourth element (price) == price_modify (new price)
                    grolist[count] = new_list[0]           # count the modify groceries in grolist which line then replace it
                    print( '\n-------------------------------  AFTER MODIFY GROCERIES PRICE   -------------------------------')
                    for i in new_list:      # print groceries details after modify
                        groname = i[0]
                        amount = i[1]
                        weight = i[2]
                        price = i[3]
                        print('\nGrocery name:' + groname + '\t' + 'Amount:' + str(amount) + '\t' + 'Weight:' + str(weight) + '\t' + 'Price:' + str(price))

                    file = open('grocerydetail.txt', 'w')       # write all groceries to txt file from grolist
                    for line in grolist:
                        for line2 in line:
                            file.writelines(str(line2).strip())
                            file.write(',')
                        file.write('\n')
                    file.close()

                    list = []                                           # line655-669 is solve a problem then after modify txt file at the end every that will keep adding commas,
                    file = open('grocerydetail.txt', 'r')      # like modify one time have one comma, modify second times become to two commas,
                    for line in file.readlines():                # so i read the txt file put in the element that i want into list and write into txt file.
                        data = line.split(',')  # read the line by line and split the line into each element
                        groname = data[0]
                        amount = data[1]
                        weight = data[2]
                        price = data[3]
                        list.append(groname + ',' + amount + ',' + weight + ',' + price.strip() + '\n')
                    file.close()

                    file = open('grocerydetail.txt', 'w')
                    for i in list:
                        file.write(i)
                    file.close()

                    while x:
                            ask_continue=str(input('\nDo you want to modify other grocery (Yes/No):')).lower()
                            if (ask_continue=='yes'):
                                a=True      # continue line 417 while loop
                                x = False   # to stop all (while x: ) loop but (a=True) so can continue looping LINE 417
                            elif(ask_continue=='no'):
                                x=False     # stop all looping and stop the function
                                a=False
                            else:
                                print('Please enter Yes or No')

                else:
                    print('Please enter A B C D')
                    continue
        elif(ask_modify==''):  # press enter key to stop modify function
            x=False
            a=False

def admin_view_customer_order():        # admin view all customer order 
    print('\n-----------------------------------   VIEW ALL CUSTOMER ORDER   ------------------------------------\n')
    file = open('ordergrocery.txt', 'r')    # open customer order files and read
    for data in file:   # read the line by line and split the line into each element 
        data = data.split(",")               
        username = str(data[0]) 
        groceryname = str(data[1])
        weight = str(data[2])
        price = str(data[3])
        orderamount = str(data[4])          # print out all the order
        print( 'UserName:' + username + (' '*(15-len(username))) + 'Grocery name:' + groceryname + (' '*(20-len(groceryname))) +
               'Weight:' + weight + (' '*(10-len(weight))) +'Price:' + price + (' '*(10-len(price))) + 'OrderAmount:' + orderamount )
    file.close()

def admin_view_specify_customer_order():  # admin search customer order
    print('\n----------------------------   VIEW SPECIFIC CUSTOMER ORDER   -----------------------------\n')
    x = True
    a = True
    while x:
        list = []  # this list to save the name of the customer on the order
        file = open('ordergrocery.txt', 'r')        # open customer order txt file and read 
        for data in file:                # read the line by line and split the line into each element 
            data = data.split(",")   
            userid = str(data[0])  # set first element is user id
            list.append(userid)                 # append all the user id from the order file to list
        list = set(list)  # using set to delete duplicates name
        print('\nThe name of the customer order :')
        print(list)      # print all the names in the list to let the admin know which customers can be searched
        file.close()
        
        ask_search_cus = str(input('\nWhich customer‘s order do you want to search, please enter custorm name:'))    # enter customer name to search customer's order
        file = open('ordergrocery.txt', 'r')    # open customer order files and read
        if ask_search_cus in list:      # if admin enter customer's name have in list (line708) then run the code
            print('\n---------------------------------------   This is ' + ask_search_cus + '‘s order   ---------------------------------------')
            for line in file:                   # read the line by line and split the line into each element 
                data = line.split(",")
                username = str(data[0])
                groceryname = str(data[1])
                weight = str(data[2])
                price = str(data[3])
                orderamount = str(data[4])
                if ask_search_cus == username:      # if admin enter customer name equal to the name in the customer order file then print the order
                    print('UserName:' + username + (' ' * (15 - len(username))) + 'Grocery name:' + groceryname + (' ' * (20 - len(groceryname))) + 'Weight:' + weight + (' ' * (10 - len(weight))) +
                        'Price:' + price + (' ' * (10 - len(price))) + 'OrderAmount:' + orderamount)
                else:
                    continue
        else:      # if admin enter customer's name not have in list (line708) then print Line 736
            print(ask_search_cus+' no purchase anything.')
        file.close()
        
        while x:
            ask = str(input('\nDo you want to continue for search customer order (Yes/NO):')).lower()       #ask admin want continue search customer order or not
            if (ask == 'yes'):      # if yes break the line739 while loop and continue line707 while loop
                break       
            elif (ask == 'no'):     # if no stop all looping
                x = False
            else:
                print('Please enter Yes or No.')
                continue

def admin():
    while True:
        while True:
            try:        # ask admin want to view groceries/update groceries/modify groceries/delete groceries/search (groceries/customer order) and exit
                print('\n-----------------------------------   ADMIN PAGE  ----------------------------------')
                ask3 = int(input('Do you want \n1.View all groceries \n2.Update groceries \n3.Modify groceries \n4.Delete groceries \n5.Search groceries'
                                 '\n6.View all customer orders \n7.Search specify customer order \n8.Exit \n:'))
                break
            except:
                print('Please enter a number from 1 to 7')
        if (ask3 == 1):      # view all groceries details
            viewgro()         # call viewgro function
        elif (ask3 == 2):   # update groceries 
            x = True
            while x:
                while True:
                    try:    
                        print('\n-----------------------   UPDATE GROCERIES PAGE   ----------------------')
                        ask1 = int(input('Which categories grocery you want to update: \n1. Household \n2. Meat \n3. Vegetable \n:'))   # ask which category groceries want to update
                        break
                    except:
                        print('Please enter a number from 1 to 3.')
                if (ask1 == 1):     # update household groceries details
                    print('\n----------------   UPDATE HOUSEHOLD GROCERIES DETAILS   -----------------')
                    household()     # call household function
                    while x:
                        ask2 = str(input('\nDo you need to update other categories of groceries (Yes/No) \n: ')).lower()  # ask want continue update other categories groceries
                        if (ask2 == 'yes'):   # if yes continue line763 while loop
                            break  
                        elif (ask2 == 'no'):
                            x = False           # if no stop line 763 while loop and continue line750 while loop
                        else:
                            print('Please enter Yes or No')
                            continue
                elif (ask1 == 2):   # update meat groceries details
                    print('\n------------------   UPDATE MEAT GROCERIES DETAILS   -------------------')
                    meat()  # call meat function
                    while x:
                        ask2 = str(input('\nDo you need to update other categories of groceries (Yes/No) \n: ')).lower()  # ask want continue update other categories groceries
                        if (ask2 == 'yes'):     # if yes continue line763 while loop
                            break
                        elif (ask2 == 'no'):    # if no stop line 763 while loop and continue line750 while loop
                            x = False
                        else:
                            print('Please enter Yes or No')
                            continue
                elif (ask1 == 3):   # update vegetable groceries details
                    print('\n----------------   UPDATE VEGETABLE GROCERIES DETAILS   -----------------')
                    vegetable()     # call vegetable function
                    while x:
                        ask2 = str(input('\nDo you need to update other categories of groceries (Yes/No) \n: ')).lower()    # ask want continue update other categories groceries
                        if (ask2 == 'yes'):      # if yes continue line763 while loop
                            break
                        elif (ask2 == 'no'):     # if no stop line 763 while loop and continue line750 while loop
                            x = False
                        else:
                            print('Please enter Yes or No')
                            continue
                else:
                    print('Please enter a number from 1 to 3.')
                    continue
        elif (ask3 == 3):# modify groceries
            modifygro()# call function
        elif (ask3 == 4):# delete groceries 
            deletegrocery()# call function
        elif (ask3 == 5):# serach groceries details
            searchgro()# call function
        elif (ask3 == 6):# view all customer order
            admin_view_customer_order()# call function
        elif (ask3 == 7):# seaerch customer order 
            admin_view_specify_customer_order()# call function
        elif (ask3 == 8):# exit
            break# stop looping
        else:
            print('Please enter a number from 1 to 7')

def adminlogin():
    x = True
    while x:
        file = open('adminlogin.txt', 'w')              # write admin password and id 
        file.write('admin' + ',' + 'admin1234')
        file.close()
        print('\n-----------------------------  ADMIN LOGIN PAGE   ----------------------------')
        ask1 = str(input('\nPlease enter Admin ID:'))          # admin input
        ask2 = str(input('Please enter Admin password:'))
        right = False
        file = open('adminlogin.txt', 'r')  # open admin login txt file
        for data in file:
            a, b = data.split(",")   # read the line by line and split the line into each element 
            if (ask1 == a) and (ask2 == b): # if enter password and id same with the txt file (right = True) and print line843 
                right = True                        # if  enter password and id NOT same with the txt file (right = Flase) and print line847
                break
        file.close()
        if right:
            print('\nSuccessfully Login') 
            admin()     # if successful login will call admin function
            break
        else:
            print('You are enter Wrongly, Please re enter')
            continue

####################################################################

def userlogin():
    print('\n-----------------------------  CUSTOMER LOGIN PAGE   ----------------------------')
    a=True
    x = True
    while x:
        ask1 = str(input('Please enter user ID :'))     # customer input ID and password
        ask2 = str(input('Please enter user password :'))
        ask2=ask2+'\n'  # here add \n because in txt files after enter password have \n, so in python \n also is a string
        file = open('loginInformation.txt', 'r')  # open the file where the customer's password and id are stored
        for line in file.readlines():
            data=line.split(",")  # read the line by line and split the line into each element 
            id=data[0]
            password=data[1]
            if ask1==id and ask2==password:
                print('\nSuccessful Login!!!')
                a=False # stop run line 872
                x=False  # to break the while loop
                break   # to break the for loop
            else:
                continue
        if a:   # if customer enter ID and password not same with the txt file will print this line873 and continue to re-enter 
            print('Please enter a valid ID and Password.\n')
            continue # continue while loop(line856)

def ordergro():     # customer order groceries function
    big_order_list = []
    print('\n----------------------------   VIEW ALL GROCERY DETAILS   ------------------------------')
    file = open('grocerydetail.txt',
                'r')  # line879-887 open file, read line by line and split the line into each element and print groceries details
    for line in file.readlines():
        data = line.split(",")
        groceryname = data[0]
        amount = str(data[1])
        weight = str(data[2])
        price = str(data[3])
        print('Grocery name:' + groceryname + (' ' * (20 - len(groceryname))) + 'Amount:' + amount + (
                    ' ' * (10 - len(amount))) + 'Weight (g):' + weight + (' ' * (10 - len(weight))) + 'Price:' + price)
    file.close()
    print('---------------------------------------------------------------------------------------------')

    x = True
    a = True
    totalcost = 0
    while x:
        username = str(input('Enter User ID:'))  # user enter user ID
        file = open('loginInformation.txt', 'r')  # open file , read line by line in the file and split the line
        for line in file.readlines():
            data = line.split(",")
            a = data[0]
            if username == a:  # if user enter ID same with the element a will stop while loop(line893) and start order (line907)
                a = False         # stop running line903
                x = False        # to stop the while first while loop
                break            # to break the for loop
        if a:                    # if user enter ID not in the file will display this line904
            print('Please enter a valid user name.')
            continue

    # start order system
    x = True
    while x:
        a=True
        print('\n---------------------------------------      ORDER    PAGE     ---------------------------------------')
        order_gro = str(input('\nWhat you want to order, Enter grocery name \n(if you want to end order page pls enter x):')).lower().strip()
        file = open('grocerydetail.txt', 'r')  # open file
        if (order_gro != ''):
            for line in file.readlines():  # read line by line in the file and split the line
                line.strip()
                data = line.split(",")
                groceryname = data[0]
                amount = str(data[1])
                weight = str(data[2])
                price = str(data[3])
                amount = int(amount)
                orderamount = 0
                if order_gro == groceryname:  # if enter groceries name have in groceries details file will run this code
                    a = False # stop run  line 1044
                    while x:
                        try:                                                                                                       # using try/except do validation
                            order_gro_amount = int(input('How many do you want to purchase:'))  # ask customers how many they want to buy
                        except:     # if the customer does not enter a number, line 931 will be printed and the customer will be asked to enter it again.
                            print('Please enter a number.')
                            continue
                        if (order_gro_amount <= amount):  # if the number of purchases does not exceed the number in the store
                            orderamount = orderamount + order_gro_amount  # customer order amount plus one
                            break                                                                 # break line928 while loop
                        elif (order_gro_amount > amount):  # if the number of purchases exceed the number in the store will print line937
                            print('Sorry, You have purchased more than the stored quantity，please re enter again, thank you.\n')
                            continue
                    saveorder = (username + ',' + groceryname + ',' + weight + ',' + price.strip() + ',' + str(orderamount))
                    big_order_list.append(str(saveorder))
                    totalcost = totalcost + (order_gro_amount * float(price))   # caculate total price
                    # three category groceries files + one all groceries file amount decrease
                    # line945-line961 / line963-979 / line981-997 / line99-1015 : open files and read line by line in the file , split the line into different element.
                    # If order groceries name same with the groceries name in the files , deccrease the number of that groceries and append all detail to the list,
                    # after decreasing the number of groceries open files, read the list one by one and write new groceries details to the files.
                    list = []
                    file = open('grocerydetail.txt', 'r')
                    for line in file.readlines():
                        data = line.split(",")
                        groceryname = data[0]
                        amount = data[1]
                        weight = data[2]
                        price = data[3]
                        amount = int(amount)
                        if order_gro == groceryname:
                            amount = amount - order_gro_amount
                            amount = str(amount)
                        list.append(groceryname + ',' + str(amount) + ',' + str(weight) + ',' + str(price))
                    file = open('grocerydetail.txt', 'w')
                    for line in list:
                        file.write(str(line))
                    file.close()

                    list1 = []
                    file1 = open('vegetable.txt', 'r')
                    for line in file1.readlines():
                        data = line.split(",")
                        groceryname = data[0]
                        amount = data[1]
                        weight = data[2]
                        price = data[3]
                        amount = int(amount)
                        if order_gro == groceryname:
                            amount = amount - order_gro_amount
                            amount = str(amount)
                        list1.append(groceryname + ',' + str(amount) + ',' + str(weight) + ',' + str(price))
                    file = open('vegetable.txt', 'w')
                    for line in list1:
                        file.write(str(line))
                    file.close()

                    file2 = open('meat.txt', 'r')
                    list2 = []
                    for line in file2.readlines():
                        data = line.split(",")
                        groceryname = data[0]
                        amount = data[1]
                        weight = data[2]
                        price = data[3]
                        amount = int(amount)
                        if order_gro == groceryname:
                            amount = amount - order_gro_amount
                            amount = str(amount)
                        list2.append(groceryname + ',' + str(amount) + ',' + str(weight) + ',' + str(price))
                    file = open('meat.txt', 'w')
                    for line in list2:
                        file.write(str(line))
                    file.close()

                    file3 = open('household.txt', 'r')
                    list3 = []
                    for line in file3.readlines():
                        data = line.split(",")
                        groceryname = data[0]
                        amount = data[1]
                        weight = data[2]
                        price = data[3]
                        amount = int(amount)
                        if order_gro == groceryname:
                            amount = amount - order_gro_amount
                            amount = str(amount)
                        list3.append(groceryname + ',' + str(amount) + ',' + str(weight) + ',' + str(price))
                    file = open('household.txt', 'w')
                    for line in list3:
                        file.write(str(line))
                    file.close()

                    while x:     #  ask customer want continue order other grocery or not
                        ask1 = str(input('\nDo you want to continue(Yes/NO):')).lower()
                        if (ask1 == 'yes'):  # if yes continue while loop line 912
                            break
                        elif (ask1 == 'no'):  # if no : read the order list (big_order_list) line877 one by one and append to customer order groceries file
                            for word in big_order_list:
                                for word2 in word:
                                    file = open('ordergrocery.txt', 'a')
                                    file.write(str(word2))
                                file.write('\n')
                            file.close()
                            x = False
                        else:
                            print('please enter yes or no')
                            continue
                elif (order_gro == 'x'):    # end the order function and read the order list (big_order_list) line877 one by one and append to customer order groceries file
                    for word in big_order_list:
                        for word2 in word:
                            file = open('ordergrocery.txt', 'a')
                            file.write(word2)
                        file.write('\n')
                    file.close()
                    a = False    # stop run line 1044
                    x = False
                    break       # break the for loop line917
            if a:   # if the customer enters a groceries name that is not the same as the groceries name in the grocery file will  print 'not this item'
                print('\n>>>  Not this item so Sorry T-T  <<<')
        else:
            print('\n>>>  Please enter a grocery name  <<<')    # if customer no enter anything in line 914 will print this line
        file.close()
    print('\nYour Order Total Price: RM' + str(totalcost))  # print total price

def view_order_payment():       # customer view owm order and do payment function
    a=True
    x = True
    while x:
        #save all customer ID to list
        login_name_list=[]
        username = str(input('\nEnter User Name to login the system:'))
        file = open('loginInformation.txt', 'r')
        for line in file.readlines():
            data = line.split(",")
            a_userid = data[0]
            login_name_list.append(a_userid)
        file.close()

        totalcost = 0
        print('\n--------------------------------------   This is yours order   ---------------------------------------\n')
        file = open('ordergrocery.txt', 'r')        # open save customer order file and read line by line
        for line in file.readlines():
            data = line.split(",")
            order_cus = str(data[0])
            groceryname = str(data[1])
            weight = str(data[2])
            price = float(data[3])
            orderamount = float(data[4])
            if username in login_name_list and username==order_cus:  # check which line is customer's order , calculate total price and display
                a=False     # stop run line1082
                totalcost = totalcost+(orderamount*price)
                print('UserName:' + username + (' ' * (15 - len(username))) + 'Grocery name:' + groceryname +
                      ( ' ' * (20 - len(groceryname))) + 'Weight (g):' + weight + (' ' * (10 - len(weight))) +'Price:' + str(price) + (' ' * (10 - len(str(price)))) + 'OrderAmount:' + str(orderamount))
            else:
                continue
        if a:  # if enter a user id have/have not in login list(line1056) and don't order anything will print this line and stop this function
            print(username+', You don‘t have buy anything.')
            x=False
            break
        file.close()
        x=True
        while x:     # after customer view owm order will ask to do payment
            ask_payment=str(input('\nDo you want doing payment now (Yes/No) :')).lower()
            if (ask_payment=='yes'):
                print('\n--------------------------------------   PAYMENT SYSTEM PAGE  ---------------------------------------\n')
                print('This is your Total Price: RM'+str(totalcost))
                while x:
                    while x:
                        try:
                            payment = int(input('\nPlease do the payment with enter HAHA BANK card number (4 numbers):'))
                            break
                        except:
                            print('Please re enter HAHA BANK card number.')
                            continue
                    payment = len(str(payment))
                    if (int(payment) == 4):     # if customer enter 4 number print 'successful' 
                        print('Successful payment , Thank you for your buying.')
                        x=False
                        break
                    else:       # if customer enter a number less then 1000 will  need to re enter again 
                        print('please enter 4 numbers.')
                        continue  # continue line1093 while loop
            elif(ask_payment=='no'):    # if customer no want to do payment print 'wish you have a nice day and stop this function
                print('Wish you have a nice day 😉 ')
                x=False
            else:
                print('Please enter Yes or No')
                continue


def view_personal_information():    # customer view owm information
    x = True
    a=True
    while x:
        print('\n----------------------------   VIEW PERSONAL INFORMATION   ------------------------------\n')
        enter_user_id = str(input('Please enter user ID to view your profile:'))    # enter user id
        print('\n--------------------------' + enter_user_id + ' Personal Information-----------------------------\n')
        file = open('customerinformation.txt', 'r')  # open file read line by line, and split the line
        for line in file.readlines():
            data = line.split("\t")
            user_id=data[6]
            if ('Id:'+enter_user_id)==user_id: # if  customer enter user id same with customer information file then print that line
                print(line)
                a=False     # stop run line 1135
                x=False
            else:
                continue

        if a:  # this line will be print if user enter id not in the save custormer information file and It means he/she is not yet registered as a user
            print('Without your personal information please go to register first. \n')
            break

def registercus(): # Existing/Already registered users function
    userlogin() # need to login first before  go to the customer page
    x=True
    while x :
        print('\n---------------------------------   CUSTOMER PAGE  ---------------------------------')
        ask1 = str(input('\nDo you want to \n1.View grocery detail \n2.Order grocery \n3.View order & Doing payment \n4.View Personal Information \n5.Exit\n:'))
        if (ask1 == '1'):  # 1 is view grocery detail and call view groceries function
            viewgro()
        elif (ask1=='2'):   # 2 is order groceries and call order groceries function
            ordergro()
        elif (ask1=='3'):   # 3 is view order and do payment  
            view_order_payment()    # call function
        elif (ask1=='4'):   #4 is view personal information
            view_personal_information() # call function
        elif (ask1=='5'): # 5 is exit
            x=False
        else:
            print('please enter a number from 1 to 5')

########################################################################

def newcustomer():
    x=True
    while x :
        print('\n------------------------------   NEW CUSTOMER PAGE  -----------------------------')
        ask = str(input('\nDo you want: \nA.View groceries Details \nB.Registeration \nC.Exit \n:')).upper()
        if (ask == 'A'): # view groceries details
            viewgro()   # call function
        elif(ask=='B'): # new customer registeration
            informcus=[]    # save all information of customer input
            print('\n------------------------------   Register Page 1   ------------------------------')
            while True:
                name = str(input('Name:'))
                if (name==' '): # name cannot be blank
                    continue
                else:
                    break
            informcus.append('Name:'+name)

            while True:
                gender = str(input('Gender(Female/Male):')).lower()     # input customer gender 
                if (gender=='female'):  
                    break
                elif (gender=='male'):
                    break
                else:
                    print('Please enter (Female/Male)')
                    continue
            informcus.append('Gender:' + gender)    # append to list call (informcus)

            x = True
            while x:    # line 1192-1204 is year validation
                print('Date of Birth')
                while x:
                    while x:
                        try:
                            year = int(input('Year:'))
                            break
                        except:
                            print('Please enter the year you birth')
                            continue
                    if (year <= 2022) and (year >= 1922): # the year cannot small then 1922 and cannot more than 2022
                        break
                    else:
                        print('please enter a year between 1922-2022')
                        continue  # continue while loop (line1192)
                while x:
                    monthlist = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                    month = str(input('Month (Exp:January):')).capitalize()     #  user enters a month, which must be in the month list (line 1206)
                    if (month in monthlist):
                        x = False
                        break
                    else:
                        print('Please enter a month.')
                        continue
                while True:
                    date = int(input('Date:'))      # the user must enter a number in the range of the day of the month
                    if (month == 'January' and date >= 1 and date <= 31):
                        break
                    elif (month == 'February' and date >= 1 and date <= 28):
                        break
                    elif (month == 'March' and date >= 1 and date <= 31):
                        break
                    elif (month == 'April' and date >= 1 and date <= 30):
                        break
                    elif (month == 'May' and date >= 1 and date <= 31):
                        break
                    elif (month == 'June' and date >= 1 and date <= 30):
                        break
                    elif (month == 'July' and date >= 1 and date <= 31):
                        break
                    elif (month == 'August' and date >= 1 and date <= 31):
                        break
                    elif (month == 'September' and date >= 1 and date <= 30):
                        break
                    elif (month == 'October' and date >= 1 and date <= 31):
                        break
                    elif (month == 'November' and date >= 1 and date <= 30):
                        break
                    elif (month == 'December' and date >= 1 and date <= 30):
                        break
                    else:   # If the number of days entered by the user is outside or not in the range of the month will display this line
                        print('This number is out of range of  ' + str(month))
                        continue
            informcus.append('Date of birth:'+str(date)+'/'+str(month)+'/'+str(year))   # append to list call (informcus)

            number = str(input('Contact Number:'))  # enter phone number 
            informcus.append('Cantact Number:' + number)

            email = str(input('Email :'))                   # enter Email
            informcus.append('Email Address:' + email)

            address = str(input('Address:'))            # enter address 
            informcus.append('Address:' + address)
            print('\n------------------------------   Register Page 2   ------------------------------')
            print('Set a ID & Login Password')
            while True:     # line 1255-1268 : id validation
                idlist = []
                file = open('loginInformation.txt', 'r')  # open file read all user id and append to id list(line1256)
                for id in file.readlines():
                    data = id.split(',')
                    userid = str(data[0])
                    idlist.append(userid)
                Id = str(input('User ID: '))
                if (Id in idlist):      # if user id same with other people id will be asked to re-enter
                    print('Your id name has already been used by someone, please enter it differently.')
                    continue
                else:   ## if user id NOT same with other people id will append to id list
                    informcus.append('Id:' + Id)
                    break
            file.close()
            x=True
            while x:
                Password = str(input('Please enter 8 character password: '))  # password must have 8 character
                PassC = len(Password)
                if (PassC < 8 or PassC > 8): # check password has fulfilled the requirements if no re enter again
                    print('Please reset your password')
                    continue
                else:
                    ConPassword = str(input('Please conform your password: '))  # if password has fulfilled the requirements let user enter again the password to conform their password
                    if (ConPassword == Password): # if the password entered 2 times is the same, the registration is successful and this function is ended
                        print('\nSuccessful register !')
                        informcus.append('Password:' + ConPassword)
                        file = open('loginInformation.txt', 'a')
                        file.write(Id + ',' + ConPassword )
                        file.write('\n')
                        file.close()
                        for data in informcus:
                            file = open('customerinformation.txt', 'a')
                            file.write(data)
                            file.write('\t')
                        file.write('\n')
                        file.close()
                        break # stop looping line 1272 and continue looping line 1162
                    else:
                        continue
        elif(ask=='C'): # enter c is want to exit 
            break
        else:
            print('Please enter A/B/C')
            continue

#########################         main system              ##############################

while True:
    print('\n----------------   Welcome to FreshCo Sdn Bhd Grocery Online Shop   ---------------')
    print('May ask if you are ?')
    ask=input('A.Admin \nB.New Customer \nC.Existing Customer\nD.Exit\n:').upper().strip()
    if (ask=='A'):
        adminlogin()
    elif (ask=='B'):
        newcustomer()
    elif (ask=='C'):
        registercus()
    elif (ask=='D'):
        break
    else:
        print('Please Enter A/B/C/D , Thank You ^ ^')
