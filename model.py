__author__ = 'InfSub'
__contact__ = "ADmin@TkYD.ru"
__copyright__ = "Copyright 2023, [LegioNTeaM]"
__date__ = "2023/05/03"
__deprecated__ = False
__email__ = "ADmin@TkYD.ru"
__maintainer__ = "InfSub"
__status__ = "Development"
__version__ = "0.0.2"

# import pprint
import os
# from os.path import join
import glob
from datetime import datetime
# import re

import config


def get_all_dsc_file(
        path: str = config.CSV_DIR,
        file_template: str = f'{config.CSV_FILE_NAME}.{config.CSV_FILE_EXCEPTION}'
) -> list:
    return glob.glob(f"{path}/{file_template}")


def get_data_from_file(
        path: str = config.CSV_FILE,
        delimiter: str = config.CSV_DELIMITER,
        encode: str = config.CSV_ENCODE
) -> list:
    """
    Getting data from a file.
    :param path: path to database file
    :param delimiter: separator in csv file
    :param encode: file encoding
    :return: returns a list of dictionaries with data
    """
    if not file_exists(path):
        return []
    with open(path, "r", encoding=encode) as file:
        # data = [el.strip().split(delimiter) for key, el in enumerate(file) if key > 0]
        # for el in file:
        #     print(f'{el.count(delimiter)}')

        db = [
            {
                'sale_timestamp': convert_datetime(f'{sale_date}{sale_time}'),
                'discount_card': int(discount_card),
                'discount_card_shop_code': int(discount_card[2:5]),
                'discount_card_number': int(discount_card[5:]),
                'cash_receipt': int(cash_receipt),
                'item_number': int(item_number),
                'quantity_of_goods': float(quantity_of_goods),
                'price': float(price),
                'sale_sum': float(sale_sum),
                'discount': float(discount),
                'amount_including_discount': float(amount_including_discount),
                'written_off_bonuses': float(written_off_bonuses),
                'amount_including_bonus_discounts': float(amount_including_bonus_discounts),
                'bonuses_accrued': float(bonuses_accrued)
            }
            for string_element in file if string_element.count(delimiter) == config.CSV_AMOUNT_OF_ELEMENTS
            for sale_date, sale_time, discount_card, cash_receipt, item_number, _, _,
            quantity_of_goods, price, sale_sum, discount, amount_including_discount, _,
            written_off_bonuses, amount_including_bonus_discounts, bonuses_accrued, _
            in [string_element.strip().split(delimiter)]
        ]

    return db


def file_exists(path: str) -> bool:
    """
    Check if file exists.
    :param path: full path to a file
    :return: True | False
    """
    return os.path.exists(path)


def convert_datetime(dt: str) -> int:
    """
    Let's convert the date and time format from the 'Kassa.DSC' file to a unix timestamp.
    :param dt: date and time (format: '%Y%m%d%H%M')
    :return: unix timestamp (seconds)
    """
    dt = dt.replace(';', '201')
    dt = dt.replace('<', '202')

    if dt[-2:] == '60':
        hours = str(int(dt[-4:-2]) + 1)
        minutes = '00'
        dt = dt.replace(dt[-4:], f'{hours}{minutes}')
    return int(datetime.strptime(dt, '%Y%m%d%H%M').timestamp())


if __name__ == '__main__':
    print(config.CSV_FILE, config.CSV_DELIMITER, config.CSV_ENCODE, sep="\n")
    print(f'file_exists: {file_exists(config.CSV_FILE)}')
    test_db = get_data_from_file()
    print(f'LEN: {len(test_db)}')

    # pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
    # pp.pprint(test_db)
    # print(datetime.fromtimestamp(test_db[450]['sale_timestamp']))
    # print(f"{test_db[450]['discount_card']}")
    # print(f"{test_db[450]['discount_card'][2:5]}")
    # print(f"{test_db[450]['discount_card'][5:]}")
    # pp.pprint(test_db[450])
    print(test_db[450])


