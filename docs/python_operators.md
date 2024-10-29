# Python Operators

In Python, operators are symbols or keywords that perform specific operations on variables and values. Below are the main types of operators in Python:

## 1. Arithmetic Operators
- `+` : Addition, e.g., `3 + 5` gives `8`
- `-` : Subtraction, e.g., `5 - 2` gives `3`
- `*` : Multiplication, e.g., `4 * 3` gives `12`
- `/` : Division, e.g., `10 / 2` gives `5.0`
- `%` : Modulus (remainder), e.g., `10 % 3` gives `1`
- `**` : Exponentiation, e.g., `2 ** 3` gives `8`
- `//` : Floor Division, e.g., `9 // 2` gives `4`

## 2. Comparison Operators (Relational Operators)
- `==` : Equal to, e.g., `5 == 5` gives `True`
- `!=` : Not equal to, e.g., `5 != 3` gives `True`
- `>` : Greater than, e.g., `6 > 3` gives `True`
- `<` : Less than, e.g., `3 < 5` gives `True`
- `>=` : Greater than or equal to, e.g., `5 >= 5` gives `True`
- `<=` : Less than or equal to, e.g., `3 <= 4` gives `True`

## 3. Assignment Operators
- `=` : Assigns a value, e.g., `x = 5`
- `+=` : Adds and assigns, e.g., `x += 3` (same as `x = x + 3`)
- `-=` : Subtracts and assigns, e.g., `x -= 2`
- `*=` : Multiplies and assigns, e.g., `x *= 4`
- `/=` : Divides and assigns, e.g., `x /= 2`
- `%=` : Modulus and assigns, e.g., `x %= 3`
- `//=` : Floor division and assigns, e.g., `x //= 2`
- `**=` : Exponentiation and assigns, e.g., `x **= 3`

## 4. Logical Operators
- `and` : Returns `True` if both statements are true, e.g., `x > 3 and x < 10`
- `or` : Returns `True` if one of the statements is true, e.g., `x < 3 or x < 10`
- `not` : Inverts the result, e.g., `not(x < 5)` gives `False` if `x < 5` is `True`

## 5. Bitwise Operators
- `&` : AND, e.g., `5 & 3` gives `1`
- `|` : OR, e.g., `5 | 3` gives `7`
- `^` : XOR, e.g., `5 ^ 3` gives `6`
- `~` : NOT (inverts bits), e.g., `~5` gives `-6`
- `<<` : Left shift, e.g., `5 << 1` gives `10`
- `>>` : Right shift, e.g., `5 >> 1` gives `2`

## 6. Membership Operators
- `in` : Returns `True` if a value is in a sequence, e.g., `"a" in "apple"`
- `not in` : Returns `True` if a value is not in a sequence, e.g., `"b" not in "apple"`

## 7. Identity Operators
- `is` : Returns `True` if both variables point to the same object, e.g., `x is y`
- `is not` : Returns `True` if both variables point to different objects, e.g., `x is not y`

## 8. Ternary Operator
Used for conditional expressions: `a if condition else b`
- Example: `result = "Positive" if x > 0 else "Negative or Zero"`

Each of these operators has a specific purpose, helping you perform a variety of operations on data.
