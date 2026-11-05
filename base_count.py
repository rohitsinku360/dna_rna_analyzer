def count_base(dna):
    A_count=dna.upper().count("A")
    T_count=dna.upper().count("T")
    G_count=dna.upper().count("G")
    C_count=dna.upper().count("C")
    return f"count of A is {A_count}\ncount of T is {T_count}\ncount of G is {G_count}\ncount of C is {C_count}"