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
    new_file = '/home/timon/workspace/m122/m122_LB2_EBill/tmp/zips/' + str(invoice_nr) + '.zip'
    zip = zipfile.ZipFile(new_file, 'w', zipfile.ZIP_DEFLATED)
    if (not invoice_filename == None):
        zip.write('/home/timon/workspace/m122/m122_LB2_EBill/tmp/six_files/' + str(invoice_filename), invoice_filename)
    if (not receipt_filename == None):
        zip.write('/home/timon/workspace/m122/m122_LB2_EBill/tmp/receipts/' + str(receipt_filename), receipt_filename)
    zip.close()
    if os.path.exists(invoice_filename):
        os.remove(invoice_filename)
    if os.path.exists(receipt_filename):
        os.remove(receipt_filename)
    return new_file