print("welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = input("What percentage tip woul you like to give? 10, 12, or 15? ")
total_person = float(input("How many people to split the bill? "))

tip_percentage = (int(tip_percentage)/100)+1
final_bill = (total_bill/total_person)*tip_percentage
final_bill = round(final_bill,2)
print(f"Each person should pay : $ {final_bill}") 