# Module 4, Problem 2

# Define main() function 
def main(): 

	# Prompt the user to enter the purchase price per share 
	price_per_share = float(input("Enter the purchase price per share: $"))

	# Prompt the user to enter the current stock price 
	current_stock_price = float(input("Enter the current stock price: $"))

	# Promp the user to enter the quantity of the stock 
	quantity_stock = int(input("Enter the quantity of the stock: "))

	# Declare variable store / calculate vlaue of the stock 
	value = (current_stock_price - price_per_share) * quantity_stock

	# Display output back to user 
	print(f"Value: ${value:,.2f}")

# Call main() function
if __name__ == "__main__":
	main()