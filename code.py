import os
# importing the os as we are going to use in some functions
def main():
        User_Name = 'menu'
        Password= 4321
        # setting a password ane a username
        User_Name = input('Type your username:')
        Password = input('Type your password:')
        # if the user entered them wrong he/she will enter a loop until the enter it correctly
        while User_Name!='menu' and Password!=4321:
            print('you have entered the wrong password or username')
            User_Name = input('enter the username please to open the menu:')
            Password = input('enter the password please to open the menu:')
        F_Name=input('Which file do you want to open?')
        # Get the number of dish records to create.
        print()
        print('-----------------------------------')
        print('Here is the contents please choose a letter.')
        print('A-store\n' +
          'B_Display all the items \n' +
          'C-Edit one iteam quantity \n' +
          'D-Delate an iteam \n' +
          'E-Add an iteam \n' +
          'F-Sort items ascending\n')
        print('-------------------------------------')
        print()
        Again= 'y'
        while Again == 'y' or Again == 'Y':
            Choose_num = input('Enter a letter from the list')
            if Choose_num=='A':
                Store(F_Name)
            elif Choose_num =='B':
                 Display(F_Name)
            elif Choose_num =='C':
                Edit(F_Name)
            elif Choose_num =='D':
                Delete(F_Name)
            elif Choose_num =='E':
                Add(F_Name)
            elif Choose_num =='F':
                sort(F_Name)

            else:
                  print('You have to enter a letter between "A-F" to keep working .. ')
            Again = input('Enter "y" to resume, Or "N" to stop the program:')


def Store(F_Name):
    # Get the number of dish records to create.
    num_dishes = int(input('How many dishes do you want to create?'))
    # Open a file for writing.
    dish_file = open(F_Name, 'w')
    # Get each dish's data and write it to the file
    for count in range(1, num_dishes + 1):
        # Get the data for a dish.
        print('Enter data for dish #', count, sep='')
        name = input('Name: ')
        price = input('Price: ')
        calories = input('Calories: ')
        # Write the data as a record to the file.
        dish_file.write(name + '\n')
        dish_file.write(price + '\n')
        dish_file.write(calories + '\n')
        # Display a blank line.
        print()
    # Close the file.
    dish_file.close()
    print('Dish records written to dish.txt.')

def Display(F_Name):
    dish_file = open(F_Name, 'r')
    name = dish_file.readline()
    while name != '':
        # name=dish_file.readline()
        price = dish_file.readline()
        Calories = dish_file.readline()
        name = name.rstrip('\n')
        price = price.rstrip('\n')
        Calories = Calories.rstrip('\n')
        print('name', name)
        print('price', price)
        print('Calories', Calories)
        print()
        name = dish_file.readline()
    dish_file.close()


def Edit(F_Name):
    import os
    # Needed for the remove and rename functions
    # Create a bool variable to use as a flag.
    found = False
    # Get the search value and the new quantity.
    search = input('Enter a description to search for: ')
    new_name = input('Enter a new name instead of the old one : ')
    dish_file = open(F_Name, 'r')
    temp_file = open('temp.txt', 'w')
    descr = dish_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        name = dish_file.readline()
        # Strip the \n from the description.
        descr = descr.rstrip('\n')
        # Write either this record to the temporary file,
        # or the new record if this is the one that is
        # to be modified.

        if descr == search:
            # Write the modified record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(new_name) + '\n')

            # Set the found flag to True.
            found = True
        else:
            # Write the original record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(name) + '\n')
        # Read the next description.
        descr = dish_file.readline()
    # Close the restaurant file and the temporary file.
    dish_file.close()
    temp_file.close()
    # Delete the original coffee.txt file.
    os.remove(F_Name)
    # Rename the temporary file.
    os.rename('temp.txt', F_Name)
    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

# This program allows the user to delete
# a record in the F_Name file.
def Delete(F_Name):
   # Create a bool variable to use as a flag.
   found = False
   # Get the dish to delete.
   search = input('Which dish do you want to delete? ')
   # Open the original F_Name file.
   dish_file = open(F_Name, 'r')
   # Open the temporary file.
   temp_file = open('temp.txt', 'w')
   # Read the first record's description field.
   descr = dish_file.readline()
   # Read the rest of the file.
   while descr != '':
       # Read the quantity field.
       name = dish_file.readline()
       # Strip the \n from the description.
       descr = descr.rstrip('\n')
       # If this is not the record to delete, then
       # write it to the temporary file.
       if descr != search:
           # Write the record to the temp file.
           temp_file.write(descr + '\n')
           temp_file.write(str(name) + '\n')
       else:
           # Set the found flag to True.
           found = True
       # Read the next description.
       descr = dish_file.readline()
   # Close the F_Name file and the temporary file.
   dish_file.close()
   temp_file.close()
   # Delete the original F_Name file.
   os.remove(F_Name)
   # Rename the temporary file.
   os.rename('temp.txt', F_Name)
   # If the search value was not found in the file
   # display a message.
   if found:
       print('The file has been updated.')
   else:
       print('That item was not found in the file.')
# Call the
# Delete(F_Name) function.

def Add(F_Name):
    # Create a variable to control the loop.
    another = 'y'
    # Open the dish.txt file in append mode.
    dish_file = open(F_Name, 'a')
    # Add records to the file.
    while another == 'y' or another == 'Y':
        # Get the dish record data.
        print('Enter the following dish data to add new dishes please:')
        Name = input('Name: ')
        Prise = float(input('Prise: '))
        Calories = float(input('Calories: '))
        # Append the data to the file.
        dish_file.write((Name) + '\n')
        dish_file.write(str(Calories) + '\n')
        dish_file.write(str(Prise) + '\n')

        # Determine whether the user wants to add
        # another record to the file.
        print('Do you want to add another dish?')
        another = input('Y = yes, anything else = no: ')

    # Close the file.

    dish_file.close()
    #call the function
def sort(F_Name):
    #this function to sort items ascending
    print('These items have been sorted ascendingly')
    my_list = ['Kimchi', 'Dukbokki', 'Kimbap', 'Bulgogi']
    #show the orignal order
    print('orignal order:', my_list)
    my_list.sort()
    #show the sorted order
    print('sorted order:', my_list)
    #dish_file.close()
main()
