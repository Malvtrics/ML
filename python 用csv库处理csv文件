import csv

label_list = []
feature_list = []

with open("sales.csv","r") as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        label_list.append(row[-1])
        row_dict = {}
        for i in range(1,len(row)-1):
            row_dict[headers[i]] = row[i]
        feature_list.append(row_dict)

print(feature_list)
print(label_list)
