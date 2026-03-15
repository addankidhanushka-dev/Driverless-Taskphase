n = int(input("Enter the number of terms: "))

nums = []

for i in range(n):
    temp = int(input(":"))
    nums.append(temp)
    
hash_table = [[] for _ in range(10)]

def binary_insert(bucket, value):
    low =0
    high = len(bucket)
    
    while (low < high):
        mid = (low + high)//2
        
        if (value > bucket[mid]):
            low = mid+1
        else:
            high = mid
    
    bucket.insert(low, value)
    
for num in nums:
    index = num% 10
    binary_insert(hash_table[index], num)
        
for i in range(10):
    print(f"Index {i}:", hash_table[i])