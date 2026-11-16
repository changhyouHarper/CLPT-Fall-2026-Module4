# Module 4, Problem 5

# Define main() function 
def main():

	# Prompt user to enter fixed costs 
	fixed_costs = float(input("Enter fixed costs: $"))

	# Prompt user to enter price per unit 
	price_per_unit = float(input("Enter price per unit: $"))

	# Prompt user to enter cost per unit 
	cost_per_unit = float(input("Enter cost per unit: $"))

	# Declare variable to store / calculate break-even point 
	breakeven = fixed_costs / (price_per_unit - cost_per_unit)

	# Display output back to user 
	print(f"\nFixed Costs: {fixed_costs:.2f}")
	print(f"Price Per Unit: {price_per_unit:.2f}")
	print(f"Cost Per Unit: {cost_per_unit:.2f}")
	print(f"Breakeven Point: {breakeven:.2f}")

# Call main() function
if __name__ == "__main__":
	main()