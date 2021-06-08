import csv
from os import listdir
from os.path import isfile, join

def parse_csv(filename):
    csv_data = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            csv_data.append(row)
            print('#'.join(row))
    return csv_data

def get_all_csv_files():
    #https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    path = 'tmp/invoices'
    return [f for f in listdir(path) if isfile(join(path, f))]