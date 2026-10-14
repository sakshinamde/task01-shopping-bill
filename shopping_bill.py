def calculate_electronics_gst(a, b):
    subtotal = a + b
    return subtotal + subtotal * 0.18


def calculate_fashion_gst(c, d):
    subtotal = c + d
    return subtotal + subtotal * 0.13


def calculate_food_gst(e):
    return e + e * 0.07


def total_bill(a, b, c, d, e):
    return (calculate_electronics_gst(a, b)
            + calculate_fashion_gst(c, d)
            + calculate_food_gst(e))


def calculate_discounted_bill(a, b, c, d, e):
    total = total_bill(a, b, c, d, e)
    discount = total * 0.20
    return total - discount


if __name__ == "__main__":
    a, b, c, d, e = 100, 100, 100, 100, 100

    total = total_bill(a, b, c, d, e)
    discount = total * 0.20
    final_amount = calculate_discounted_bill(a, b, c, d, e)

    print(f"Electronics: ₹{calculate_electronics_gst(a, b):.2f}")
    print(f"Fashion: ₹{calculate_fashion_gst(c, d):.2f}")
    print(f"Food: ₹{calculate_food_gst(e):.2f}")
    print(f"Total after GST = ₹{total:.2f} | Discount = ₹{discount:.2f} | "
          f"Final payable amount = ₹{final_amount:.2f}")