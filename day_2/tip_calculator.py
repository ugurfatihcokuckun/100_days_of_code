#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("bill: "))
split = float(input("How  manny people share this bill: "))
percentage = float(input ("Enter the tip percentage: "))

total = ((bill * (percentage/100) + bill) / split)
total = "{:.2f}".format(total)
print(f"Each person should pay {total} ")