import json


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    def __init__(self, df):
        self.__data_file = df
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        """
        pass

    def insert(self, data):
        with open('df.json', 'r') as f:
            json.dump(data, f)
        return self.__data_file

    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        data_from_file = []
        with open(self.__data_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for d in data:
            for k, v in query.items():
                if d[k] == v:
                    data_from_file.append(d)
        return data_from_file



    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select
        """
        pass


if __name__ == '__main__':
    df = Connector('df.json')

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert(data_for_file)
    data_from_file = df.select({'id': 1})
    assert data_from_file == [data_for_file]

    df.delete(dict())
    data_from_file = df.select(dict())
    assert data_from_file == []
