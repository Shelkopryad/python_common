import matplotlib.pyplot as plt
import re

with open("C:\\Users\\user\\Desktop\\python\\plt.txt") as data_file:
    data = data_file.readlines()

tmp = [x.lower() for x in data[0] if re.match("[a-zA-Z]", x)]

arr = {}
for x in tmp:
    if x not in arr:
        arr[x] = 1
    else:
        arr[x] += 1

letters = [x for x in arr]
letters.sort()
counts = [arr[letter] for letter in letters]

x_axe = [x for x in range(0, len(letters))]

plt.xticks(x_axe, letters)
plt.plot(x_axe, counts, ls="--")
plt.scatter(x_axe, counts)

plt.show()