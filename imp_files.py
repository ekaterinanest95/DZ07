import csv

def read_txt(device=1):
    file = 'imp1.txt'
    with open(file, 'r', encoding='utf-8') as d1:
        text = d1.read()
        print(text)
    return(text)



def read_csv(device=1):
    file = 'imp2.csv'
    with open(file, 'r', newline='') as d:
        reader = csv.reader(d)
        rows = []
        for row in reader:
            rows.append(row)
    return(rows)



print(read_csv())
print(read_txt())