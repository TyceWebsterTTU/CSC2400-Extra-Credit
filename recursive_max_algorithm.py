
def recursive_max_algorithm(S, n, depth=0):
    indent = "    " * depth
    print(f"{indent}Called recursive_max_algorithm(S, n={n})")

    if n == 1:
        print(f"{indent}Base case reached: returning {S[0]}")
        return S[0]
    else:
        print(f"{indent}Decreasing problem: calling recursive_max_algorithm(S, n={n - 1})")
        max_of_rest = recursive_max_algorithm(S, n - 1, depth + 1)

        print(f"{indent}Conquering: comparing max_of_rest = {max_of_rest} and S[{n - 1}] = {S[n - 1]}")
        result = max_of_rest if max_of_rest > S[n - 1] else S[n - 1]

        print(f"{indent}Returning result: {result}")
        return result
    
if __name__ == "__main__":
    S = [3, 5, 2, 9, 1, 8, 0, 2]
    print(f"Input: {S}\n")

    max = recursive_max_algorithm(S, len(S))
    print(f"\nThe maximum value in the list is: {max}")