n = int(input("Enter the number of terms: "))

nums = []
for i in range(n):
    temp= int(input(":"))
    nums.append(temp)
    
hash_table = [[] for _ in range(10)]

for num in nums:
    index = num% 10
    hash_table[index].append(num)
    
    
for i in range(10):
    print(f"Index {i}:", hash_table[i])


