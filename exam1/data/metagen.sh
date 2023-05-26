#!/bin/bash

# Ruta al archivo infants_metagenome.txt
archivo_infants_metagenome="C:\Users\crist\OneDrive\Documents\Bioinfo\2023I_gbi6_exam1/exam1/data/metagen/infants_metagenome.txt"

# Ruta al archivo mygenomemap.sam
archivo_mygenomemap="C:\Users\crist\OneDrive\Documents\Bioinfo\2023I_gbi6_exam1/exam1/data/metagen/mygenomemap.sam"

# Ruta al archivo gata.txt para guardar los fragmentos de interés encontrados
archivo_gata="C:\Users\crist\OneDrive\Documents\Bioinfo\2023I_gbi6_exam1/gata.txt"

# Analizar el archivo infants_metagenome.txt para contar los registros hasta el nivel de especies
registros_especies=$(grep -c -E "^([^|]+[|]){3}[^|]+$" "$archivo_infants_metagenome")
echo "Número de registros hasta el nivel de especies: $registros_especies"

# Realizar la búsqueda de fragmentos de interés (TATA, GAGA, GATA) en el archivo mygenomemap.sam y guardarlos en gata.txt
grep -E "TATA|GAGA|GATA" "$archivo_mygenomemap" > "$archivo_gata"

echo "Proceso completado. Los resultados se han guardado en gata.txt."
