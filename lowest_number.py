#Program 2: Find the lowest number

#Create a program that ask 3 numbers.
no_1 = int(input("Enter number 1: "))
no_2 = int(input("Enter number 2: "))
no_3 = int(input("Enter number 3: "))

#Find the lowest number using only if-else statement.
if no_1 < no_2 and no_1 < no_3 :
    lowest_number = no_1
else:
    if no_2 < no_1 and no_2 < no_3 :
        lowest_number = no_2
    else:
        lowest_number = no_3
        
#Display the lowest number
print("The lowest number is {}.".format(lowest_number))