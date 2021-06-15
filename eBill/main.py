import client_system_client
import csv_parser
import file_generator

invoices = client_system_client.download_invoices()
if (invoices == 0):
    raise Exception('Es wurden keine neuen Rechnungen gefunden!')

csv_data = []
csv_files = csv_parser.get_all_csv_files()
for file in csv_files:
    csv_data.append(csv_parser.parse_csv('tmp/invoices/' + file))

for file in csv_data:
    txt_file = file_generator.generate_txt(file)
    xml_file = file_generator.generate_xml(file)
    target_system_client.upload_files(txt_file, xml_file)