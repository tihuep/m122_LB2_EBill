import client_system_client
import csv_parser

invoices = client_system_client.download_invoices()
if (invoices == 0):
    raise Exception('Es wurden keine neuen Rechnungen gefunden!')

csv_data = []
csv_files = csv_parser.get_all_csv_files()
for file in csv_files:
    csv_data.append(csv_parser.parse_csv('tmp/invoices/' + file))

for file in csv_data:
    for row in file:
        for value in row:
            continue