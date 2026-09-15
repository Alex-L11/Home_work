import os
import pandas as pd
from typing import Any, Hashable


def get_fin_oper_csv(data_csv: str) -> list[dict[Hashable, Any]]:
    """ Принимает путь к файлу CSV и выдает список словарей с транзакциями """
    # папка где лежит проект
    base_dir = os.path.dirname(__file__)

    # поднимаемся в корень проекта
    project_root = os.path.dirname(base_dir)

    # собираем путь до файла целиком
    data_path = os.path.join(project_root, 'data', data_csv)
    if not os.path.exists(data_path):
        raise FileNotFoundError(f'Файл не найден: {data_csv}')
    try:
        trans_csv = pd.read_csv(data_path, sep=';')
        result = trans_csv.to_dict(orient='records')
        return result
    except ValueError:
        raise ValueError('Файл пустой или содержит некорректные данные')
