import csv

rows = []

with open("Names.csv", "r") as file:
    reader = csv.reader(file)
   
    for r in reader:
        number = int(r[0])
        name = r[1].strip()
        rows.append((number, name))
        
    
rows.sort(key=lambda x:x[0])




filtered = [rows[i] for i in range(len(rows)) if ((i+1)%2==0)]


with open ("filtered.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(filtered)
    
combined = "".join(name.strip() for _, name in filtered)


min_diff = float("inf")         


for i in range(len(combined)-1):
    diff = abs(ord(combined[i])- ord(combined[i+1]))
    min_diff = min(min_diff,diff)
    
print("Min ASCII difference: ", min_diff)