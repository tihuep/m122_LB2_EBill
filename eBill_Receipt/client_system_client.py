from ftplib import FTP
import zipfile

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
    new_file = '../tmp/zips/' + str(invoice_nr) + '.zip'
    zip = zipfile.ZipFile(new_file, 'w', zipfile.ZIP_DEFLATED)
    zip.write('../tmp/six_files/' + invoice_filename, invoice_filename)
    zip.write('../tmp/receipts/' + receipt_filename, receipt_filename)
    zip.close()
    return new_file