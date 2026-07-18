# Query Index

Global rule: validation queries are generated for the database-side complete JSON source only. No knowledge-base validation output is generated unless explicitly requested later. No accession-prefix or collection-name filter is applied unless a request explicitly asks for one.

Question-only list: [query-list.md](query-list.md)

## Q001

Request text:

> Give me all the strains with formOfSupply Agar

Interpretation:

List all strains whose explicit `FormOfSupply` contains the value `Agar`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q001_formofsupply_agar.py](../scripts/validation/Q001_formofsupply_agar.py)

Outputs:

- Database file: [Q001_formofsupply_agar.tsv](database/Q001_formofsupply_agar.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 6733

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

## Q003

Request text:

> Give me all the strains whose `Substrate` contains `wood`.

Interpretation:

List all strains whose explicit `Substrate` field contains the text `wood`, using case-insensitive substring matching. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q003_substrate_contains_wood.py](../scripts/validation/Q003_substrate_contains_wood.py)

Outputs:

- Database file: [Q003_substrate_contains_wood.tsv](database/Q003_substrate_contains_wood.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 220

## Q004

Request text:

> Give me all the strains whose `Substrate` contains `chicken`.

Interpretation:

List all strains whose explicit `Substrate` field contains the text `chicken`, using case-insensitive substring matching. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q004_substrate_contains_chicken.py](../scripts/validation/Q004_substrate_contains_chicken.py)

Outputs:

- Database file: [Q004_substrate_contains_chicken.tsv](database/Q004_substrate_contains_chicken.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 23

## Q005

Request text:

> Give me all the strains whose `OrganismType` is equal to `Filamentous Fungi`.

Interpretation:

List all strains whose explicit `OrganismType` field is equal to `Filamentous Fungi`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q005_organismtype_filamentous_fungi.py](../scripts/validation/Q005_organismtype_filamentous_fungi.py)

Outputs:

- Database file: [Q005_organismtype_filamentous_fungi.tsv](database/Q005_organismtype_filamentous_fungi.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 6296

## Q006

Request text:

> Give me all the strains whose `OrganismType` is equal to `Bacteria`.

Interpretation:

List all strains whose explicit `OrganismType` field is equal to `Bacteria`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q006_organismtype_bacteria.py](../scripts/validation/Q006_organismtype_bacteria.py)

Outputs:

- Database file: [Q006_organismtype_bacteria.tsv](database/Q006_organismtype_bacteria.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 493

## Q007

Request text:

> Give me all the strains whose `OrganismType` is equal to `Yeasts`.

Interpretation:

List all strains whose explicit `OrganismType` field is equal to `Yeasts`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q007_organismtype_yeasts.py](../scripts/validation/Q007_organismtype_yeasts.py)

Outputs:

- Database file: [Q007_organismtype_yeasts.tsv](database/Q007_organismtype_yeasts.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 427

## Q008

Request text:

> Give me all strains available at the collection (`AvailableAtCC = Yes`).

Interpretation:

List all strains whose explicit `AvailableAtCC` field is equal to `Yes`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q008_available_at_cc_yes.py](../scripts/validation/Q008_available_at_cc_yes.py)

Outputs:

- Database file: [Q008_available_at_cc_yes.tsv](database/Q008_available_at_cc_yes.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 7216

## Q009

Request text:

> Give me all strains available for distribution (`AvailableForDis = Yes`).

Interpretation:

List all strains whose explicit `AvailableForDis` field is equal to `Yes`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q009_available_for_distribution_yes.py](../scripts/validation/Q009_available_for_distribution_yes.py)

Outputs:

- Database file: [Q009_available_for_distribution_yes.tsv](database/Q009_available_for_distribution_yes.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 7216

## Q010

Request text:

> Give me all public strains (`PublicData = Yes`).

Interpretation:

List all strains whose explicit `PublicData` field is equal to `Yes`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q010_public_data_yes.py](../scripts/validation/Q010_public_data_yes.py)

Outputs:

- Database file: [Q010_public_data_yes.tsv](database/Q010_public_data_yes.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 7216

## Q011

Request text:

> Give me all strains registered in the collection (`RegisteredCollection = Yes`).

Interpretation:

List all strains whose explicit `RegisteredCollection` field is equal to `Yes`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q011_registered_collection_yes.py](../scripts/validation/Q011_registered_collection_yes.py)

Outputs:

- Database file: [Q011_registered_collection_yes.tsv](database/Q011_registered_collection_yes.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 0

## Q012

Request text:

> Give me all strains whose `RiskGroup` is equal to `1`.

Interpretation:

List all strains whose explicit `RiskGroup` field is equal to `1`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q012_riskgroup_1.py](../scripts/validation/Q012_riskgroup_1.py)

Outputs:

- Database file: [Q012_riskgroup_1.tsv](database/Q012_riskgroup_1.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 5615

## Q013

Request text:

> Give me all strains whose `RiskGroup` is equal to `2`.

Interpretation:

List all strains whose explicit `RiskGroup` field is equal to `2`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q013_riskgroup_2.py](../scripts/validation/Q013_riskgroup_2.py)

Outputs:

- Database file: [Q013_riskgroup_2.tsv](database/Q013_riskgroup_2.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 795

## Q014

Request text:

> Give me all GMO strains.

Interpretation:

List all strains whose explicit `GMO` field is equal to `Yes`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q014_gmo_yes.py](../scripts/validation/Q014_gmo_yes.py)

Outputs:

- Database file: [Q014_gmo_yes.tsv](database/Q014_gmo_yes.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 14

## Q015

Request text:

> Give me all non-GMO strains.

Interpretation:

List all strains whose explicit `GMO` field is equal to `No`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q015_gmo_no.py](../scripts/validation/Q015_gmo_no.py)

Outputs:

- Database file: [Q015_gmo_no.tsv](database/Q015_gmo_no.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 7202

## Q016

Request text:

> Give me all strains that are type strains.

Interpretation:

List all strains whose explicit `TypeStrain` field is equal to `Yes`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q016_type_strain_yes.py](../scripts/validation/Q016_type_strain_yes.py)

Outputs:

- Database file: [Q016_type_strain_yes.tsv](database/Q016_type_strain_yes.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 43

## Q017

Request text:

> Give me all strains that are not type strains.

Interpretation:

List all strains whose explicit `TypeStrain` field is equal to `No`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q017_type_strain_no.py](../scripts/validation/Q017_type_strain_no.py)

Outputs:

- Database file: [Q017_type_strain_no.tsv](database/Q017_type_strain_no.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 7173

## Q018

Request text:

> Give me all dual-use strains.

Interpretation:

List all strains whose explicit `DualUse` field is equal to `Yes`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q018_dual_use_yes.py](../scripts/validation/Q018_dual_use_yes.py)

Outputs:

- Database file: [Q018_dual_use_yes.tsv](database/Q018_dual_use_yes.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 8

## Q019

Request text:

> Give me all strains marked as EU quarantine.

Interpretation:

List all strains whose explicit `EUQuarantine` field is equal to `Yes`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q019_eu_quarantine_yes.py](../scripts/validation/Q019_eu_quarantine_yes.py)

Outputs:

- Database file: [Q019_eu_quarantine_yes.tsv](database/Q019_eu_quarantine_yes.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 135

## Q020

Request text:

> Give me all strains whose `NagoyaConditions` is equal to `1`.

Interpretation:

List all strains whose explicit `NagoyaConditions` field is equal to `1`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q020_nagoya_conditions_1.py](../scripts/validation/Q020_nagoya_conditions_1.py)

Outputs:

- Database file: [Q020_nagoya_conditions_1.tsv](database/Q020_nagoya_conditions_1.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 7066

## Q021

Request text:

> Give me all strains whose `UseRestrictions` is equal to `3`.

Interpretation:

List all strains whose explicit `UseRestrictions` field is equal to `3`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q021_use_restrictions_3.py](../scripts/validation/Q021_use_restrictions_3.py)

Outputs:

- Database file: [Q021_use_restrictions_3.tsv](database/Q021_use_restrictions_3.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 6461

## Q022

Request text:

> Give me all strains from the genus `Penicillium`.

Interpretation:

List all strains whose explicit `Genus` field is equal to `Penicillium`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q022_genus_penicillium.py](../scripts/validation/Q022_genus_penicillium.py)

Outputs:

- Database file: [Q022_genus_penicillium.tsv](database/Q022_genus_penicillium.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 1141

## Q023

Request text:

> Give me all strains from the genus `Diplodia`.

Interpretation:

List all strains whose explicit `Genus` field is equal to `Diplodia`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q023_genus_diplodia.py](../scripts/validation/Q023_genus_diplodia.py)

Outputs:

- Database file: [Q023_genus_diplodia.tsv](database/Q023_genus_diplodia.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 7

## Q024

Request text:

> Give me all strains from the genus `Coniochaeta`.

Interpretation:

List all strains whose explicit `Genus` field is equal to `Coniochaeta`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q024_genus_coniochaeta.py](../scripts/validation/Q024_genus_coniochaeta.py)

Outputs:

- Database file: [Q024_genus_coniochaeta.tsv](database/Q024_genus_coniochaeta.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 9

## Q025

Request text:

> Give me all strains from the species `Diplodia seriata`.

Interpretation:

List all strains whose explicit `Genus` field is equal to `Diplodia` and whose explicit `Species` field is equal to `seriata`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q025_species_diplodia_seriata.py](../scripts/validation/Q025_species_diplodia_seriata.py)

Outputs:

- Database file: [Q025_species_diplodia_seriata.tsv](database/Q025_species_diplodia_seriata.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 5

## Q026

Request text:

> Give me all strains from the species `Penicillium aurantiogriseum`.

Interpretation:

List all strains whose explicit `Genus` field is equal to `Penicillium` and whose explicit `Species` field is equal to `aurantiogriseum`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q026_species_penicillium_aurantiogriseum.py](../scripts/validation/Q026_species_penicillium_aurantiogriseum.py)

Outputs:

- Database file: [Q026_species_penicillium_aurantiogriseum.tsv](database/Q026_species_penicillium_aurantiogriseum.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 70

## Q027

Request text:

> Give me all strains identified only at genus level, with `Species = sp.`.

Interpretation:

List all strains whose explicit `Species` field is equal to `sp.`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q027_species_sp.py](../scripts/validation/Q027_species_sp.py)

Outputs:

- Database file: [Q027_species_sp.tsv](database/Q027_species_sp.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 520

## Q028

Request text:

> How many distinct genera are in the knowledge base?

Interpretation:

Count distinct explicit `Genus` values in the complete JSON source. This is generated database-side only for now, even though the natural-language request mentions the knowledge base.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q028_distinct_genera_count.py](../scripts/validation/Q028_distinct_genera_count.py)

Outputs:

- Database file: [Q028_distinct_genera_count.tsv](database/Q028_distinct_genera_count.tsv)
- Format: TSV with header
- Columns: `distinct_genera`
- Data rows: 1
- Result value: 662

## Q029

Request text:

> How many distinct species are there for each genus?

Interpretation:

For each explicit `Genus`, count distinct explicit `Species` values.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q029_distinct_species_count_by_genus.py](../scripts/validation/Q029_distinct_species_count_by_genus.py)

Outputs:

- Database file: [Q029_distinct_species_count_by_genus.tsv](database/Q029_distinct_species_count_by_genus.tsv)
- Format: TSV with header
- Columns: `genus`, `distinct_species_count`
- Data rows: 662

## Q030

Request text:

> Which genera have more than 50 strains?

Interpretation:

List genera with more than 50 strain records and report their strain counts.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q030_genera_more_than_50_strains.py](../scripts/validation/Q030_genera_more_than_50_strains.py)

Outputs:

- Database file: [Q030_genera_more_than_50_strains.tsv](database/Q030_genera_more_than_50_strains.tsv)
- Format: TSV with header
- Columns: `genus`, `strain_count`
- Data rows: 20

## Q031

Request text:

> Which genera have only one represented species?

Interpretation:

List genera with exactly one distinct explicit `Species` value represented.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q031_genera_with_one_species.py](../scripts/validation/Q031_genera_with_one_species.py)

Outputs:

- Database file: [Q031_genera_with_one_species.tsv](database/Q031_genera_with_one_species.tsv)
- Format: TSV with header
- Columns: `genus`, `species`, `distinct_species_count`
- Data rows: 447

## Q032

Request text:

> Which genera have both bacterial and fungal strains?

Interpretation:

List genera whose explicit `OrganismType` values include `Bacteria` and at least one fungal type. Fungal types are interpreted from explicit values as `Filamentous Fungi` or `Yeasts`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q032_genera_with_bacterial_and_fungal_strains.py](../scripts/validation/Q032_genera_with_bacterial_and_fungal_strains.py)

Outputs:

- Database file: [Q032_genera_with_bacterial_and_fungal_strains.tsv](database/Q032_genera_with_bacterial_and_fungal_strains.tsv)
- Format: TSV with header
- Columns: `genus`, `organism_types`, `strain_count`
- Data rows: 0

## Q033

Request text:

> Give me all organisms similar to `MUT00007136` by same genus.

Interpretation:

Find the target strain `MUT00007136`, read its explicit `Genus` value (`Coniochaeta`), and list all other strains with the same genus. The target strain itself is excluded from the output. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q033_similar_to_MUT00007136_same_genus.py](../scripts/validation/Q033_similar_to_MUT00007136_same_genus.py)

Outputs:

- Database file: [Q033_similar_to_MUT00007136_same_genus.tsv](database/Q033_similar_to_MUT00007136_same_genus.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 8

## Q034

Request text:

> Give me all organisms similar to `MUT00007136` by same species.

Interpretation:

Find the target strain `MUT00007136`, read its explicit `Genus` and `Species` values (`Coniochaeta sp.`), and list all other strains with the same genus and species. The target strain itself is excluded from the output. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q034_similar_to_MUT00007136_same_species.py](../scripts/validation/Q034_similar_to_MUT00007136_same_species.py)

Outputs:

- Database file: [Q034_similar_to_MUT00007136_same_species.tsv](database/Q034_similar_to_MUT00007136_same_species.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 6
