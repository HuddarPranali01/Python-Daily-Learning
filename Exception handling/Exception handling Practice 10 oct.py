'''
#1:Basic try-except (Handling Division by Zero)
#Write a script that safely divides two numbers provided by the user.
try:
    numerator = int(input("Enter number1:"))
    denominator = int(input("Enter number2:"))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero!")

print("Program continues running smoothly...")
'''
'''
Example 2: Handling Multiple Specific Exceptions
Ask the user for a number, convert it to an integer, and
divide 100 by it. Handle both non-numeric inputs and zero inputs.

try:
    user_input = input("Enter a number to divide 100: ")
    number = int(user_input)
    result = 100 / number
    print(f"100 divided by {number} is {result}")
except ValueError:
    print("Error: Please enter a valid integer, not text.")
except ZeroDivisionError:
    print("Error: You cannot enter zero as the divisor.")
'''
'''
#Example 3: Using else and finally
#•	else: Runs only if no exceptions occurred in the try block. 
#•	finally: Always runs at the end, regardless of whether an error occurred or not (ideal for cleanup tasks like closing files or database connections). 
#•	Task: Demonstrate a complete flow using try, except, else, and finally.

try:
    number = int(input("Enter a positive number: "))
    if number < 0:
        raise ValueError("Number cannot be negative.")
except ValueError as e:
    print(f"Invalid input: {e}")
else:
    print(f"Success! You entered: {number}")
finally:
    print("Execution complete. Cleaning up resources...\n")
'''






