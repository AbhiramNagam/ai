
def is_valid_solution(mapping, puzzle):
    first_num = 0
    second_num = 0
    result_num = 0

    for char in puzzle[0]:
        first_num = first_num * 10 + mapping[char]
    for char in puzzle[1]:
        second_num = second_num * 10 + mapping[char]
    for char in puzzle[2]:
        result_num = result_num * 10 + mapping[char]

    return first_num + second_num == result_num


def solve_cryptarithmetic(puzzle):
    unique_chars = set(''.join(puzzle))
    if len(unique_chars) > 10:
        return None

    unique_chars = list(unique_chars)

    def backtrack(index, used_digits, mapping):
        if index == len(unique_chars):
            if is_valid_solution(mapping, puzzle):
                return mapping.copy()
            return None

        char = unique_chars[index]
        for digit in range(10):
            if digit not in used_digits:
                mapping[char] = digit
                used_digits.add(digit)
                result = backtrack(index + 1, used_digits, mapping)
                if result:
                    return result
                mapping[char] = -1
                used_digits.remove(digit)

        return None

    initial_mapping = {char: -1 for char in unique_chars}
    return backtrack(0, set(), initial_mapping)


# Example puzzle: SEND + MORE = MONEY
puzzle = ['SEND', 'MORE', 'MONEY']
solution = solve_cryptarithmetic(puzzle)

if solution:
    print("Valid Solution:")
    for char, digit in solution.items():
        print(f"{char}: {digit}")
else:
    print("No valid solution found.")
