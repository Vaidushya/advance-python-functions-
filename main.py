# Add two lists using map and lambda
num1 = [1,2,3]
num2 = [4,5,6]
result = map(lambda x, y: x + y, num1, num2)
print("Addition of two lists: ", list(result))

#using map
numbers = [1,2,3,4,5]
def sequare(n):
    return n*n
square = list(map(sequare, numbers))
print("Square of numbers in list: ", square)