def all_permutations(rest,currPer,permutations = set()):
    # Base case: if the data has only one element, return a list containing a single-element list
    if len(rest) == 0:
        permutations.add(currPer);

    # Iterate over the data
    for i in range(len(rest)):
        # Extract the current element
        current = rest[i]
        # Remaining elements
        remaining = rest[:i] + rest[i+1:]
        # Generate all permutations of the remaining elements
        all_permutations(remaining,currPer+rest[i])
    return permutations

if __name__ == '__main__':
    s='cda'
    result=all_permutations(s,'')
    for i in sorted(result):
        print(i)