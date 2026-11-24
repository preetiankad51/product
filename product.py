import sys
def product_details(product_id, name, quantity, price):
    return (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: Rs. {price:.2f}"
    )
# Taking input using command-line arguments
product_id = sys.argv[1]
name = sys.argv[2]
quantity = int(sys.argv[3])
price = float(sys.argv[4])
result = product_details(product_id, name, quantity, price)
print(result)

