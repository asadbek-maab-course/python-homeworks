#!/bin/bash

output_file="combined.py"
folder="homework"

# combined.py faylini bo'shatish
> "$output_file"

# .py fayllarni topib, nomini alifbo bo'yicha saralash
find "$folder" -maxdepth 1 -name "*.py" | sort | while read file; do
    filename=$(basename "$file")
    echo "# $filename" >> "$output_file"
    cat "$file" >> "$output_file"
    echo -e "\n" >> "$output_file"
done
