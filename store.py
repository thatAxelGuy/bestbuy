from products import Product


class Store:

    def __init__(self, products: list[Product]) -> None:
        self.products: list[Product] = products

    def add_products(self, product: Product) -> None:
        """
        Adds a product to the store.
        """
        self.products.append(product)

    def remove_products(self, product: Product) -> None:
        """
        Removes a product from store.
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns how many items are in the store in total.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> list[Product]:
        """
        Returns all products in the store that are active.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price