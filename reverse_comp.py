complement =[]
def rev_comp(dna):
	for i in dna:
		if i.upper()=="A":
			complement.append("T")
		elif i.upper()=="T":
			complement.append("A")
		elif i.upper()=="G":
			complement.append("C")
		elif i.upper()=="C":
			complement.append("G")
	comp=complement[::-1]
	reverse="".join(comp)
	return reverse




