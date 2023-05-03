__author__ = 'InfSub'
__contact__ = "ADmin@TkYD.ru"
__copyright__ = "Copyright 2023, [LegioNTeaM]"
__date__ = "2023/04/26"
__deprecated__ = False
__email__ = "ADmin@TkYD.ru"
__maintainer__ = "InfSub"
__status__ = "Development"
__version__ = "0.0.1"


import sqlite3


class Database:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def add_queue(self, *args):
        # db = 'Discount'
        db_table = 'Cash'
        table_columns = (
            'Date_Year', 'Date_Month', 'Date_Day', 'Date_Time_Hours', 'Date_Time_Minutes', 'Discount_Card_Shop_Code',
            'Discount_Card_Number', 'Cash_Receipt', 'Item_Number',  'Quantity_of_Goods', 'Price', 'Sum', 'Discount',
            'Amount_Including_Discount', 'Written_off_Bonuses', 'Amount_Including_Bonus_Discounts', 'Bonuses_Accrued'
        )
        count_table_columns = len(table_columns)

        if len(*args) == count_table_columns:
            with self.connection:
                return self.cursor.execute(
                    f"INSERT INTO {db_table} ({', '.join([value for value in table_columns])}) "
                    f"VALUES ({', '.join('?' for _ in range(count_table_columns))})", *args
                )

    def select_queue(self, column_id):
        # db = 'Discount'
        db_table = 'Cash'
        with self.connection:
            selected = self.cursor.execute(
                f"SELECT * FROM {db_table} WHERE id = ?", column_id
            )
            return [row for row in selected]


'''
CREATE TABLE Cash (
    ID                               INTEGER      NOT NULL
                                                  PRIMARY KEY AUTOINCREMENT
                                                  UNIQUE,
    Date_Year                        INTEGER (4)  NOT NULL,
    Date_Month                       INTEGER (2)  NOT NULL,
    Date_Day                         INTEGER (2)  NOT NULL,
    Date_Time_Hours                  INTEGER (2)  NOT NULL,
    Date_Time_Minutes                INTEGER (2)  NOT NULL,
    Discount_Card_Shop_Code          INTEGER (3)  NOT NULL,
    Discount_Card_Number             INTEGER (8)  NOT NULL,
    Cash_Receipt                     INTEGER (4)  NOT NULL,
    Item_Number                      INTEGER (13) NOT NULL,
    Quantity_of_Goods                REAL (4, 2),
    Price                            REAL (5, 2),
    Sum                              REAL (6, 2),
    Discount                         REAL (2, 2),
    Amount_Including_Discount        REAL (6, 2),
    Written_off_Bonuses              REAL (6, 2),
    Amount_Including_Bonus_Discounts REAL (6, 2),
    Bonuses_Accrued                  REAL (6, 2),
    UNIQUE (
        Date_Year,
        Date_Month,
        Date_Day,
        Cash_Receipt,
        Item_Number
    )
);
'''

if __name__ == '__main__':
    test_db = Database('Discount.sqlite')
    arguments = tuple('1' for _ in range(17))
    print(arguments)
    print(test_db.add_queue(arguments))
    print(test_db.select_queue('1'))

