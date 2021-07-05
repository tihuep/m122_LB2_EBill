from os import listdir
from os.path import isfile, join
import re

def get_all_invoices_from_receipts():
    path = '/tmp/m122_eBill/receipts'
    receipts_filenames = [f for f in listdir(path) if isfile(join(path, f))]

    def filter_receipt(receipt):
        if (re.match('^quittungsfile.+\.txt$', receipt)):
            return True
        else:
            return False

    receipt_filter = filter(filter_receipt, receipts_filenames)
    filtered_receipts = []
    for receipt in receipt_filter:
        filtered_receipts.append(receipt)

    receipt_invoice_email = []
    for receipt in filtered_receipts:
        file = open('/tmp/m122_eBill/receipts/' + receipt, 'r')
        Lines = file.readlines()
        file.close()
        for line in Lines:
            if line.split(' -- ')[0].find('.xml') > 0:
                invoice_number = line.split(' -- ')[1].split('/')[1][4:]
                receipt_invoice_email.append([invoice_number, receipt, get_invoice_file(invoice_number), get_email_of_invoice(invoice_number)])
    return receipt_invoice_email

def get_invoice_file(invoice_number):
    path = '/tmp/m122_eBill/six_files/'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for file in files:
        if file.__contains__('invoice.txt'):
            if file.__contains__(invoice_number):
                return file
    return None

def get_email_of_invoice(invoice_number):
    file = open('/tmp/m122_eBill/inv_email.csv', 'r')
    lines = file.readlines()
    for line in lines:
        if line.split(';')[0] == invoice_number:
            return line.split(';')[1]
    return None