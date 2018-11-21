prices = [
    ("ice cream", 80),
    ("bike", 20000),
    ("water", 30),
]


sorted_by_price = sorted(prices, key=lambda x: x[1])
print(sorted_by_price)
# > [('water', 30), ('ice cream', 80), ('bike', 20000)]