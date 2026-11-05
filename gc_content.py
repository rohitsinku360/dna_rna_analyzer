def gc_content(dna):
    per="%"
    gc_per=round(((dna.upper().count("G")+dna.upper().count("C"))/len(dna))*100,2)        
    return f"{gc_per} {per}"
          
    