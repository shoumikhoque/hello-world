def find_symmetric(pairs):
    lookup=set()
    result=[]
    for pair in pairs:
        current_pair=tuple(pair)
        pair.reverse()
        reverse_pair=tuple(pair)
        if reverse_pair in lookup:
            result.append(current_pair)
            result.append(reverse_pair)
        else:
            lookup.add(current_pair)
    return result


if __name__ == '__main__':
    test_cases = [
        [[1, 2], [4, 6], [4, 3], [6, 4], [5, 9], [3, 4], [9, 5]],
        [[1, 2], [2, 1], [3, 4], [5, 5], [6, 7]],
        [[1, 9], [9, 1]],
        [[1, 2], [3, 4], [5, 6]],
        [[-8, -4], [7, 7], [1, 1], [2, 2], [-4, -8]]
    ]
    i = 1
    for case in test_cases:
        print(i, ".\tInput list: ", case, sep="")
        symmetric = find_symmetric(case)
        print("\n\tSymmetric pairs: ", symmetric)
        print("-" * 100)
        i += 1