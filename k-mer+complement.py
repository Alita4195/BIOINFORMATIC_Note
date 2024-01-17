def FrequentWordsWithMismatchesAndReverse(seq, k, mismatch_num):
    frequent_patterns = set()
    count_dict = {}

    # Count occurrences of each pattern and its reverse complement, store in count_dict
    for i in range(len(seq) - k + 1):
        pattern = seq[i : i + k]
        reverse_pattern = ReverseComplement(pattern)

        # Check the original pattern
        neighbors = Neighbors(pattern, mismatch_num)
        for neighbor in neighbors:
            count_dict[neighbor] = count_dict.get(neighbor, 0) + 1

        # Check the reverse complement
        reverse_neighbors = Neighbors(reverse_pattern, mismatch_num)
        for reverse_neighbor in reverse_neighbors:
            count_dict[reverse_neighbor] = count_dict.get(reverse_neighbor, 0) + 1

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


def ReverseComplement(seq):
    complement_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
    cleaned_seq = "".join(base for base in seq if base in "ACGT")
    return "".join(complement_dict[base] for base in reversed(cleaned_seq))


# Your sequence loading code
seq_path = "/home/nina/Downloads/dataset_30278_10.txt"
with open(seq_path, "r") as file:
    seq = file.read()

k = 5
mismatch_num = 2

frequent_patterns = FrequentWordsWithMismatchesAndReverse(seq, k, mismatch_num)
print(
    "Frequent Patterns with at most",
    mismatch_num,
    "mismatches and reverse complements:",
    frequent_patterns,
)
