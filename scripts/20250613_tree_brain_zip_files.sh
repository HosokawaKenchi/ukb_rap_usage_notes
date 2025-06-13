#!/bin/bash

SEARCH_DIR="/mnt/project/Bulk/Brain MRI/Surface-based analysis of resting and task fMRI"
OUTPUT_DIR="./docs/tree"
PYTHON_SCRIPT="./tree_zip.py"

# ASL
# Connectomes
# dMRI
# Functional time series
# Native atlases
# Native atlases (Diffusion)
# Native atlases (Structural and functional)
# rfMRI
# Scout
# Surface-based analysis of resting and task fMRI

# find コマンドの出力を改行区切りで読み込み、配列に格納
zip_files=()
while IFS= read -r line; do
    zip_files+=("$line")
done < <(find "${SEARCH_DIR}" -type f -name "*.zip")

for zip_file in "${zip_files[@]}";
do
    python ${PYTHON_SCRIPT} --input_file "${zip_file}" --output_dir "${OUTPUT_DIR}"
done
