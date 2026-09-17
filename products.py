"""Define products and their inventory behavior."""


class Product:
    """Represent a product that can be purchased from inventory."""

    def __init__(
            self,
            name: str = "Product Name",
            price: float = 0.0,
            quantity: int = 0
        ) -> None:
        """Initialize a product with a name, price, and quantity."""
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity
        self.active: bool = True


    def get_quantity(self) -> int:
        """Return the product quantity."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Set the product quantity.

        If quantity reaches 0, deactivates the product.
        """
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return whether the product is active."""
        return self.active

    def activate(self) -> None:
        """Activate the product."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivate the product."""
        self.active = False

    def show(self) -> None:
        """Print a string that represents the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """Buy a given quantity of the product.

        * Return the total price of the purchase.
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



