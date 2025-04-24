"""
    Name: CSC-2400 Extra Credit Programming Assignment
    Author: Tyce Webster & Logan McDavid
    Filename: recursive_max_algorithm
    Purpose: Return maximum value in 
        set S recursively.
    Sources: 
        https://stackoverflow.com/questions/50455784/python-and-f-strings-explanation
            - Used to better understand Python
        https://chatgpt.com/
            - Used to better understand Python
        https://www.geeksforgeeks.org/pprint-data-pretty-printer-python/
            - Used to improve readability of output
"""


"""
    Function: recursive_max_algorithm
    Parameters:
        S - Set / List of numbers
        n - Length or list or portion of list being considered
        depth - Used for output
"""
def recursive_max_algorithm(S, n, depth=0):
     # Indention for printing recursive process
    indent = "    " * depth
    
     # Display current size n of list S
    print(f"{indent}Called recursive_max_algorithm(S, n={n})") 

    # Base Case: One value left in set S
    if n == 1:
        # Return first element in S
        print(f"{indent}Base case reached: returning {S[0]}")
        return S[0]
    # Decrease size n of list S, recursively call, then put back out for conquering / return phase at end
    else:
        # Decrease size n in list S, and recursively call function 
        print(f"{indent}Decreasing problem: calling recursive_max_algorithm(S, n={n - 1})")
        max_of_rest = recursive_max_algorithm(S, n - 1, depth + 1)  # Call recursive_max_algorithm

        # Compare current max value with element in list S based on where function is in recursive call
        print(f"{indent}Conquering: comparing max_of_rest = {max_of_rest} and S[{n - 1}] = {S[n - 1]}")
        result = max_of_rest if max_of_rest > S[n - 1] else S[n - 1]  # Store larger value in result

        # Output current max value
        print(f"{indent}Returning result: {result}")
        return result
    
# Run main function where user can input list S
if __name__ == "__main__":
    # S = [3, 5, 2, 9, 1, 8, 0, 2]
    while True:
        # Prompt user to enter list of numbers
        user_input = input("Enter a list of numbers separated by commas: ")
        # Validate correct syntax, normalizing values with delimitor ,
        try:
            S = [int(x.strip()) for x in user_input.split(",")]
            break
        except ValueError:
            print("Invalid input. Please enter a list of numbers separated by commas.")
    
    print(f"Input: {S}\n")  # Output user input list S 

    # Initial function call, returning maximum value
    max = recursive_max_algorithm(S, len(S))
    
    # Print max value 
    print(f"\nThe maximum value in the list is: {max}")