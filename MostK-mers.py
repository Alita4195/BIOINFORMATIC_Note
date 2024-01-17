def FrequentWordsWithMismatches(seq, k, mismatch_num):
    frequent_patterns = set()
    count_dict = {}

    # Count occurrences of each pattern and store in count_dict
    for i in range(len(seq) - k + 1):
        pattern = seq[i : i + k]
        neighbors = Neighbors(pattern, mismatch_num)
        for neighbor in neighbors:
            count_dict[neighbor] = count_dict.get(neighbor, 0) + 1

    # Find the maximum count
    max_count = max(count_dict.values())

    # Add patterns with maximum count to frequent_patterns
    frequent_patterns.update(
        pattern for pattern, count in count_dict.items() if count == max_count
    )

    return list(frequent_patterns)


def Neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A", "C", "G", "T"}
    neighbors = set()
    suffix_neighbors = Neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if HammingDistance(pattern[1:], text) < d:
            for nucleotide in "ACGT":
                neighbors.add(nucleotide + text)
        else:
            neighbors.add(pattern[0] + text)
    return neighbors


def HammingDistance(seq1, seq2):
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))


seq_path = "/home/nina/Downloads/dataset_30278_9.txt"
with open(seq_path, "r") as file:
    seq = file.read()

k = 5
mismatch_num = 3

frequent_patterns = FrequentWordsWithMismatches(seq, k, mismatch_num)
print("Frequent Patterns with at most", mismatch_num, "mismatches:", frequent_patterns)
