from itertools import permutations


def solve_cryptarithmetic(puzzle):
    unique_letters = set(letter for word in puzzle for letter in word)
    if len(unique_letters) > 10:
        return None  # There are more than 10 letters, so no valid solution

    for digits in permutations(range(10), len(unique_letters)):
        digit_mapping = dict(zip(unique_letters, digits))

        if all(digit_mapping[word[0]] != 0 for word in puzzle):  # Check for leading zeros
            send = int(''.join(str(digit_mapping[letter]) for letter in puzzle[0]))
            more = int(''.join(str(digit_mapping[letter]) for letter in puzzle[1]))
            money = int(''.join(str(digit_mapping[letter]) for letter in puzzle[2]))

            if send + more == money:
                return digit_mapping

    return None  # No solution found


# Puzzle: SEND + MORE = MONEY
# puzzle=list(map(str,input().split()))
puzzle = ["send", "more", "money"]
solution = solve_cryptarithmetic(puzzle)

if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")


