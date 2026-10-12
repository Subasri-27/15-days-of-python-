
# Program 1: Pass or Fail

mark = int(input("Enter mark: "))
if mark >= 35:
    print("Pass")
else:
    print("Fail")


# Program 2: Scholarship Eligibility

income = int(input("Enter income: "))
if income > 7000:
    print("Not eligible for scholarship")
else:
    print("Scholarship is available")


# Program 3: Check Divisibility by Both 3 and 5

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")


# Program 4: Check Even or Odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Program 5: Student Performance Classification

score = int(input("Enter the score: "))
if score >= 70:
    print("Good Student")
elif score > 35:
    print("Average Student")
else:
    print("Poor Student")


# Program 6: Simple Calculator Using If-Elif-Else

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
operation = input("Enter add/sub/mul/div: ")

if operation == "add":
    print(a + b)
elif operation == "sub":
    print(a - b)
elif operation == "mul":
    print(a * b)
elif operation == "div":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")


# Program 7: Check Eligibility Before Collecting Details

score = int(input("Enter your score: "))
if score >= 70:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    location = input("Enter your location: ")
    print("You are eligible")
else:
    print("You are not eligible")


# Program 8: Loan Eligibility and Loan Amount Check

salary = int(input("Enter salary: "))
age = int(input("Enter age: "))
if salary >= 20000 or age <= 25:
    amount = int(input("Enter loan amount: "))

    if 0 < amount <= 50000:
        print("Eligible for loan amount")
    elif amount > 50000:
        print("Maximum loan amount is 50000")
    else:
        print("Enter a valid loan amount")
else:
    print("Not eligible")


# Program 9: Calculate Average of Five Values

one = int(input("Enter value 1: "))
two = int(input("Enter value 2: "))
three = int(input("Enter value 3: "))
four = int(input("Enter value 4: "))
five = int(input("Enter value 5: "))

avg = (one + two + three + four + five) / 5
print("Average:", avg)

if avg < 35:
    print("Additional class is required")
else:
    print("You are good to go")
