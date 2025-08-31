def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying discount.
    If discount_percent >= 20, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt the user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    print(f"Final price: {final_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
