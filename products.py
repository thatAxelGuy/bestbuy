class Product:

    def __init__(
            self,
            name: str = "Product Name",
            price: float = 0.0,
            quantity: int = 0
        ) -> None:
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity
        self.active: bool = True


    def get_quantity(self) -> int:
        """
        Getter function for quantity. Returns the quantity (int).
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Setter function for quantity.
        If quantity reaches 0, deactivates the product.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Getter function for active.
        Returns True if the product is active, otherwise False.
        """
        return self.active

    def activate(self) -> None:
        """ Activates the product. """
        self.active = True

    def deactivate(self) -> None:
        """ Deactivates the product. """
        self.active = False

    def show(self) -> None:
        """Prints a string that represents the product. """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        * Buys a given quantity of the product.
        * Returns the total price (float) of the purchase.
        * Updates the quantity of the product.
        * Raises an exception if amount bought would exceed
          available quantity or product is inactive.
        """
        if not self.is_active():
            raise Exception("Product is inactive.")

        if quantity > self.get_quantity():
            raise Exception("Not enough quantity available.")

        self.set_quantity(self.quantity - quantity)
        return self.price * quantity



