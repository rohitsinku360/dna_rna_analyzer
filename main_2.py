from tools_dna import fasta_validate, dna_to_rna
dna=input("enter your fasta file path: ")
with open(dna,"r") as f:
	data=f.read()
if fasta_validate(data)==True:
	seq="".join(data.splitlines()[1:]).strip()
	header=data.splitlines()[0]
	print("header is: ",header)
	print("dna sequence is: ",seq)
	print("RNA sequence is: ",dna_to_rna(seq))
	