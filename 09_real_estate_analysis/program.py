import csv
import os
import statistics

from Purchase import Purchase


def prin_header():
    print('-----------------------------')
    print(' REAL ESTATE DATA MINING APP')
    print('-----------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
    # with open(filename, 'r') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


def query_data(data):
    data.sort(key=lambda p: p.price)

    high_purchase = data[-1]
    print('high_purchase {:,}'.format(high_purchase.price))
    low_purchase = data[0]
    print('low_purchase {:,}'.format(low_purchase.price))

    ave_price = statistics.mean([p.price for p in data])
    print('ave_price {:,}'.format(ave_price))

    ave_price_2_beds = statistics.mean([p.price for p in data if p.beds == 2])
    print('ave_price_2_beds {:,}'.format(ave_price_2_beds))

def main():
    prin_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)

if __name__ == '__main__':
    main()
