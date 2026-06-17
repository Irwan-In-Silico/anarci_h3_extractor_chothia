# anarci_h3_extractor_chothia
Extract Chothia-numbered CDR-H3 sequences and metadata from ANARCI output files




## What it does

This script takes one or more ANARCI output files (.csv) and parses them to extract:
- Antibody/nanobody ID
- User-specified label (binder/non-binder — you add this in the script settings)
- HMM species (auto-detected by ANARCI)
- Chain type (auto-detected by ANARCI)
- e-value and score from ANARCI
- Sequence start and end indices (from ANARCI)
- The extracted CDR-H3 sequence (Chothia numbering)
- Length of the CDR-H3 sequence

All of this is saved as a CSV file for downstream analysis.

## Requirements

- Python 3.7+
- pandas

Install dependencies with:

bash
pip install pandas


Or if you have a requirements.txt:

bash
pip install -r requirements.txt


## How to run

1. Clone this repo:
   bash
   git clone https://github.com/Irwan_In_Silico/anarci_h3_extractor_chothia.git
   cd anarci_h3_extractor_chothia
   

2. Edit the 'SETTINGS' in the script:
   - Place [input_file] with your input file name
   - Set ouput file name.

3. Run the script:
   bash
   python extract_h3_chothia.py
   

## Output

A CSV file with the following columns:
| Column | Description |
|--------|-------------|
| id | Antibody/nanobody identifier |
| label | User-defined label (e.g., binder/non-binder) |
| hmm_species | Species predicted by ANARCI |
| chain_type | Heavy or light chain |
| evalue | e-value from ANARCI |
| score | Score from ANARCI |
| seq_start | Start index of the full sequence |
| seq_end | End index of the full sequence |
| cdrh3_sequence | Extracted CDR-H3 using Chothia numbering |
| cdrh3_length | Length of the CDR-H3 sequence |

## Notes

- This script uses *Chothia* numbering. If you want IMGT numbering, check out the sister repo: [anarci_h3_extractor_imgt]

