import csv
from os import listdir
from os.path import isfile, join

def parse_csv(filename):
    csv_data = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvreader:
            csv_data.append(row)
    return csv_data

def get_all_csv_files():
    #https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    path = '/tmp/m122_eBill/invoices'
    return [f for f in listdir(path) if isfile(join(path, f))]