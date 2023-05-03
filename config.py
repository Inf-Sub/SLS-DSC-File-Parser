__author__ = 'InfSub'
__contact__ = "ADmin@TkYD.ru"
__copyright__ = "Copyright 2023, [LegioNTeaM]"
__date__ = "2023/05/03"
__deprecated__ = False
__email__ = "ADmin@TkYD.ru"
__maintainer__ = "InfSub"
__status__ = "Development"
__version__ = "0.0.3"


from os.path import abspath, dirname, join


MAIN_DIR = abspath(dirname(__file__))

SLS_DIR = r'c:\Softland Systems'
# SLS_KASSA_DIR = join(MAIN_DIR, '..', 'SLS-Kacca')
SLS_KASSA_DIR = join(SLS_DIR, 'SLS-Kacca')

# CSV_DIR = abspath(dirname(SLS_KASSA_DIR))
CSV_DIR = SLS_KASSA_DIR
CSV_FILE_NAME = 'Kassa'
CSV_FILE_EXCEPTION = 'DSC'
CSV_FILE = join(CSV_DIR, f'{CSV_FILE_NAME}.{CSV_FILE_EXCEPTION}')


CSV_DELIMITER = '|'
CSV_ENCODE = 'utf-8'
CSV_AMOUNT_OF_ELEMENTS = 16

SQL_LITE_DB_FILE = join(MAIN_DIR, 'Discount.sqlite')

DEFAULT_LANGUAGE = 'ru'


if __name__ == '__main__':
    rn = '\n'
    print(
        f'MAIN_DIR: {MAIN_DIR}{rn}'
        f'SLS_KASSA_DIR: {SLS_KASSA_DIR}{rn}'
        f'CSV_DIR: {CSV_DIR}{rn}'
        f'CSV_FILE_NAME: {CSV_FILE_NAME}'
        f'CSV_FILE_EXCEPTION: {CSV_FILE_EXCEPTION}'
        f'CSV_FILE: {CSV_FILE}{rn}'
        f'CSV_DELIMITER: {CSV_DELIMITER}{rn}'
        f'CSV_ENCODE: {CSV_ENCODE}{rn}'
        f'SQL_LITE_DB_FILE: {SQL_LITE_DB_FILE}{rn}'
        f'DEFAULT_LANGUAGE: {DEFAULT_LANGUAGE}{rn}'
    )
