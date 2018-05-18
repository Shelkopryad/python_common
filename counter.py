words = input("Write:\n")

def replace(s):
    return s.replace(".", "").replace(",", "").replace("!", "")

tmp = [x.lower() for x in replace(words).split()]
result = {}
for x in tmp:
    if x not in result:
        result[x] = 1
    else:
        result[x] += 1

print("\n", result)