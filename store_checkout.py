"""
Store checkout exercise (translated)
"""

PRODUCT_PRICES = {
    1: 0.50,
    2: 1.00,
    3: 4.00,
    5: 7.00,
    9: 8.00,
}


def main():
    """Run the interactive checkout loop and print totals."""
    quantities = {code: 0 for code in PRODUCT_PRICES}

    product_list = ", ".join(
        f"code {code} = ${price:.2f}" for code, price in PRODUCT_PRICES.items()
    )
    print(f"Welcome to Market X. Available products: {product_list}")

    while True:
        try:
            code = int(
                input(
                    "Enter the product code (0 to finish and show total): "
                )
            )
        except ValueError:
            print("Invalid input. Please enter a numeric code.")
            continue

        if code == 0:
            break

        if code not in PRODUCT_PRICES:
            print("Invalid code, please enter an existing product code.")
            continue

        try:
            qty = int(input("Enter the quantity for the selected product: "))
        except ValueError:
            print("Invalid quantity. Please enter an integer.")
            continue

        quantities[code] += qty

    # Print per-product totals
    total_items = 0
    total_value = 0.0
    for code, qty in quantities.items():
        price = PRODUCT_PRICES[code]
        value = price * qty
        print(f"Quantity code {code}: {qty}  value = ${value:.2f}")
        total_items += qty
        total_value += value

    print(f"Total purchase amount: ${total_value:.2f}")
    print(f"Total number of items purchased: {total_items}")


if __name__ == "__main__":
    main()
