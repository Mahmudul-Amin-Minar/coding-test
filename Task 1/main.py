def get_aspected_index(two_pair_values, target_value):
    length = len(two_pair_values)

    for index in range(length):
        if sum(two_pair_values[index]) == target_value:
            return index
    return "No target value found"



if __name__ == "__main__":
    two_pair_values = [
        [1, 5],
        [9, -7],
        [0, 8],
        [6, 3],
        [4, 11],
        [14, 0],
        [8, 1],
        [4, 9],
    ]
    target_value = 9

    result = get_aspected_index(two_pair_values, target_value)
    print(result)