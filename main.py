"""Command-line interface for managing Best Buy products and orders."""

from products import Product
from store import Store

BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = Store(product_list)


def validate_input() -> str:
    """Prompt until the user enters a valid main-menu selection."""
    selection = input("Please choose a number:\n")

    while selection not in ["1", "2", "3", "4"]:
        print("Invalid selection. Please choose a number between 1 and 4.")
        selection = input("Please choose a number:\n")

    return selection


def list_products(basket=None) -> list[Product]:
    """Display and return products with stock available for purchase.

    Parameters
    ----------
    basket : list, optional
        Products and quantities already selected for the current order.

    Returns
    -------
    list[Product]
        Products with remaining available stock.

    """
    products: list[Product] = best_buy.get_all_products()
    available_products = []

    for product in products:
        available_stock = product.quantity
        if basket is not None:
            for basket_product, basket_quantity in basket:
                if basket_product == product:
                    available_stock -= basket_quantity

        if available_stock > 0:
            available_products.append(product)
            print(
                f"{len(available_products)}. {product.name} Quantity: {available_stock}"
            )

    return available_products


def show_total_quantity() -> None:
    """Display the total quantity of products currently in the store."""
    print(f"Total amount of items in store: {best_buy.get_total_quantity()}")


def make_order() -> None:
    """Collect an order interactively and display its summary."""
    basket = []

    while True:
        print("\nAvailable items")
        print("-" * 6)
        products = list_products(basket)
        print("-" * 6)
        print("Type 'leave' if you want to cancel the order.")

        selection = input("Select a product #: \n")

        if selection.lower() == "leave":
            return

        if not selection.isdigit():
            print("Please enter a valid product number.")
            continue

        product_number = int(selection)

        if product_number < 1 or product_number > len(products):
            print("Please select a product from the list.")
            continue

        product = products[product_number - 1]
        available_stock = product.quantity
        for basket_product, basket_quantity in basket:
            if basket_product == product:
                available_stock -= basket_quantity

        if available_stock == 0:
            print(
                "You have already added all available stock of this "
                "product to your order."
            )
            continue

        print(f"{product.name} selected! Amount remaining: {available_stock}")

        while True:
            quantity = input("How many would you like to order?: ")
            if not quantity.isdigit():
                print("Please enter a valid quantity.")
                continue

            quantity = int(quantity)

            if quantity > available_stock:
                print(f"Sorry, only {available_stock} are available.")
                continue

            break

        basket.append((product, quantity))

        continue_order = input("Would you like to add another product? (y/n): ")

        if continue_order.lower() == "n":
            break

    total = best_buy.order(basket)

    print("\n" + "=" * 40)
    print("           ORDER SUMMARY")
    print("=" * 40)

    for index, (product, quantity) in enumerate(basket, start=1):
        item_total = product.price * quantity
        print(f"\n{index}. {product.name}")
        print(f"   ${product.price:,.2f} × {quantity} = ${item_total:,.2f}")

    print("\n" + "-" * 40)
    print(f"TOTAL: ${total:,.2f}")
    print("=" * 40)


def start() -> None:
    """Run the interactive Best Buy main menu."""
    while True:
        print("\n" + YELLOW + "=" * 40)
        print(BLUE + "              BEST BUY")
        print(YELLOW + "=" * 40 + RESET)

        print(BLUE + "1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit" + RESET)

        print(YELLOW + "-" * 40 + RESET)

        selection = validate_input()
        print("-" * 30)

        if selection == "1":
            list_products()
        elif selection == "2":
            show_total_quantity()
        elif selection == "3":
            make_order()
        elif selection == "4":
            print("Goodbye!")
            break


def main() -> None:
    """Start the Best Buy command-line application."""
    start()


if __name__ == "__main__":
    main()
