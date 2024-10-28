# This will be an overview of the 7 basic concepts of Python.

## Concept 1: Data types & Variables
___
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

friends = 5

friends += 1

` print(friend) = 6 `
</br>
</br>

## Concept 3: Typecasting
**Purpose :** The process of converting a variable from one data type to another: str(), int(), float(), bool().
</br>
Note: You can find out what data type a variable is by using the `type` command.
</br>
---
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
</br>

**exampele: False** 
  ```python
  username = ""
  username = bool(username)

  print(username)
  ```

  output = false
___
  **exampele: True**
  ```python
  username = "amiel"
  username = bool(username)

  print(username)
  ```

output = true

## User input (I/O)
