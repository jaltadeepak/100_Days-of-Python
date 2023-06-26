# division of int is always float
# int(floatingnumber) converts it into int, same for all data types
# PEMDASLR(left to right)
# // is floor division, gives the floor int number
# f-strings: a_f_string = f"{varaiblename} and whatever the string you want is" 

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip_perc = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_of_people = input("How many people to split the bill? ")

per_person_share = round(((float(bill) * ( 1 + int(tip_perc)/100)) / int(num_of_people)), 2)

#makes the decimal digits = 2 even when there aren't decimal values in the value itself
per_person_share = "{:.2f}".format(per_person_share) 

print(f"Each person should pay: ${per_person_share}")