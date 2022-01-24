#Author: Noah Brinsden
#Homework Number & Name: 1, Brinsden_Noah_HW1
#Due Date: 9/9/2019
#Program Description: Parking Garage & Ticket Calculation


#Calculating Time Entered
hours_entered = int(input("Hour Entered: "))
minutes_entered = int(input("Minute Entered: "))
total_enter_minutes = (hours_entered*60)+ minutes_entered

#Calculating Time Exited
hours_exit = int(input("Hour Exited: "))
minutes_exit = int(input("Minutes Exited: "))
total_exit_minutes = (hours_exit*60) + minutes_exit

#Total time
total_minutes = int(total_exit_minutes - total_enter_minutes)
total_time = float(total_minutes / 60)
validated_hour = float(input("Hours validated: "))
final_time = float(total_time - validated_hour)

#Pricing
hourly_rate = float(input("Price: $"))
total_price = (hourly_rate * final_time) 
tax = (.0625 * total_price)
total_with_tax = (tax + total_price)

#Total Cost Less Validation
total_cost_validation = (final_time * hourly_rate)

#Receipt
blank_line = ''
print(blank_line)
print("Receipt:")

#Receipt Entrance Time
print("Entrance Time: ", sep ="", end="")
print(format(hours_entered, '02d'), ":", sep="", end ="")
print(format(minutes_entered, '02d'))

#Receipt Exit Time
print("Exit Time: ", sep = "", end="")
print(format(hours_exit, '02d'), ":", sep='', end='')
print(format(minutes_exit, '02d'))

#Receipt Hours Used
print("Hours Used: ", end="")
print(format(total_time, '.1f'))

#Receipt Hours Validated
print("Hours Validated: ", end='')
print(format(validated_hour, '.1f'))

#Receipt Total Cost Less Validation    
print("Total Cost Less Validation: $", end='')
print(format(total_cost_validation, '.2f'))

#Receipt Tax Cost
print("Tax Cost: $", end = '')
print(format(tax, '.2f'))

#Receipt Total Cost
print("Total Cost: $", end='')
print(format(total_with_tax, '.2f'))

                    


