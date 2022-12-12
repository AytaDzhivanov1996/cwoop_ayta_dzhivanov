class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, *args, **kwargs):
        pass

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
    a = Product()

    def __init__(self):
        self.products = []

    def __bool__(self):
        """
        Проверяет есть ли товар в категории
        """
        for i in self.products:
            if self.a.title in i:
                return True
            else:
                return False

    def __len__(self):
        products_name = []
        """
        Возвращает количество наименований товаров, у которых есть наличие на складе
        """
        if self.a.count > 0:
            products_name.append(self.a.title)
        return len(products_name)
