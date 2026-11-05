from tools_dna import fasta_validate, dna_to_rna, len_dna, count_base, base_per, gc_content, rev_comp
dna=input("enter your fasta file path: ")
with open(dna,"r") as f:
	data=f.read()
if fasta_validate(data)==True:
	seq="".join(data.splitlines()[1:]).strip()
	header=data.splitlines()[0]
	print("header is: ",header)
	print("length: ",len_dna(seq))
	print("count of bases are: \n",count_base(seq))
	print("percentage of bases are: \n",base_per(seq))
	print("gc content: ",gc_content(seq))
	print("reverse complement is: ",rev_comp(seq))
	print("RNA sequence is: ",dna_to_rna(seq))
	
