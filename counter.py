words = input("Write:\n")

tmp = [x.lower() for x in words.replace(",", "").split()]
result = {}
for x in tmp:
    if x not in result:
        result[x] = 1
    else:
        result[x] += 1

print("\n", result)