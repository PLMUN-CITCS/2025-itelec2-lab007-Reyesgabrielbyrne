import math  # Import math module

# Step 1: Get numerical input
user_number = float(input("Enter a number to perform operations on: "))

# Step 2: Perform arithmetic operations
addition = user_number + 10
subtraction = user_number - 5
multiplication = user_number * 2
division = user_number / 3

# Step 3: Use math library functions
# Square root (handling negative input)
sqrt_value = math.sqrt(user_number) if user_number >= 0 else "Undefined for negative numbers"
# Sine of the user number (assumed to be in degrees)
sine_value = math.sin(math.radians(user_number))  # Convert to radians before taking sine

# Step 4: Display results with formatted output
print("\nArithmetic Operations:")
print(f"User number + 10 = {addition:.2f}")
print(f"User number - 5  = {subtraction:.2f}")
print(f"User number * 2  = {multiplication:.2f}")
print(f"User number / 3  = {division:.2f}")

print("\nMath Library Functions:")
print(f"Square root of {user_number:.2f} is: {sqrt_value}")
print(f"Sine of {user_number:.2f} degrees is: {sine_value:.4f}")