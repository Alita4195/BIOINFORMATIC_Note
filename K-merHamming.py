def maxmatch_pos(pattern, seq, mismatch_num):
    result = []
    for i in range(len(seq) - len(pattern) + 1):
        count = 0
        window = seq[i : i + len(pattern)]

        for j in range(len(window)):
            if window[j] != pattern[j]:
                count += 1

        if count <= mismatch_num:
            result.append(i)
    print(len(result))
    #         result.append(
    #             str(i)
    #         )  # Convert the position to a string and append to result:为了提交答案之便

    # print(" ".join(result))  # Use join to print positions separated by spaces


pattern = "AAGCTC"
# seq = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
mismatch_num = 2


seq_path = (
    "/home/nina/Downloads/dataset_30278_6.txt"  # Replace with the actual file path
)
with open(seq_path, "r") as file:
    seq = file.read()

maxmatch_pos(pattern, seq, mismatch_num)
