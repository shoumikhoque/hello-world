def char_mapping(char):
    return ord(char) - ord('A') + 1

def find_repeated_sequences(dna, k):
    dna_len=len(dna)
    if dna_len<k:
        return set()

    base=4
    hash_value=0
    hash_set=set()
    output=set()
    for i in range(dna_len-k+1):
        hash_value = get_hash(base, dna, hash_value, i, k)
        if hash_value in hash_set:
            output.add(dna[i:i+k])
        hash_set.add(hash_value)
    return output


def get_hash(base, dna, hash_value, i, k):
    if i == 0:
        for j in range(k):
            hash_value += char_mapping(dna[j]) * (base ** (k - j - 1))
    else:
        prev_hash_value = hash_value
        hash_value = (((prev_hash_value - char_mapping(dna[i - 1]) * (base ** (k - 1))) * base)
                      + char_mapping(dna[i + k - 1]))
    return hash_value


if __name__ == '__main__':
    inputs_string = ["AGACCTAGAC",]
    inputs_k = [3,]

    for i in range(len(inputs_k)):
        print(i + 1, ".\tInput Sequence: \'", inputs_string[i], "\'", sep="")
        print("\tk: ", inputs_k[i], sep="")
        print("\tRepeated Subsequence: ",
              find_repeated_sequences(inputs_string[i], inputs_k[i]))
        print("-" * 100)