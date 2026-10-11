#Positive Negative number 

num= int(input("Enter a number:"))
if num>0:
       print("Positive")
else:
       print("Zero or Negative")


#Voting eligibility 

age=int(input("Enter your age:"))
if age>=18:
       print("Eligible")
else:
       print("Not Eligible")


#password check 

password=int(input("Enter a password:"))
if password=="python123":
       print("Login successful")
else:
       print("Wrong password")


#Pass/Fail 

num=int(input("Enter your marks :"))
if num>=35:
     print("Pass")
else:
     print("Fail")

     
#Grade classification

marks=int(input("Enter your marks:"))
if marks >=90:
     print("Grade A")
elif marks >=70:
     print("Grade B")
elif marks >=35:
     print("Grade C")
else:
     print("Fail")