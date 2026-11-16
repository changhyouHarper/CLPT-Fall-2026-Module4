# Module 4, Problem 3

# Define main() function 
def main():

	# Prompt the user to enter the total for a meal
	subtotal = float(input("Enter the total: $"))

	# Declare variable to store 15% amount
	tip_15 = subtotal * 0.15

	# Declare variable to store the total for 15% 
	total_15 = subtotal + tip_15

	# Declare variable to store 18% amount
	tip_18 = subtotal * 0.18

	# Declare variable to store the total for 18% 
	total_18 = subtotal + tip_18

	# Declare variable to store 20% amount
	tip_20 = subtotal * 0.20

	# Declare variable to store the total for 20% 
	total_20 = subtotal + tip_20

	# Display output back to user 
	print("\nWith 15% Tip: ")
	print(f"Total: {subtotal:.2f}")
	print(f"Tip: {tip_15:.2f}")
	print(f"Total with Tip: {total_15:.2f}")

	print("\nWith 18% Tip: ")
	print(f"Total: {subtotal:.2f}")
	print(f"Tip: {tip_18:.2f}")
	print(f"Total with Tip: {total_18:.2f}")

	print("\nWith 20% Tip: ")
	print(f"Total: {subtotal:.2f}")
	print(f"Tip: {tip_20:.2f}")
	print(f"Total with Tip: {total_20:.2f}")

# Call main() function
if __name__ == "__main__":
	main()

