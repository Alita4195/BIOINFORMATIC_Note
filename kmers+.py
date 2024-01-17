def FrequentWords(text, k):
    frequent_patterns = set()
    count_dict = {}

    # Count occurrences of each pattern and store in count_dict
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        count_dict[pattern] = count_dict.get(pattern, 0) + 1

    # Find the maximum count
    max_count = max(count_dict.values())

    # Add patterns with maximum count to frequent_patterns
    frequent_patterns.update(
        pattern for pattern, count in count_dict.items() if count == max_count
    )

    return list(frequent_patterns)


# Example
# text_example = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
text = "/home/nina/Downloads/dataset_30272_13.txt"  # Replace with the actual file path
with open(text, "r") as file:
    text_example = file.read()

k_example = 13
result = FrequentWords(text_example, k_example)

print(f"The most frequent {k_example}-mers in the given text are: {result}")
# more efficient way!
