class sort:
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

        return " ".join(arr)

strings = input("Enter the list of strings: ").split()
obj = sort(strings)

sorted_list = obj.selection_sort()
print("Sorted list: ", sorted_list)