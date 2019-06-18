import csv
from context_ids import context_id

with open('lti_report_csv_17_Jun_2019_90620190617-7638-1e9se6n.csv', 'r') as f:
    csvreader = csv.DictReader(f)
    data = [x for x in csvreader]

print(data[0])
headers = list(data[0].keys())
print(len(data))
in_context  = [x for x in data if (int(x['context_id']) in context_id) and (x['tool_type_id'] != 'DoE_Markbook')]
for row in in_context:
    print(f"name: {row['tool_type_name']},\taccount: {row['account_name']},\tprivacy: {row['privacy_level']}")
print(len(in_context))

with open('deleted_ltis.csv','w') as f:
    csvwriter = csv.DictWriter(f, fieldnames=headers)
    csvwriter.writeheader()
    for row in in_context:
        csvwriter.writerow(row)