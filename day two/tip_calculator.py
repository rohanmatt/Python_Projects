print("Welcome to the tip calculator.")
total_bill= float( input ("What was the total bill? $"))
tip_percent= int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_people= int(input("How many people to split the bill? "))
payment = total_bill/no_people * (tip_percent+100)/100
final_amount= round(payment,2)
print(f"Each person should pay: ${final_amount}")
