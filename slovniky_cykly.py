product_stock = {
    'Apple_iPhone 12': 30,
    'Apple_MacBook Air': 20,
    'Apple_AirPods Pro': 50,
    'Samsung_Galaxy S21': 40,
    'Samsung_Galaxy Tab S7': 25,
}

def count_vendor_sales(data, vendor):
    total = 0
    for key, value in data.items():
        if vendor in key:
            total += value
    return total
print(count_vendor_sales(product_stock, "Apple"))