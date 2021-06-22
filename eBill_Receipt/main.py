import banking_system_client

receipts = banking_system_client.download_receipts()
if (receipts == 0):
    raise Exception('Es wurden keine neuen Quittungen gefunden!')