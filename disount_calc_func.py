# Calculate discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent/100)
        final_price = price - discount
    else:
        final_price = price

    return final_price

# Ask for users input
original_price = int(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

price = calculate_discount(original_price, discount_percentage)
print("The price of the item will be: ",price)
