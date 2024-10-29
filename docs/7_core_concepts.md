# This will be an overview of the 7 basic concepts of Python.

## Concept 1: Data types & Variables

**Variable** = a reusable container for a value (store values in it). 

There are 4 main data types in python: integers(int), strings(str), booleans(boo), and floats(float).

___
### **Strings**:
a group of characters. </br>
Example: `name = John`

### **Integers**:
Whole numbers values. </br>
Example: `num1 = 14`

### **Floats**:
Number values with a decimal. </br>
Example: `gpa = 3.4`

### **Booleans**:

Variables thet are either True or False. </br>
Example: `is_raining = True`

---
**Full variable Code Example:**

Sting :`name = John` </br>
Integer :`age = 14` </br>
Float: `gpa = 3.4` </br>
Boolean: `is_raining = true`
</br>
</br>
## Concept 2: Basic Arithmetic Operations
___
### <u>**Arithmetic**</u>
#####
**addition :** + </br>
**subtraction :** - </br>
**multiplication :** * </br>
**division (return a float) :** /</br>
**integer division (return as an integer) :** //</br>
**remainder:** %

**<u>Augmented Assignment: </u>** </br>


**Purpose:** If you don't want to do long hand arithmetic operators i.e. (friends = friends + 1), </br>
you can use an augmented assignment. i.e. (friends += 1)


It is performed by typing the variable and then adding the arithmetic Operation (+, -, /, *, //, *) directly to an ( = ) sign and then printing it. 
  </br> 

### <u>**Exampele:**</u>
```python
friends = 5

friends += 1

` print(friend) = 6 `
```


## Concept 3: Typecasting
___

**Purpose :** The process of converting a variable from one data type to another: `str()`, `int()`, `float()`, `bool()`.
</br>
Note: You can find out what data type a variable is by using the `type` command.
</br>

**Example:** </br>
```python
name = "Amiel"
age = 30
gpa = 3.2
is_engineer = True

print(type(age))
```
output = <class 'int'>
</br>
---
**Example:** </br>
```python
name = "Amiel"
age = 30
gpa = 3.2
is_engineer = True

gpa = int(gpa)

print(gpa)
```

output = 3

___
**Important Note:** </br>
- booleans only output "True" or "False". Changing the value inside the variable when typecasting will mostly return true. </br>
A good usecase for it would be to use it for user registration. 
</br>


**Example: False** 
  ```python
  username = ""
  username = bool(username)

  print(username)
  ```

  output = false
___
  **Example: True**
  ```python
  username = "amiel"
  username = bool(username)

  print(username)
  ```

output = true
</br>

## Concept 4: User input (I/O)
___
This is how you get user input to store a variable to use later in the module. </br>
`input()` is to store input into variable. </br>
`print()` is to output the result. </br>

**Example:** </br>
```python
name = input("What is your name? ")
age = input("How old are you?")

print(f"Hello {name}, you are {age} years old!")
```
output = Hello amiel, you are 30 years old!
___
**Important note:**
If you want to do anything to the store variable outside of printing it, you must define the data type (typecast) and before hand.
</br>
Also ensure that when typecasting, put `int()`, `float()`, `str()`, or `bool()` **_<u>before</u>_** `input()`. 

**Example:**
```python
name = input("What is your name? ")
age = int(input("How old are you?" ))

age += 1

print(f"Hello {name}, you are {age} years old!")
```
output : Hello amiel, you are 31 years old!
</br>
## Concept 5: `if` statements
if statements = can execute some code if a condition is True, otherwise can have secondary & tertiary conditional actions. 
Allows for basic decision-making. </br>
(if, elif, else).

**Example:**
```python
age = int(input("How old are you? "))

if age >= 18: 
    print("You are old enough!")
else: 
    print("You are not old enough.")
```
___
`elif` statements = statements that are a secondary condition to the `if` statement. 
`else` statements = statements that everything else falls under. </br>
**example:**
```python
age = int(input("How old are you? "))

if age > 65:
  print("You are a senior citizen")
elif age >= 18:
  print("You are old enough!")
elif age <= 0:
  print("You haven't been born yet!")
else:
  print("You are not old enough.")
```
<u>**Important note:**</u> 
</br>
Python will read the statement in the order that you put it. Once the value (input) meets the condition, the module will stop reading statements and print which condition it met. </br>
</br>So the order in which you type your statements matters. Ensure that you write the statements so that they are conditionally true or false in order. 
___

### `if` statements with Booleans: 
You can also use `booleans` with `if` statements. 
if would be good with things like authentication and permission based applications. 
</br>
**Example 1:**
```python
# Simulate correct credentials
correct_username = "admin"
correct_password = "password123"

username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

# Check if the credentials are correct
if username == correct_username and password == correct_password:
  is_logged_in = True
else:
  is_logged_in = False

# Use the Boolean variable in an if statement
if is_logged_in:
  print("Welcome back!")
else:
  print("Invalid credentials, please try again.")

```
**Example 2:**
```python
# Define the minimum age requirement
minimum_age = 21

# Ask the user for their age
age = int(input("Please enter your age: "))

# Check if the user meets the age requirement
if age >= minimum_age:
  is_allowed_access = True
else:
  is_allowed_access = False

# Use the Boolean variable in an if statement
if is_allowed_access:
  print("Access granted! Welcome to the restricted section.")
else:
  print("Access denied. You must be at least 21 years old.")
```
___
**Example 3 (where boolean is not contingent on input):**
```python
age = int(input("How old are you? "))
has_ticket = True
price = 10.00

# Check age credentials
if age <= 0:
  print("error, please enter a valid age")
elif age > 65:
  print("You are a senior citizen")
  print(f"The price for a senior ticket is ${price * 0.75}")
elif age >= 18:
  print("You are old enough!.")
  print(f"The price for an adult ticket is ${price}")
else:
  print("You are a child.")
  print(f"The price for a child ticket is ${price * 0.85}")
```

## Concept 5: Logical Operators:
Logical operators allows us to evaluate multiple conditions (`or`, `and`, `not`)
- `or` - at least one conditions must be True
- `and` - both conditions must be True
- `not` - inverst the condition (not False, not True)

```python
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining: 
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
```