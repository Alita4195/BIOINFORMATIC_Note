def skew(seq):
    skew_ori = 0
    skew_list = [skew_ori]

    for i in range(len(seq)):
        if seq[i] == "C":
            skew_ori -= 1
            skew_list.append(skew_ori)
        elif seq[i] == "G":
            skew_ori += 1
            skew_list.append(skew_ori)
        else:
            skew_ori += 0
            skew_list.append(skew_ori)
    min_value = min(skew_list)
    for index, value in enumerate(skew_list):
        if value == min_value:
            print(index)


# seq = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
seq_path = "/home/nina/Downloads/dataset_30277_10.txt"
with open(seq_path, "r") as file:
    seq = file.read()

skew(seq)
