import csv
from user_interface import get_data as gt
from imp_files import read_txt as rt
from imp_files import read_csv as rc

def writing_csv ():
    file = 'exp2.csv'
    data_csv = rc()
    data = gt()
    if data:
        with open (file, 'a', newline='', encoding = 'utf-8') as r:
            writer = csv.writer(r) #, delimiter='', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['name', 'surname;birth', 'date', 'workplace', 'phone', 'number'])
            writer.writerows(data_csv)
        with open (file, 'a', newline='', encoding = 'utf-8') as r:
            r.write(f'{data[0]};{data[1]};{data[2]};{data[3]};{data[4]}\n')
    else:
        with open (file, 'a', newline='', encoding = 'utf-8') as r:
            writer = csv.writer(r) #, delimiter='', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(f'name;surname;birth_date;workplace;phone_number\n')
            writer.writerows(data_csv)
    print("Finish")


def writing_txt ():
    file = 'exp1.txt'
    data_txt = rt()
    data = gt()
    if data:
        with open (file, 'a', encoding = 'utf-8') as g:
            g.write(data_txt)
            g.write(f'name: {data[0]}\n\nsurname: {data[1]}\n\nbirth_date: {data[2]}\n\nworkplace: {data[3]}\n\nwphone_number: {data[4]}\n\n\n')
    else:
        with open (file, 'a', encoding = 'utf-8') as g:
            g.write(str(data_txt))
    print("Finish")
