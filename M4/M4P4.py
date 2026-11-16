# Module 4, Problem 4

# Define main() function 
def main(): 

	# Prompt the user to enter their first name 
	first_name = input("Enter first name: ")

	# Propmt the user to enter number of steps walked in a day 
	steps_walked = int(input("Enter the total number of steps walked in a day: "))

	# Declare variable to store and calculate number of calories burned 
	calories_burned = steps_walked * 0.25

	# Display output back to user 
	print("\nFirst Name: " + first_name)
	print(f"Calories Burned: {calories_burned:.2f}")

# Call main() function
if __name__ == "__main__":
	main()