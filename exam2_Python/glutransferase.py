import csv
from Bio import Entrez, SeqIO

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

