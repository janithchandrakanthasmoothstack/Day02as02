



numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
oddCount = 0;
eveCount = 0;
for x in numbers:
    if x%2:
        oddCount +=1
    else:
        eveCount +=1

print(f"Number of even numbers: {oddCount}")
print(f"Number of odd numbers: {eveCount}")
