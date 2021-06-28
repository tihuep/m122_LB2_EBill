from ftplib import FTP
import os

def upload_files(txt_file, xml_file):
    ftp = get_ftp_connection()
    remotefile = txt_file.split('/')[len(txt_file.split('/')) - 1]
    with open(txt_file, 'rb') as file:
        ftp.storbinary('STOR %s' % remotefile, file)
    if os.path.exists(txt_file):
        os.remove(txt_file)

    remotefile = xml_file.split('/')[len(xml_file.split('/')) - 1]
    with open(xml_file, 'rb') as file:
        ftp.storbinary('STOR %s' % remotefile, file)
    if os.path.exists(xml_file):
        os.remove(xml_file)


def get_ftp_connection():
    ftp = FTP(host='134.119.225.245', user='310721-297-zahlsystem', passwd='Berufsschule8005!')
    ftp.cwd('in/AP18dHueppi')
    return ftp