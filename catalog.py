from connector import Connector


class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, data_json):
        self.id = data_json.get('id')
        self.title = data_json.get('title')
        self.price = data_json.get('price')
        self.count = data_json.get('count')
        self.category = data_json.get('category')

    def __str__(self):
        return f'Продукт "{self.title}" с количеством на складе {self.count} с ценой {self.price} за кг'

    def __bool__(self):
        """
        Проверяет есть ли товар в наличии
        """

        if self.count > 0:
            print(f'товар есть в наличии ({self.count} шт.)')
            return True
        else:
            print('товара нет в наличии')
            return False

    def __len__(self):
        """
        Возвращает количество товара на складе
        """

        return self.count


class Category:
    id: int
    title: str
    description: str
    products: list

    def __init__(self, data_json):
        self.id = data_json.get('id')
        self.title = data_json.get('title')
        self.description = data_json.get('description')
        self.products = data_json.get('products')

    def __str__(self):
        return f'{self.title} - {self.id}'

    def __bool__(self):
        """
        Проверяет есть ли товар в категории
        """
        return bool(len(self.products))

    def __len__(self):
        products_name = []
        """
        Возвращает количество наименований товаров, у которых есть наличие на складе
        """
        for i in self.products:
            if i.count > 0:
                products_name.append(i.title)
        return len(products_name)


class Shop:
    """
    Класс для работы с магазином
    """

    # products: list
    # categories: list

    def __init__(self, *args, **kwargs):
        pass

    def get_categories(self):
        """
        Показать все категории пользователю в произвольном виде, главное, чтобы пользователь
        мог видеть идентификаторы (id) каждой категории
        """
        categories_connector = Connector('categories.json')
        categories_list = categories_connector.select({})
        for i in categories_list:
            k = Category(i)
            print(k)

    def get_products(self):
        """
        Запросить номер категории и вывести все товары, которые относятся к этой категории
        Обработать вариант отсутствия введенного номера
        """
        cat_number = input('Введите номер категории: ')

        while not cat_number.isdigit():
            cat_number = input('Введите НОМЕР категории, а не что-то другое: ')

        product_connector = Connector('products.json')
        products_list = product_connector.select({'category': int(cat_number)})
        for prod in products_list:
            prod_obj = Product(prod)
            print(prod_obj)

    def get_product(self):
        """
        Запросить ввод номера товара и вывести всю информацию по нему в произвольном виде
        Обработать вариант отсутствия введенного номера
        """
        prod_number = input('Введите номер товара: ')

        prod_connector = Connector('products.json')
        prod_list = prod_connector.select({'id': int(prod_number)})
        for p in prod_list:
            p_obj = Product(p)
            print(p_obj)


if __name__ == '__main__':
    my_shop = Shop()
    my_shop.get_product()
