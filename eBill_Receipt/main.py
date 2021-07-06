import banking_system_client
import receipt_handler
import client_system_client
import mail_client
import os

receipts = banking_system_client.download_receipts()
if (receipts == 0):
    raise Exception('Es wurden keine neuen Quittungen gefunden!')

invoices = receipt_handler.get_all_invoices_from_receipts()

for invoice in invoices:
    zip_filename = client_system_client.make_zip(invoice[2], invoice[1], invoice[0])
    client_system_client.upload_receipt_zip('/home/timon/workspace/m122/m122_LB2_EBill/tmp/zips/' + invoice[0] + '.zip')
    mail_client.send_email(invoice[3], zip_filename, invoice[0], invoice[4], invoice[5])
    if os.path.exists(zip_filename):
        os.remove(zip_filename)
    if os.path.exists('/home/timon/workspace/m122/m122_LB2_EBill/tmp/six_files/' + invoice[2]):
        os.remove('/home/timon/workspace/m122/m122_LB2_EBill/tmp/six_files/' + invoice[2])

for invoice in invoices:
    if os.path.exists('/home/timon/workspace/m122/m122_LB2_EBill/tmp/receipts/' + invoice[1]):
        os.remove('/home/timon/workspace/m122/m122_LB2_EBill/tmp/receipts/' + invoice[1])