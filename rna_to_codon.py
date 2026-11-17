def codon(rna_seq):
    cod=[]
    for i in range(0,len(rna_seq),3):
        if i+3>len(rna_seq):
            continue 
        else:
            cod.append(rna_seq[i:i+3])
    return cod
        
