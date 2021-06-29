import banking_system_client
import receipt_handler
import client_system_client
import mail_client

receipts = banking_system_client.download_receipts()
if (receipts == 0):
    raise Exception('Es wurden keine neuen Quittungen gefunden!')

invoices = receipt_handler.get_all_invoices_from_receipts()

for invoice in invoices:
    zip_filename = client_system_client.make_zip(invoice[2], invoice[1], invoice[0])
    print(zip_filename)
    client_system_client.upload_receipt_zip('../tmp/zips/' + invoice[0] + '.zip')
    #send