#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Even or odd
num = int(input("Enter a number:"))
if num & 1 == 0:
    print("Even")
else:
    print("Odd")


# In[5]:


#checking Vote Eligible
age = int(input("Enter your Age:"))
if age >=18:
    print("Your are Eligible to Vote.")
else:
    print("Your are not Eligible to Vote")


# In[8]:


#Positive, Negative, or Zero
number = int(input("Enter a Number:"))
if number > 0 :
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("zero")


# In[11]:


#leap year checker
year = int(input("Enter a Year:"))
if year%400 == 0 or year%4 == 0 and year%100 != 0:
    print("Given Number is leap year")
else:
    print("Given Number is not a leap year")


# In[13]:


#Maximum of two numbers
num1 = int(input("Enter a first number:"))
num2 = int(input("Enter a second number:"))
if num1 > num2:
    print(f"{num1} is highest Number")
elif num2 > num1:
    print(f"{num2} is highest Number")
else:
    print("Both are same")


# In[15]:


#Grade Calculator
marks = int(input("Enter your marks:"))
if marks>=90:
    print("Grade:A")
elif marks>=80:
    print("Grade:B")
elif marks>=70:
    print("Grade:C")
elif marks>=60:
    print("Grade:D")
else:
    print("Grade:F")


# In[18]:


#Character Type
letter = input("Enter a letter between (a-z):").lower()
Vowels = 'aeiou'
if letter in Vowels:
    print("Given letter is Vowel")
else:
    print("Given letter is a Consonant")


# In[27]:


#Divisible by Both
num = int(input("Enter a number:"))
if num%3==0 & num%5==0:
    print("Given Number is divisible by both 3 and 5")
else:
    print("Given Number is not divisible by both 3 and 5")


# In[20]:


#Day of Week
day_num = int(input("Enter a Number between (1-7):"))
if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    print("Invalid number")


# In[31]:


#Simple Calculator
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
operator = input("Enter a operator(+,-,*,/):")
if operator == '+':
    print(f"Addition of two Numbers:{num1+num2}")
elif operator == '-':
    print(f"Subtraction of two Numbers:{num1-num2}")
elif operator == '*':
    print(f"Multiplication of two Numbers:{num1*num2}")
elif operator == '/':
    if num2 == 0:
        print("Division is not possible by zero")
    else:
        print(f"Division of two Numbers:{num1/num2}")
else:
    print("Invalid values")


# In[1]:


#Triangle Type
s1 = float(input("Enter side1:"))
s2 = float(input("Enter side2:"))
s3 = float(input("Enter side3:"))

if s1+s2>s3 and s2+s3>s1 and s3+s1>s2:
    if s1==s2==s3:
        print("Equilateral Triangle")
    elif s1==s2 or s2==s3 or s3==s1:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")


# In[2]:


#Electricity Bill Calculator
units = int(input("Enter units:"))
bill = 0
if units <= 100:
    bill = 0
elif units <=200:
    bill = (units-100)*5
else:
    bill = (100*5)+(units-200)*10

print(f"{units} units of Amount is Rs/-{bill}")


# In[3]:


#ATM Withdrawal
amount_withdrawal = int(input("Enter amount to withdraw:"))
balance = 5000

if amount_withdrawal >= balance:
    print("Check Your Balance Amount")
elif amount_withdrawal > balance-500:
    print("Minimum balance upto 500 Required")
else:
    balance -= amount_withdrawal
    print(f"Total Balance:{balance}")


# In[4]:


#Discount Calculator
amount = float(input("Enter purchase amount:"))
final_bill = amount
if amount > 5000:
    discount = amount*0.2
    final_bill = amount-discount
    print(f"Discount:20% final Bill:{final_bill}")
elif amount > 2000:
    discount = amount*0.10
    final_bill = amount-discount
    print(f"Discount:10% final Bill:{final_bill}")
else:
    print(f"Discount: 0% final Bill:{final_bill}")


# In[5]:


#BMI Calculator
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))

BMI = weight/(height**2)
print(f"Your BMI:{BMI}")

if BMI < 18.5:
    print("Category:Underweight")
elif BMI < 25:
    print("Category:Normalweight")
else:
     print("Category:obese")


# In[6]:


#Multiplication Table
number = int(input("Enter a number:"))
for i in range(1,11):
    print(f"{number}x{i}={number*i}")


# In[8]:


#Sum of Natural Numbers
number = int(input("Enter a number:"))
sum = 0
for i in range(number+1):
    sum += i
print(f"Sum first {number} Natural numbers:{sum}")


# In[11]:


#factorial Calculator
number = int(input("Enter a number:"))
fact = 1
for i in range(1,number+1):
    fact *= i
print(f"factorial of {number} is {fact}")


# In[13]:


#Count Digits
num = int(input("Enter a number:"))
count = 0
for i in str(num):
    count += 1
print(f"Given number {num} in total digits {count}")


# In[15]:


#print Pattern
n = 5
for i in range(n+1):
    for j in range(i):
        print("*",end="")
    print()


# In[18]:


#Sum of Even Numbers
sum = 0
for i in range(1,101):
    if i%2 == 0:
        sum +=i
print(f"Sum of Even Numbers from 1 to 100:{sum}")


# In[19]:


#Prime Number Check
num = int(input("Enter a number:"))
if num <=1:
    print("Not prime")
else:
    for i in range(2,num):
        if num % i ==0:
            print("Not prime")
            break
    else:
        print("prime")


# In[ ]:


#Guess the Number
import random
secret = random.randint(1,100)
attempts = 0
while True:
    guess = int(input("Enter a number Your guess:"))
    attempts +=1
    if guess == secret:
        print(f"Correct! you took {attempts} attempts")
        break
    elif guess<secret:
        print("Too low! Try again")
    else:
        print("Too high! Try again")


# In[ ]:


#Sum Until Zero
total = 0
num = int(input("Enter a number (0 to stop):"))
while num!=0:
    total+=num
    num = int(input("Enter another number(0 to stop):"))

print(f"su of all numbers:{total}")


# In[ ]:


#Reverse a Number
num  = int(input("Enter a number:"))
reverse = 0
orginal_number = num
while num > 0:
    value=num%10
    reverse = reverse*10+value
    num = num//10

print(reverse)


# In[ ]:


#Countdown Timer
count = 10
while count>0:
    print(count)
    count -=1
print("Blast off")


# In[ ]:


#Armstrong Number
num = int(input("Enter a number:"))
orginal = num
length = len(str(num))
armstrong = 0
while num>0:
    value = num%10
    armstrong = (value**length)+armstrong
    num = num//10
if orginal == armstrong:
    print("Given number is Armstrong")
else:
    print("Given number is not Armstrong")


# In[ ]:


#Find first Multiple
for i in range(1,100):
    if i%7==0:
        print(f"first Number divisible by 7 is:{i}")
        break


# In[ ]:


#skip Multiples of 3
for i in range(1,20):
    if i%3==0:
        continue
    else:
        print(i)


# In[ ]:


#Menu-Driven Program
while True:
    print("\n---Menu---")
    print("1.Say Hello")
    print("2.Print Date")
    print("3.Print Numbers 1-10")
    print("4.Exit")
    
    choice = int(input("Enter your option:"))
    
    if choice == 1:
        print("Hello, How are you") 
    elif choice == 2:
        import datetime
        print("Today's date:",datetime.datetime.now().strftime("%Y-%m-%d"))
    elif choice == 3:
        for i in range(1,11):
            print(i)
    elif choice == 4:
        print("Good Bye!, Have a Nice day..")
        break
    else:
        print("Invalid choice!")


# In[2]:


#Simple Calculator with Match
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
operator = input("Enter a operator(+,-,*,/):")

match operator:
    case '+':
        print(f"{num1}+{num2}:{num1+num2}")
    case '-':
        print(f"{num1}-{num2}:{num1-num2}")
    case '*':
        print(f"{num1}*{num2}:{num1*num2}")
    case '/':
        if num2==0:
            print("zero is not divisble by division")
        else:
            print(f"{num1}/{num2}:{num1/num2}")
    case '_':
        print("Invalid operator")


# In[3]:


#HTTP Status Codes
code = int(input("Enter the Code:"))

match code:
    case 200:
        print("Successfull login")
    case 201:
        print("Login Fail")
    case 202:
        print("Resource has moved")
    case 203:
        print("Unauthorized")
    case _:
        print("Unknow code Enter")


# In[5]:


#Shape Area Calculator
shape = input("Enter the shape(circle,square,rectangle):")
match shape:
    case 'circle':
        radius = float(input("Enter a radius of a circle"))
        area = 3.14*radius**2
        print("Area of circle",area)
    case 'square':
        side = float(input("Enter side length:"))
        area = side**2
        print("Area of Square",area)
    case 'rectangle':
        length = float(input("Enter length:"))
        width = float(input("Enter width:"))
        area = length*width
        print("Area of Rectangle:",area)
    case '':
        print("Invalid shape")


# In[9]:


#Number Pyramid
n=5
for i in range(n+1):
    for j in range(i):
        print(i,end =' ')
    print()


# In[10]:


#Fibonacci series
n = int(input("Enter a number:"))
f1,f2 = 0,1
count = 0
while count<n:
    f3 = f1+f2
    f1 = f2
    f2 = f3
    count += 1
    print(f1)


# In[11]:


#Palindrome Checker
text = input("Enter a string:").lower()
orginal = text
reverse = ''
for i in text:
    reverse = i+reverse

if reverse == orginal:
    print(f"Given text {text} is a Palindrome")
else:
    print(f"Given text {text} is not a Palindrome")


# In[12]:


#Pattern with Break
num = int(input("Enter a number:"))
for i in range(1,11):
    if i%4==0:
        print(f"Found {i} divisible by 4. Stopping!")
        break
    else:
        print(i)


# In[13]:


#Valid password checker
password = input("Enter a Password:")
has_number = False
has_special = False
special_characters = "!@#$%^&*()_-?/.,[]{}`~"
if len(password)<8:
    print("Password must be atleast 8 characters long")
else:
    for char in password:
        if char.isdigit():
            has_number = True
        if char in special_characters:
            has_special = True
    
    if has_number and has_special:
        print("Password is valid!")
    else:
        if not has_number:
            print("Password must contain at least one number")
        if not has_special:
            print("Password must contain at least one special character")


# In[14]:


#Number Guessing with Hint
import random
secret = random.randint(1,50)
attempts = 0
max_attempts = 7
print("I am thinking of a number between 1 and 50")
print(f"you have {max_attempts} attempts")

while attempts<max_attempts:
    guess = int(input("Your guess:"))
    attempts += 1
    
    if guess == secret:
        print(f"Correct! You guessed it in {attempts} attempts!")
        break
    elif guess<secret:
        print(f"Too low! Attempts left:{max_attempts-attempts}")
    else:
        print(f"Too low! Attempts left:{max_attempts-attempts}")
else:
    print(f"Game over! The number was {secret}")
        


# In[15]:


#Rock Paper Scissors
import random
choices = ["rock","paper","scissors"]
computer = random.choice(choices)
user = input("Enter rock,paper or scissors:").lower()
if user not in choices:
    print("Invalid choice!")
else:
    print(f"Computer chose:{computer}")
    
    match(user,computer):
        case(u,c)if u==c:
            print("it's a tie!")
        case("rock","scissors"):
            print("You win! Rock crushes scissors")
        case("paper","rock"):
            print("You win! Paper covers rock")
        case("scissors","paper"):
            print("You win! Scissors cut paper")
        case _:
            print(f"You lose!{computer} beats {user}")


# In[16]:


#Combine Everything into one program
def main():
    while True:
        print("/--Menu--")
        print("1.Even/Odd Checker")
        print("2.Grade Calculator")
        print("3.Multiplication Table")
        print("4.Factorial Calculator")
        print("5.Guess the Number Game")
        print("6.Palindrome Checker")
        print("7.Rock Paper Scissors")
        print("8.Exit")
        
        choice = input("Enter your Choice (1-8):")
        
        match choice:
            case '1':
                num = int(input("Enter a number:"))
                if num & 1 == 0:
                    print("Even")
                else:
                    print("Odd")
            case '2':
                marks = int(input("Enter your marks:"))
                if marks>=90:
                    print("Grade:A")
                elif marks>=80:
                    print("Grade:B")
                elif marks>=70:
                    print("Grade:C")
                elif marks>=60:
                    print("Grade:D")
                else:
                    print("Grade:F")
            case '3':
                number = int(input("Enter a number:"))
                for i in range(1,11):
                    print(f"{number}x{i}={number*i}")
            case '4':
                number = int(input("Enter a number:"))
                fact = 1
                for i in range(1,number+1):
                    fact *= i
                print(f"factorial of {number} is {fact}")
            case '5':
                import random
                secret = random.randint(1,50)
                attempts = 0
                max_attempts = 7
                print("I am thinking of a number between 1 and 50")
                print(f"you have {max_attempts} attempts")
                
                while attempts<max_attempts:
                    guess = int(input("Your guess:"))
                    attempts += 1
                    if guess == secret:
                        print(f"Correct! You guessed it in {attempts} attempts!")
                        break
                    elif guess<secret:
                        print(f"Too low! Attempts left:{max_attempts-attempts}")
                    else:
                        print(f"Too low! Attempts left:{max_attempts-attempts}")
                else:
                    print(f"Game over! The number was {secret}")
            case '6':
                text = input("Enter a string:").lower()
                orginal = text
                reverse = ''
                for i in text:
                    reverse = i+reverse
                
                if reverse == orginal:
                    print(f"Given text {text} is a Palindrome")
                else:
                    print(f"Given text {text} is not a Palindrome")
            case '7':
                import random
                choices = ["rock","paper","scissors"]
                computer = random.choice(choices)
                user = input("Enter rock,paper or scissors:").lower()
                if user not in choices:
                    print("Invalid choice!")
                else:
                    print(f"Computer chose:{computer}")
                
                match(user,computer):
                    case(u,c)if u==c:
                        print("it's a tie!")
                    case("rock","scissors"):
                        print("You win! Rock crushes scissors")
                    case("paper","rock"):
                        print("You win! Paper covers rock")
                    case("scissors","paper"):
                        print("You win! Scissors cut paper")
                    case _:
                        print(f"You lose!{computer} beats {user}")
            case '8':
                print("Good Bye!")
                break
            case _:
                print("Invalid Choice!")

if __name__ == "__main__":
    main()
    


# In[ ]:




