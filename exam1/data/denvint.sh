# Ruta de la carpeta donde se encuentran los archivos .csv
carpeta="C:\Users\crist\OneDrive\Documents\Bioinfo\2023I_gbi6_exam1\exam1\data\denvint"

# Cambiar al directorio de la carpeta
cd "$carpeta"

# Bucle for para recorrer los archivos .csv
for i in *.csv; do
  echo "Archivo: $i"
  
  echo "Filas:"
  head -n1 "$i" | grep -o "," | wc -l
  
  echo "Columnas:" #NF variable que cuenta en cada archivo
  awk -F"," '{print NF}' "$i" | sort -nu | tail -n1
  
  echo "-----------------------------"
done
