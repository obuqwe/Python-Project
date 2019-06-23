import os
import csv
import statistics

from data_types import *


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('----------------------------')
    print('REAL ESTATE DATA MINING APP')
    print('----------------------------')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases
        # header = fin.readline().strip()
        # reader = csv.reader(fin)

        # for row in reader:
        #     print(row)

# def load_file_basics(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('found header: ' + header)

#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             bed_count = line_data[4]
#             lines.append(line_data)

#         print(lines[:5])


def query_data(data):
    data.sort(key=lambda p: p.price)

    high_purchase = data[-1]
    print(f'The most expensive house {high_purchase.price}')

    low_purchase = data[0]
    print(f'The least expensive house is {low_purchase.price}')

    two_bed_homes = (
        p
        for p in data
        if announce(p, f'2-bedrooms, found {p.beds}') and p.beds == 2
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break 
        homes.append(h)

    ave_price = statistics.mean((announce(p.price, 'price') for p in homes))
    ave_baths = statistics.mean((p.baths for p in homes))
    ave_sqft = statistics.mean((p.sq__ft for p in homes))

    print(f'Average 2-bedrooms home is ${int(ave_price)}, baths={round(ave_baths, 1)}, sq ft={round(ave_sqft, 1)}')

def announce(item, msg):
    print(f'Pulling item {item} for {msg}')
    return item

if __name__ == "__main__":
    main()
