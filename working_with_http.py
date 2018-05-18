import matplotlib.pyplot as plt
import requests
import re

response = requests.get('http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html')
arr = response.content

tmp = [x.lower() for x in str(arr) if re.match("[a-zA-Z1-9]", x)]

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