def FrequencyTable(text, k):
    """Generate a frequency table for a given window of a string."""
    frequency_table = {}
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        frequency_table[pattern] = frequency_table.get(pattern, 0) + 1
    return frequency_table


def FindMostLikelyReplicationStart(genome, k, L, t):
    most_likely_starts = set()

    for i in range(len(genome) - L + 1):
        window = genome[i : i + L]
        freq_table = FrequencyTable(window, k)

        for pattern, count in freq_table.items():
            if count >= t:
                most_likely_starts.add(pattern)

    return most_likely_starts


# Example
genome_path = (
    "/home/nina/Downloads/dataset_30274_5.txt"  # Replace with the actual file path
)
with open(genome_path, "r") as file:
    genome = file.read()

k_value = 10
L_value = 100
t_value = 4

likely_starts = FindMostLikelyReplicationStart(genome, k_value, L_value, t_value)

print(f"The most likely replication start k-mers are: {list(likely_starts)}")
