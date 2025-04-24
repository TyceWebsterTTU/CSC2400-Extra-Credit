"""
    Name: CSC-2400 Extra Credit Programming Assignment
    Author: Tyce Webster & Logan McDavid
    Filename: recursive_max_algorithm
    Purpose: Return maximum value in set S recursively.
    Sources: 
        Stack Overflow. "Python and f-strings explanation." Stack Overflow, 21 June 2018, 
        https://stackoverflow.com/questions/50455784/python-and-f-strings-explanation.
            — Used to better understand Python f-strings and syntax.

        OpenAI. ChatGPT. 
        https://chatgpt.com/.
            — Used to better understand Python recursion and output formatting.

        GeeksforGeeks. "pprint — Data Pretty Printer in Python." GeeksforGeeks, 
        https://www.geeksforgeeks.org/pprint-data-pretty-printer-python/.
            — Used to improve readability of console output.

        Bader, Dan. "Python time.sleep(): Add Time Delays to Your Code." Real Python, 
        https://realpython.com/python-sleep/.
        — Used to understand how to implement timed delays using time.sleep() in Python.
"""

"""
    To Run on Command Prompt Use this Following Command:
        - "c:/File Path/recursive_max_algorithm.py"
"""


"""
    Function: recursive_max_algorithm
    Parameters:
        S     - Set / List of numbers
        n     - Length or list or portion of list being considered 
        depth - Used for output
"""
# Import time module for dynamic output during the recursive process
import time

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
        time.sleep(0.5)  # Sleep for 0.5 second to simulate processing time
        max_of_rest = recursive_max_algorithm(S, n - 1, depth + 1)  # Call recursive_max_algorithm

        # Compare current max value with element in list S based on where function is in recursive call
        print(f"{indent}Conquering: comparing max_of_rest = {max_of_rest} and S[{n - 1}] = {S[n - 1]}")
        time.sleep(0.5)  # Sleep for 0.5 second to simulate processing time
        result = max_of_rest if max_of_rest > S[n - 1] else S[n - 1]  # Store larger value in result

        # Output current max value
        print(f"{indent}Returning result: {result}")
        time.sleep(0.5)  # Sleep for 0.5 second to simulate processing time
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