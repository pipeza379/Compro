rna = str(input("Enter RNA:"))
size = int(input("Left side is ('5' or '3'): "))
count = 0; find = False
f = "False"
dic = {"UUU": "Phenylalanine (Phe)", "UUC": "Phenylalanine (Phe)", "UUA": "Phenylalanine (Phe)", "UUG": "Phenylalanine (Phe)", "CUU": "Leucine (Leu)", "CUC": "Leucine (Leu)", 'CUA': "Leucine (Leu)", 'CUG': "Leucine (Leu)", "AUU": 'Isoleucine (Ile)', "AUC": 'Isoleucine (Ile)', 'AUA': 'Isoleucine (Ile)', "AUG": 'Isoleucine (Ile)', 'GUU': 'Valine (Val)', 'GUC': 'Valine (Val)', 'GUA': 'Valine (Val)', 'GUG': 'Valine (Val)', 'UCU': 'Serine (Ser)', 'UCC': 'Serine (Ser)', 'UCA': 'Serine (Ser)', 'UCG': 'Serine (Ser)', 'CCU': 'Proline (Pro)', 'CCC': 'Proline (Pro)', 'CCA': 'Proline (Pro)', 'CCG': 'Proline (Pro)', 'ACU': 'Threorine (Thr)', 'ACC': 'Threorine (Thr)', 'ACA': 'Threorine (Thr)', 'ACG': 'Threorine (Thr)', 'GCU': 'Alanine (Ala)', 'GCC': 'Alanine (Ala)', 'GCA': 'Alanine (Ala)', 'GCG': 'Alanine (Ala)', 'UAU': 'Tyrosine (Tyr)', 'UAC': 'Tyrosine (Tyr)', 'CAU': 'Histidine (His)', 'CAC': 'Histidine (His)', 'CAA': 'Glutamine (Gin)', 'CAC': 'Glutamine (Gin)', 'AAU': 'Asparagine (Asn)', 'AAC': 'Asparagine (Asn)', 'AAA': 'Lysine (Lys)', 'AAG': 'Lysine (Lys)',
'GAU': 'Aspartic acid (Asp)', 'GAC': 'Aspartic acid (Asp)', 'GAA': 'Glutamic acid (Glu)', 'GAG': 'Glutamic acid (Glu)', 'UGU': 'Cysteine (Cys)', 'UGC': 'Cysteine (Cys)', 'UGG': 'Tryptophan (Trp)', 'CGU': 'Arginine (Arg)', 'CGC': 'Arginine (Arg)', 'CGA': 'Arginine (Arg)', 'CGG': 'Arginine (Arg)', 'AGU': 'Serine (Ser)', 'AGC': 'Serine (Ser)', 'AGA': 'Arginine (Arg)', 'AGG': 'Arginine (Arg)', 'GGU': 'Glycine (Gly)', 'GGC': 'Glycine (Gly)', 'GGA': 'Glycine (Gly)', 'GGG': 'Glycine (Gly)'}
dic2= {'Phe': 0}
if size == 3:
  rna = rna[::-1]
for i in range(0, len(rna)):
  if rna[i:i+3] == "AUG":
    count += 1
    nub = i+3
    find = True
    break

for i in range(nub, len(rna), 3):
  if find == True:
    if rna[i:i+3] in dic.keys():
      a = dic.get((rna[i:i+3]), 0)

    if i+3 > len(rna):
      break
    count += 1
  if rna[i:i+3] == "UAA" or rna[i:i+3] == "UAG" or rna[i:i+3] == "UGA":
    f = "True"
    break
print(count)
print(f)
