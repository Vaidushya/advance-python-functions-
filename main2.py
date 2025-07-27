# Zip elements of two lists
s1 = [1,2,3]
s2 = ["a","b","c"]
s3 = list(zip(s1, s2))

print(s3, "\n")

# Zip elements of two lists
# Print elements one by one, but elements of 2nd list will be in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)


# Zip into dictionary
stock = ['reliance', 'infosys', 'tcs']
price = [2175, 1127, 2750]
new_dict = {stock: price for stock, price in zip(stock, price)}
print('\n{}'.format(new_dict))
