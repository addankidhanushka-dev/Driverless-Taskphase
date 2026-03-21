
strings = []

n = int(input("Enter the number of strings: "))

for i in range(n):
    s = input("Enter the string: ")
    strings.append(s)


strings = [w.lower() for w in strings]
dict = {}
print(strings)


for k in range(len(strings)):
    for j in strings[k]:
       dict[j] = dict.get(j, 0) + 1
        
print(dict)
