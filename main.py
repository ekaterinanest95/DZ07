# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# (txt - csv например)

# data = open('exp1.txt', 'r+') # код для удаления данных из файла
# data.seek(0)
# data.truncate()
# data.close()


from export import writing_txt
from export import writing_csv


writing_txt()
writing_csv()
