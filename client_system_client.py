from ftplib import FTP
import re

def download_invoices():
    invoices = get_invoice_filenames()
    ftp = getFTPConnection()
    for invoice in invoices:
        filename = invoice[63:len(invoice)]
        with open('tmp/invoices/' + filename + '.csv', 'wb') as file:
            ftp.retrbinary('RETR ' + filename, file.write)
        ftp.delete(filename)
    ftp.quit()

def get_invoice_filenames():
    ftp_invoices = []
    ftp = getFTPConnection()
    def list_callback(data):
        ftp_invoices.append(data)
    ftp.dir(list_callback)
    ftp.quit()

    def filter_invoices(invoice):
        if (re.match('^.+rechnung.+.data$', invoice)):
            return True
        else:
            return False
    invoice_filter = filter(filter_invoices, ftp_invoices)
    filtered_invoices = []
    for invoice in invoice_filter:
        filtered_invoices.append(invoice)

    return filtered_invoices

def getFTPConnection():
    ftp = FTP(host='ftp.haraldmueller.ch',user='schoolerinvoices',passwd='Berufsschule8005!')
    ftp.cwd('out/AP18dHueppi')
    return ftp