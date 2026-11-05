def base_per(dna):
    A_count=dna.upper().count("A")
    T_count=dna.upper().count("T")
    G_count=dna.upper().count("G")
    C_count=dna.upper().count("C")
    per="%"
    A_per=round((A_count/len(dna))*100,2)
    T_per=round((T_count/len(dna))*100,2)
    G_per=round((G_count/len(dna))*100,2)
    C_per=round((C_count/len(dna))*100,2)
    return f"percentage of A is {A_per} {per}\npercentage of T is {T_per} {per}\npercentage of G is {G_per} {per}\npercentage of C is {C_per} {per}"
    
    