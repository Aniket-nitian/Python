# 1st sol

age = input("Enter your age: ")
age = int(age)

if (age<13):
    print("Child")
    exit()

elif (age>=13 and age <=19):
    print("Teenager")

elif age>=20 and age<=59:
    print("Adult")

else:
    print("Senior")


## 2nd sol

age =22
day = "Wednesday"

price = 12 if age >=18 else 8
if day == "Wednesday":
    price = price - 2

print("Ticket price for you is: $",price)


# 3rd

marks = 68

garde = "A" if marks >=90 else "B" if marks >=80 else "C" if marks >=70 else "D" if marks >=60 else "F"

print("Your garde is: ", garde)