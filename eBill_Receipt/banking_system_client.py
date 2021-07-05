from ftplib import FTP
import re

def download_receipts():
    receipts = get_receipt_filenames()
    ftp = get_ftp_connection()
    receipt_count = 0
    for receipt in receipts:
        filename = receipt[62:len(receipt)]
        with open('/tmp/m122_eBill/receipts/' + filename, 'wb') as file:
            ftp.retrbinary('RETR ' + filename, file.write)
        ftp.delete(filename)
        receipt_count = receipt_count + 1
    ftp.quit()
    return receipt_count

def get_receipt_filenames():
    ftp_receipts = []
    ftp = get_ftp_connection()
    def list_callback(data):
        ftp_receipts.append(data)
    ftp.dir(list_callback)
    ftp.quit()

    def filter_invoices(receipt):
        if (re.match('^.+quittungsfile.+.txt$', receipt)):
            return True
        else:
            return False
    receipt_filter = filter(filter_invoices, ftp_receipts)
    filtered_receipts = []
    for receipt in receipt_filter:
        filtered_receipts.append(receipt)

    return filtered_receipts

def get_ftp_connection():
    ftp = FTP(host='134.119.225.245', user='310721-297-zahlsystem', passwd='Berufsschule8005!')
    ftp.cwd('out/AP18dHueppi')
    return ftp