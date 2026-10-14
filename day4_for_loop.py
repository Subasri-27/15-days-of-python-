
# Day 4: Python for Loops

# Program 1: Iterate through a string
for letter in "Apple":
    print(letter)

# Program 2: Print numbers from 0 to 4
for i in range(5):
    print(i)

# Program 3: Multiplication table of 2
for i in range(1, 11):
    print(i, "* 2 =", i * 2)

# Program 4: Multiplication table of 3
for i in range(1, 11):
    print(i, "* 3 =", i * 3)

# Program 5: Print odd numbers from 1 to 9
for i in range(1, 10, 2):
    print(i)

# Program 6: Countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)

# Program 7: Count backwards by 2
for i in range(10, 1, -2):
    print(i)

# Program 8: Multiples of 5 from 5 to 50
for i in range(5, 51, 5):
    print(i)

# Program 9: Countdown from 20 to 1
for i in range(20, 0, -1):
    print(i)

# Program 10: Even numbers from 10 to 30
for i in range(10, 31, 2):
    print(i)

# Program 11: Iterate through a list of names
names = ["Subasri", "Priya", "Kavi", "Anu"]
for name in names:
    print(name)

# Program 12: Print a star pattern using nested loops
for i in range(3):
    for j in range(2):
        print("*", end=" ")
    print()

# Program 13: Print numbers between two inputs
a = int(input("Enter A: "))
b = int(input("Enter B: "))

for i in range(a + 1, b):
    print(i)

# Program 14: Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)

# Program 15: Count even numbers from 1 to 10
count = 0

for i in range(1, 11):
    if i % 2 == 0:
        count += 1

print("Total even numbers:", count)
