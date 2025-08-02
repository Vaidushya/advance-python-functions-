#--HomeWork--#

# Homework number 1

try:
    num = int(input("Enter a number: "))
    odd_num = [i for i in range(1, num + 1) if i % 2 != 0]
    print("Odd numbers:", odd_num)

except ValueError:
    print("Please enter a valid integer.")

# Homework number 2

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

cap_fruits = [fruit.capitalize() for fruit in fruits]

print(f"Original list of fruits: {fruits}")
print(f"Capitalized list of fruits: {cap_fruits}")

#--Done--#