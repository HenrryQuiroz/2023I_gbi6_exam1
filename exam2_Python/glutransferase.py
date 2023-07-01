import csv
from Bio import Entrez, SeqIO
import matplotlib.pyplot as plt


def source(accession):
    Entrez.email = 'henrryquiroz0@gmail.com'
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'gb')
    handle.close()
    organism = record.annotations['organism']
    species = record.annotations['taxonomy']
    frequencies = {}
    for specie in species:
        if specie in frequencies:
            frequencies[specie] += 1
        else:
            frequencies[specie] = 1
        with open('results/source.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Organismo', 'Frequencia'])
        for specie, freq in frequencies.items():
            writer.writerow([specie, freq])
    print("Extracción de la fuente y frecuencia de organismos ha sido completada. Los resultados se guardaron en 'results/source.csv'.")

def sequences(accession):
    Entrez.email = 'henrryquiroz0@gmail.com'
    handle = Entrez.efetch(db='nucleotide', id=accession, rettype='gb', retmode='text')
    record = SeqIO.read(handle, 'gb')
    handle.close()
    dna_sequence = record.seq
    protein_sequence = dna_sequence.translate(to_stop=True)
    peptides = []
    current_peptide = ""
    for aa in protein_sequence:
        if aa == "M":
            current_peptide = "M"
        elif aa == "*":
            if current_peptide:
                peptides.append(current_peptide)
                current_peptide = ""
        elif current_peptide:
            current_peptide += aa
    peptide_data = []
    for peptide in peptides:
        analysis = ProteinAnalysis(peptide)
        molecular_weight = analysis.molecular_weight()
        instability_index = analysis.instability_index()
        peptide_data.append((peptide, molecular_weight, instability_index))
    with open('results/glupeptides.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Peptide', 'Molecular Weight', 'Instability Index'])
        for peptide, molecular_weight, instability_index in peptide_data:
            writer.writerow([peptide, molecular_weight, instability_index])
    mw_values = [data[1] for data in peptide_data]
    ii_values = [data[2] for data in peptide_data]
    plt.figure(figsize=(8, 6))
    plt.scatter(mw_values, sii_value, c='gren', s=50, alpha=0.7)
    plt.title('Peso molecular vs Índice de inestabilidad')
    plt.xlabel('Peso molecular')
    plt.ylabel('Índice de inestabilidad')
    plt.savefig('results/glupeptides.png')
    plt.close()
    print("Extracción y análisis de secuencias ha sido completada. Los resultados se guardaron en 'results/glupeptides.csv' y 'results/glupeptides.png'.")

