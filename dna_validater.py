def fasta_validate(data):
	sequence ={"A","T","G","C"}
	if len(data)==0:
		print("empty file!")
		return False
	elif len(data)>0:
		header=data.splitlines()[0]
		seq="".join(data.splitlines()[1:]).strip()
		if len(header)==0:
			print("invalid header!")
			return False
		elif ">" not in header:
			print("invalid header starter!")
			return False
		elif len(seq)==0:
			print("sequence not found !")
			return False
	for i in seq:
		if i.upper() not in sequence:
			print("invalid sequence!")
			return False
	return True
			
			
			
	
	
	
			
		
		