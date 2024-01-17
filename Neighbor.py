def Neighbors(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {"A", "C", "G", "T"}

    Neighborhood = set()
    SuffixNeighbors = Neighbors(Suffix(Pattern), d)

    for text in SuffixNeighbors:
        if HammingDistance(Suffix(Pattern), text) < d:
            for nucleotide in "ACGT":
                Neighborhood.add(nucleotide + text)
        else:
            Neighborhood.add(FirstSymbol(Pattern) + text)

    return Neighborhood


def Suffix(Pattern):
    return Pattern[1:]


def FirstSymbol(Pattern):
    return Pattern[0]


def HammingDistance(seq1, seq2):
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))  # 用于将多个可迭代对象合并成一个元组的迭代器。


# 对布尔值求和，最后就能知道有多少个元素不相同


# Example usage:
pattern = "GAGTCTGATAT"
d = 3
result = Neighbors(pattern, d)
print(" ".join(result))
