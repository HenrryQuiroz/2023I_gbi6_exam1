
find ./exam1/data/singlecell -type f \( -name "*.csv" -o -name "*.txt" -o -name "*.tsv" -o -name "*.gz" -o -name "*.png" \) | grep -E -o '\.[a-zA-Z0-9]+$' | sort | uniq -c > extensiones.txt
