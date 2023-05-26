#!/bin/bash

# Ruta al archivo sites.csv
archivo_sites="C:\Users\crist\OneDrive\Documents\Bioinfo\2023I_gbi6_exam1/exam1/data/mahomes/sites.csv"

# Ruta al archivo pdb.csv para guardar las columnas separadas
archivo_pdb="C:\Users\crist\OneDrive\Documents\Bioinfo\2023I_gbi6_exam1/pdb.csv"

# Ruta al archivo pdb_count.csv para guardar los conteos de elementos únicos
archivo_pdb_count="C:\Users\crist\OneDrive\Documents\Bioinfo\2023I_gbi6_exam1/pdb_count.csv"

# Extraer las columnas "resName1", "PDB Classification" y "Uniprot Acc" del archivo sites.csv y guardarlas en pdb.csv
cut -d ',' -f 5,18,21 "$archivo_sites" > "$archivo_pdb"

# Calcular el conteo de elementos únicos en cada una de las columnas y guardar los resultados en pdb_count.csv
printf "resName1\n" >> "$archivo_pdb_count"
cut -d "," -f 5 "$archivo_sites" | sort | uniq -c | awk '{print $2","$1}' >> "$archivo_pdb_count"

printf "PDB Classification\n" >> "$archivo_pdb_count"
cut -d "," -f 18 "$archivo_sites" | sort | uniq -c | awk '{print $2","$1}' >> "$archivo_pdb_count"

printf "Uniprot Acc\n" >> "$archivo_pdb_count"
cut -d "," -f 21 "$archivo_sites" | sort | uniq -c | awk '{print $2","$1}' >> "$archivo_pdb_count"

echo "Proceso completado. Los resultados se han guardado en pdb.csv y pdb_count.csv."
