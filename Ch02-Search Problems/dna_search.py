from enum import IntEnum

Nucleotide: IntEnum = IntEnum("Nucleotide", ("A", "C", "G", "T"))
# intenum has comparison operators

Codon = tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = list[Codon]


def valid_gene_str(s: str) -> bool:
    for char in s:
        if char not in list("ACGT"):
            return False
    return True


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    length = (
        len(s) - len(s) % 3
    )  # handling the case when the number of genes is not a multiple of three by stripping the last few genes
    s = s.upper()
    if not valid_gene_str(s):
        raise TypeError
    for i in range(0, length, 3):
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        # print(codon)
        gene.append(codon)

    return gene


def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False


# requires some kind of ordering
def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False


# another binary search using bisect

if __name__ == "__main__":
    gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGGTTTATATATATACCCTAGGACTCCCTTT"
    my_gene: Gene = string_to_gene(gene_str)
    acg: Codon = string_to_gene("ACG")[0]
    gat: Codon = string_to_gene("GAT")[0]
    print(linear_contains(my_gene, acg))
    print(linear_contains(my_gene, gat))
    print(binary_contains(sorted(my_gene), acg))
    print(binary_contains(sorted(my_gene), gat))
