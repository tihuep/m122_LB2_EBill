import client_system_client
import csv_parser
import file_generator
import target_system_client
import os

invoices = client_system_client.download_invoices()
if (invoices == 0):
    raise Exception('Es wurden keine neuen Rechnungen gefunden!')

csv_data = []
csv_files = csv_parser.get_all_csv_files()
for file in csv_files:
    csv_data.append(csv_parser.parse_csv('/tmp/m122_eBill/invoices/' + file))
    if os.path.exists('/tmp/m122_eBill/invoices/' + file):
        os.remove('/tmp/m122_eBill/invoices/' + file)

for file in csv_data:
    f = open('/tmp/m122_eBill/inv_email.csv', 'a')
    f.write(file[0][0].split("_")[1] + ';' + file[1][7] + '\n')

    txt_file = file_generator.generate_txt(file)
    xml_file = file_generator.generate_xml(file)
    target_system_client.upload_files(txt_file, xml_file)