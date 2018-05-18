import os

file_name = "mathhack.py"
sentence = input("sentence:\n")

f = open(file_name, "w+")
f.write("a = " + str(sentence) + "\nprint(a)")
f.close()

os.system("python " + file_name)
# os.remove(file_name)
