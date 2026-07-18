# Query Index

Global rule: validation queries use all strain records available in both the complete JSON source and the knowledge base. No accession-prefix or collection-name filter is applied unless a request explicitly asks for one.

## Q001

Request text:

> Give me all the strains with formOfSupply Agar

Interpretation:

List all strains whose explicit `FormOfSupply` contains the value `Agar`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

For the knowledge-base validation, only `wiki/microorganisms/*.md` is consulted.

Script:

- File: [Q001_formofsupply_agar.py](../scripts/validation/Q001_formofsupply_agar.py)

Outputs:

- Database file: [Q001_formofsupply_agar.tsv](database/Q001_formofsupply_agar.tsv)
- Knowledge-base file: [Q001_formofsupply_agar.tsv](knowledgebase/Q001_formofsupply_agar.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 6733
- Comparison: database and knowledge-base TSV files are identical

## Q002

Request text:

> Give me all the strains whose `Substrate` is equal to `Soil contaminated by PAHs`.

Interpretation:

List all strains whose explicit `Substrate` field is equal to `Soil contaminated by PAHs`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated yet.

Script:

- File: [Q002_substrate_soil_contaminated_by_pahs.py](../scripts/validation/Q002_substrate_soil_contaminated_by_pahs.py)

Outputs:

- Database file: [Q002_substrate_soil_contaminated_by_pahs.tsv](database/Q002_substrate_soil_contaminated_by_pahs.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 119
