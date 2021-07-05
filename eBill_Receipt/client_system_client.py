from ftplib import FTP
import zipfile
import os

def upload_receipt_zip(filename):
    ftp = get_ftp_connection()
    remotefile = filename.split('/')[len(filename.split('/')) - 1]
    with open(filename, 'rb') as file:
        ftp.storbinary('STOR %s' % remotefile, file)
    return None

def get_ftp_connection():
    ftp = FTP(host='ftp.haraldmueller.ch',user='schoolerinvoices',passwd='Berufsschule8005!')
    ftp.cwd('in/AP18dHueppi')
    return ftp

def make_zip(invoice_filename, receipt_filename , invoice_nr):
    new_file = '/tmp/m122_eBill/zips/' + str(invoice_nr) + '.zip'
    zip = zipfile.ZipFile(new_file, 'w', zipfile.ZIP_DEFLATED)
    zip.write('/tmp/m122_eBill/six_files/' + invoice_filename, invoice_filename)
    zip.write('/tmp/m122_eBill/receipts/' + receipt_filename, receipt_filename)
    zip.close()
    if os.path.exists(invoice_filename):
        os.remove(invoice_filename)
    if os.path.exists(receipt_filename):
        os.remove(receipt_filename)
    return new_file