import re
import datetime

def generate_txt(csv_data):
    template_file = open('templates/invoice_template.txt', 'r')
    Lines = template_file.readlines()

    output_file = open('tmp/six_files/' + csv_data[1][2] + '_' + csv_data[0][0].split('_')[1] + '_' + 'invoice.txt', 'w')
    for line in Lines:
        iterations = 1
        if (line.__contains__('pos')):
            iterations = len(csv_data) - 3
        for iteration in range(1, iterations + 1):
            new_line = line
            for _ in [m.start() for m in re.finditer('\{', str(line))]:
                var_start = new_line.find('{')
                var_end = new_line.find('}')
                old = new_line[var_start:var_end+1]
                var = new_line[var_start+1:var_end]
                new = get_value(csv_data, var, iteration, 'txt')
                new_line = new_line.replace(old, new, 1)
            output_file.write(new_line)
    output_file.close()

    return str(output_file.name)

def generate_xml(csv_data):
    csv_data[3][6] = 'MWST_5.40%'
    csv_data[4][6] = 'MWST_2.21%'
    template_file = open('templates/invoice_template.xml', 'r')
    Lines = template_file.readlines()

    output_file = open('tmp/six_files/' + csv_data[1][2] + '_' + csv_data[0][0].split('_')[1] + '_' + 'invoice.xml', 'w')
    for line in Lines:
        new_line = line
        for _ in [m.start() for m in re.finditer('\{', str(line))]:
            var_start = new_line.find('{')
            var_end = new_line.find('}')
            old = new_line[var_start:var_end+1]
            var = new_line[var_start+1:var_end]
            new = get_value(csv_data, var, None, 'xml')
            new_line = new_line.replace(old, new, 1)
        output_file.write(new_line)
    output_file.close()

    return str(output_file.name)

def get_value(csv_data, var_name, iteration, format):
    true_length = False
    right_just = False
    csv_records = len(csv_data)
    posCount = len(csv_data) - 3
    value = ''
    if var_name.strip() == 'sender_name':
        value = csv_data[1][3]
    elif var_name.strip() == 'sender_address':
        value = csv_data[1][4]
    elif var_name.strip() == 'sender_zip_and_city':
        value = csv_data[1][5]
    elif var_name.strip() == 'tax_no':
        value = csv_data[1][6]
    elif var_name.strip() == 'invoice_place':
        true_length = True
        value = csv_data[0][2] + ','
    elif var_name.strip() == 'invoice_date':
        true_length = True
        value = csv_data[0][3]
    elif var_name.strip() == 'receiver_name':
        value = csv_data[2][2]
    elif var_name.strip() == 'receiver_address':
        value = csv_data[2][3]
    elif var_name.strip() == 'receiver_zip_and_city':
        value = csv_data[2][4]
    elif var_name.strip() == 'client_nr':
        true_length = True
        right_just = True
        value = csv_data[1][2]
    elif var_name.strip() == 'order_nr':
        true_length = True
        right_just = True
        value = csv_data[0][1].split("_")[1]
    elif var_name.strip() == 'invoice_nr':
        true_length = True
        right_just = True
        value = csv_data[0][0].split("_")[1]
    elif var_name.strip() == 'pos_nr':
        true_length = True
        value = csv_data[2 + iteration][1]
    elif var_name.strip() == 'pos_description':
        true_length = True
        value = csv_data[2 + iteration][2]
    elif var_name.strip() == 'pos_amount':
        right_just = True
        true_length = True
        value = csv_data[2 + iteration][3]
    elif var_name.strip() == 'pos_single_sum':
        true_length = True
        value = csv_data[2 + iteration][4]
    elif var_name.strip() == 'curr':
        true_length = True
        value = "CHF"
    elif var_name.strip() == 'pos_sum':
        true_length = True
        right_just = True
        value = csv_data[2 + iteration][5]
    elif var_name.strip() == 'pos_mwst':
        true_length = True
        value = csv_data[2 + iteration][6]
    elif var_name.strip() == 'invoice_sum':
        true_length = True
        right_just = True
        sum = 0
        for i in range(csv_records - posCount, csv_records):
            sum = sum + float(csv_data[i][5])
        value = str(sum)
    elif var_name.strip() == 'invoice_mwst':
        true_length = True
        right_just = True
        mwst = 0
        for i in range(csv_records - posCount, csv_records):
            mwst = mwst + float(float(csv_data[i][6].split("_")[1].rstrip("%"))/100 * float(csv_data[i][5]))
        value = str(mwst)
    elif var_name.strip() == 'payment_limit_days':
        value = csv_data[0][5].split("_")[1]
    elif var_name.strip() == 'payment_date_limit':
        days = int(csv_data[0][5].split("_")[1])
        date = datetime.datetime.strptime(csv_data[0][3], '%d.%m.%Y')
        date_limit = date + datetime.timedelta(days=days)
        value = date_limit.date().__format__('%d.%m.%Y')
    elif var_name.strip() == 'receiver_account_nr':
        true_length = True
        value = '0 00000 00000 00000'
    elif var_name.strip() == 'pid_sender':
        value = csv_data[1][1]
    elif var_name.strip() == 'pid_receiver':
        value = csv_data[2][1]
    elif var_name.strip() == 'xml_date':
        date = datetime.datetime.strptime(csv_data[0][3], '%d.%m.%Y')
        value = date.date().__format__('%Y%m%d')
    elif var_name.strip() == 'invoice_date_day':
        date = datetime.datetime.strptime(csv_data[0][3], '%d.%m.%Y')
        value = date.date().__format__('%d')
    elif var_name.strip() == 'reference_nr':
        date = datetime.datetime.now(datetime.timezone(datetime.timedelta(0, 0, 0, 0, 0, 1)))
        value = date.date().__format__('%Y%m%d') + csv_data[0][0].split("_")[1] + csv_data[0][1].split("_")[1]
    if (true_length and format == 'txt'):
        if (len(var_name) + 2 > len(value)):
            for _ in range(0, len(var_name) + 2 - len(value)):
                if (right_just):
                    value = ' ' + value
                else:
                    value = value + ' '
    return value