import pandas as pd
import re
from pathlib import Path

#=-=-=-SETTINGS=-=-=-=-=-=-=-=-=-=-
input_file = "help/all_resultsCHOTHIA_H.csv"
output_file = "all_resultsCHOTHIA_H3.csv"
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def is_chothia_h3_position(col):
    """
    Chothia CDR-H3 = positions 95 to 102,
    including insertions like 100A, 100B, 100C...
    """
    col = str(col).strip()

    match = re.fullmatch(r"(\d+)([A-Z]?)", col)
    if not match:
        return False
    


    number = int(match.group(1))
    return 95 <= number <= 102

def clean_residue(x):
    if pd.isna(x):
        return ""

    x = str(x).strip()

    if x in ["-", ""]:
        return ""

    return x


# Make sure file exists
path = Path(input_file)

if not path.exists():
    raise FileNotFoundError(f"Cannot find input file: {path.resolve()}")


# Read CSV
df = pd.read_csv(path, sep=None, engine="python")

print("Rows loaded:", len(df))
print("Columns loaded:", len(df.columns))
print("First 20 columns:", list(df.columns[:20]))


# Detect Chothia H3 columns
h3_cols = [col for col in df.columns if is_chothia_h3_position(col)]

print("Detected H3 columns:", h3_cols)

if not h3_cols:
    raise ValueError("NO H3 COLUMNS DETECTED. Column names may be weird.")


# Extract H3
all_outputs = []

for _, row in df.iterrows():
    residues = [clean_residue(row[col]) for col in h3_cols]
    cdrh3 = "".join(residues)

    all_outputs.append({
        "Id": row.get("Id", ""),
        "hmm_species": row.get("hmm_species", ""),
        "chain_type": row.get("chain_type", ""),
        "e-value": row.get("e-value", ""),
        "score": row.get("score", ""),
        "seqstart_index": row.get("seqstart_index", ""),
        "seqend_index": row.get("seqend_index", ""),
        "cdrh3_chothia": cdrh3,
        "cdrh3_length": len(cdrh3),
    })


# Save output
out_df = pd.DataFrame(all_outputs)
out_df.to_csv(output_file, index=False)

df = pd.read_csv(path, sep="\t", engine="python")

print("\nTotal extracted rows:", len(out_df))
print("Saved to:", output_file)
print(out_df.head())
