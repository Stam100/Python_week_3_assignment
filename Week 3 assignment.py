def calculate_discount(price,discount_percent):
    if discount_percent >=20:
        return price*(100 - discount_percent)/100
    else: return price
price = float (input('Original price:'))
discount_percent = float (input('What is the discount percentage?'))


print("Final price:", calculate_discount(price, discount_percent))
