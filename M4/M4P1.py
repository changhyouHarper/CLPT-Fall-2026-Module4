# Module 4, Problem 1

# Define main() function 
def main(): 

	# Prompt user to enter first exam score 
	score_1 = float(input("Enter the first exam score: "))

	# Prompt user to enter second exam score 
	score_2 = float(input("Enter the second exam score: ")) 

	# Declare variable to calculate total score 
	total_score = (score_1 * .60) + (score_2 * .40)

	# Display output back to user 
	print(f"Total: {total_score:.2f}")

# Call main() function
if __name__ == "__main__":
	main()