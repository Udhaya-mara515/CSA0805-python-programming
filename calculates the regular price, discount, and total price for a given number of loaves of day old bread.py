# Get number of loaves of day old bread from user
loaves = int(input("Enter number of loaves of day old bread: "))

# Calculate regular price
regular_price = loaves * 185

# Calculate discount
discount = regular_price * 0.6

# Calculate total price
total_price = regular_price - discount

# Display prices with two decimal places and aligned decimal points
print("Regular price: {:.2f} rupees".format(regular_price))
print("Discount: {:.2f} rupees".format(discount))
print("Total price: {:.2f} rupees".format(total_price))
