__author__ = 'InfSub'
__contact__ = "ADmin@TkYD.ru"
__copyright__ = "Copyright 2023, [LegioNTeaM]"
__date__ = "2023/05/03"
__deprecated__ = False
__email__ = "ADmin@TkYD.ru"
__maintainer__ = "InfSub"
__status__ = "Development"
__version__ = "0.0.2"


import config
import model
import view
# from database import Database


def controller(DEBUG: bool = False) -> None:
    """
    Program operation controller.
    :param DEBUG: True | False debug mode
    :return: None
    """
    # db = Database(config.SQL_LITE_DB_FILE)
    # db.add_queue(arguments)

    all_file_path = model.get_all_dsc_file(file_template=f'{config.CSV_FILE_NAME}*{config.CSV_FILE_EXCEPTION}')

    # for path in all_file_path:
    #     data = model.get_data_from_file(path, config.CSV_DELIMITER, config.CSV_ENCODE)
    #     print(f'LEN: {len(data)}\t{type(data)}\t{path}')

    # data = [model.get_data_from_file(path, config.CSV_DELIMITER, config.CSV_ENCODE) for path in all_file_path]

    # print(f'LEN data[0]: {len(data[0])}\t{type(data)}')
    # print(f'LEN data[1]: {len(data[1])}\t{type(data)}')

    # combined_list = [list_one, list_two]

    list_data = [
        i for sublist in
        [model.get_data_from_file(path, config.CSV_DELIMITER, config.CSV_ENCODE) for path in all_file_path]
        for i in sublist
    ]

    print(f'LEN list_merged: {len(list_data)}\t{type(list_data)}')
    # print(f'{list_merged}')

    # model.get_data_from_file(config.CSV_FILE, config.CSV_DELIMITER, config.CSV_ENCODE)


if __name__ == '__main__':
    controller(DEBUG=False)
