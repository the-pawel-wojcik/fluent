import csv
from inplace import inplace

filename='sample.csv'

with inplace(filename, 'r', newline='', encoding='utf-8') as (infh, outfh):
    reader = csv.reader(infh)
    writer = csv.writer(outfh)

    for row in reader:
        row += ['new', 'columns']
        writer.writerow(row)

    # for row in reader:
    #     writer.writerow(row[:-2])
