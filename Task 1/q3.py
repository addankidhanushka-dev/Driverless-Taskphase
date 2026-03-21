class StringOperations:
    
    def __init__(self, string):
        self.string = string


    def selection_sort(self):
        arr = self.string
        n = len(arr)

        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j].lower() < arr[min_index].lower():
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

        return (arr)
        
    def binary_search(self, key):
        a = self.string
        key = key.lower()
        last = len(a)-1
        first = 0
        mid = (first+last)//2

        while first<=last:
            mid = (first+last)//2
            
            if a[mid].lower() < key:
                first = mid + 1
            elif a[mid].lower() > key:  
                last = mid - 1
            elif a[mid].lower() == key :
                return mid

    
        return -1


strings = input("Enter the string: ").split()
obj = StringOperations(strings)
sorted_list = obj.selection_sort()
print("Sorted List: \n", sorted_list)

search_key = input("Enter the key to search: ")


result = obj.binary_search(search_key)

if result != -1:
    print("String found at index:", result)
else:
    print("String not found")
    