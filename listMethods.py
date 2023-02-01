# numbers = [5, 2, 1, 6, 4]
# numbers.append(13)
# print(numbers)

# numbers = [5, 2, 1, 6, 4]
# numbers.insert(0, 10)
# print(numbers)


# numbers = [5, 2, 1, 6, 4]
# numbers.remove(5)
# print(numbers)


# numbers = [5, 2, 1, 6, 4]
# numbers.clear()
# print(numbers)

# numbers = [5, 2, 1, 6, 4]
# numbers.pop()
# print(numbers)

# numbers = [5, 2, 1, 6, 4]
# print(numbers.index(1))

# numbers = [5, 2, 1, 6, 4]
# print(50 in numbers)

# numbers = [5, 2, 1, 5, 6, 4]
# print(numbers.count(5))

# numbers = [5, 2, 1, 6, 4]
# numbers.sort()
# print(numbers)


# numbers = [5, 2, 1, 6, 4]
# numbers.sort()
# numbers.reverse()
# print(numbers)

# numbers = [5, 2, 1, 6, 4]
# numbers2 = numbers.copy()
# numbers.append(17)
# print(numbers)
# print(numbers2)


#remove the duplicates from the list
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


