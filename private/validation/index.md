# Query Index

Global rule: validation queries are generated for the database-side complete JSON source only. No accession-prefix or collection-name filter is applied unless a request explicitly asks for one.

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

## Q035

Request text:

> Give me all strains included in 2024.

Interpretation:

List all strains whose explicit `InclusionDate` year is `2024`. The year is read from the first four digits of `InclusionDate`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q035_inclusion_year_2024.py](../scripts/validation/Q035_inclusion_year_2024.py)

Outputs:

- Database file: [Q035_inclusion_year_2024.tsv](database/Q035_inclusion_year_2024.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 679

## Q036

Request text:

> Give me all strains deposited in 2019.

Interpretation:

List all strains whose explicit `DepositDate` year is `2019`. The year is read from the first four digits of `DepositDate`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q036_deposit_year_2019.py](../scripts/validation/Q036_deposit_year_2019.py)

Outputs:

- Database file: [Q036_deposit_year_2019.tsv](database/Q036_deposit_year_2019.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 203

## Q037

Request text:

> Give me all strains collected in 2021.

Interpretation:

List all strains whose explicit `CollectionDate` year is `2021`. The year is read from the first four digits of `CollectionDate`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q037_collection_year_2021.py](../scripts/validation/Q037_collection_year_2021.py)

Outputs:

- Database file: [Q037_collection_year_2021.tsv](database/Q037_collection_year_2021.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 338

## Q038

Request text:

> Give me all strains isolated on `20230515`.

Interpretation:

List all strains whose explicit `IsolationDate` field is exactly equal to `20230515`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q038_isolation_date_20230515.py](../scripts/validation/Q038_isolation_date_20230515.py)

Outputs:

- Database file: [Q038_isolation_date_20230515.tsv](database/Q038_isolation_date_20230515.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 59

## Q039

Request text:

> How many strains were included per year?

Interpretation:

Group strains by the year of explicit `InclusionDate`, read from the first four digits, and count strains per year.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q039_inclusion_count_by_year.py](../scripts/validation/Q039_inclusion_count_by_year.py)

Outputs:

- Database file: [Q039_inclusion_count_by_year.tsv](database/Q039_inclusion_count_by_year.tsv)
- Format: TSV with header
- Columns: `year`, `strain_count`
- Data rows: 53

## Q040

Request text:

> How many strains were deposited per year?

Interpretation:

Group strains by the year of explicit `DepositDate`, read from the first four digits, and count strains per year.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q040_deposit_count_by_year.py](../scripts/validation/Q040_deposit_count_by_year.py)

Outputs:

- Database file: [Q040_deposit_count_by_year.tsv](database/Q040_deposit_count_by_year.tsv)
- Format: TSV with header
- Columns: `year`, `strain_count`
- Data rows: 53

## Q041

Request text:

> Which strains have missing `CollectionDate`?

Interpretation:

List all strains where the explicit `CollectionDate` field is absent or empty.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q041_collection_date_missing.py](../scripts/validation/Q041_collection_date_missing.py)

Outputs:

- Database file: [Q041_collection_date_missing.tsv](database/Q041_collection_date_missing.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 185

## Q042

Request text:

> Which strains have missing `IsolationDate`?

Interpretation:

List all strains where the explicit `IsolationDate` field is absent or empty.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q042_isolation_date_missing.py](../scripts/validation/Q042_isolation_date_missing.py)

Outputs:

- Database file: [Q042_isolation_date_missing.tsv](database/Q042_isolation_date_missing.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 3910

## Q043

Request text:

> Which strains have `DepositDate` different from `InclusionDate`?

Interpretation:

List all strains where both explicit `DepositDate` and explicit `InclusionDate` are present and their values differ.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q043_deposit_date_differs_from_inclusion_date.py](../scripts/validation/Q043_deposit_date_differs_from_inclusion_date.py)

Outputs:

- Database file: [Q043_deposit_date_differs_from_inclusion_date.tsv](database/Q043_deposit_date_differs_from_inclusion_date.tsv)
- Format: TSV with header
- Columns: `accessionnumber`, `depositdate`, `inclusiondate`
- Data rows: 0

## Q044

Request text:

> Give me all strains collected before 2010.

Interpretation:

List all strains whose explicit `CollectionDate` year is before `2010`. The year is read from the first four digits of `CollectionDate`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q044_collection_before_2010.py](../scripts/validation/Q044_collection_before_2010.py)

Outputs:

- Database file: [Q044_collection_before_2010.tsv](database/Q044_collection_before_2010.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 2510

## Q045

Request text:

> Give me all strains included after 2020.

Interpretation:

List all strains whose explicit `InclusionDate` year is after `2020`. The year is read from the first four digits of `InclusionDate`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q045_inclusion_after_2020.py](../scripts/validation/Q045_inclusion_after_2020.py)

Outputs:

- Database file: [Q045_inclusion_after_2020.tsv](database/Q045_inclusion_after_2020.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 2001

## Q046

Request text:

> Give me all strains with `GeoOrigin = L000570`.

Interpretation:

List all strains whose explicit `GeoOrigin` field is equal to `L000570`. Strains are identified only by `accessionnumber`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q046_geoorigin_L000570.py](../scripts/validation/Q046_geoorigin_L000570.py)

Outputs:

- Database file: [Q046_geoorigin_L000570.tsv](database/Q046_geoorigin_L000570.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 18

## Q047

Request text:

> Give me all strains collected in Italy.

Interpretation:

List all strains whose explicit `GeoOrigin` resolves to a locality record with `Country = Italy`.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/localities_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q047_geoorigin_country_italy.py](../scripts/validation/Q047_geoorigin_country_italy.py)

Outputs:

- Database file: [Q047_geoorigin_country_italy.tsv](database/Q047_geoorigin_country_italy.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 5901

## Q048

Request text:

> Give me all strains collected in Torino.

Interpretation:

List all strains whose explicit `GeoOrigin` resolves to a locality record with `City = Torino`.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/localities_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q048_geoorigin_city_torino.py](../scripts/validation/Q048_geoorigin_city_torino.py)

Outputs:

- Database file: [Q048_geoorigin_city_torino.tsv](database/Q048_geoorigin_city_torino.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 81

## Q049

Request text:

> Give me all strains associated with `Parco del Meisino - Orto 53`.

Interpretation:

List all strains whose explicit `GeoOrigin` resolves to a locality record with `Locality = Parco del Meisino - Orto 53`.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/localities_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q049_geoorigin_locality_parco_del_meisino_orto_53.py](../scripts/validation/Q049_geoorigin_locality_parco_del_meisino_orto_53.py)

Outputs:

- Database file: [Q049_geoorigin_locality_parco_del_meisino_orto_53.tsv](database/Q049_geoorigin_locality_parco_del_meisino_orto_53.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 107

## Q050

Request text:

> How many strains are there per country?

Interpretation:

Resolve each strain's explicit `GeoOrigin` to a locality record and count strains by `Country`.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/localities_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q050_strain_count_by_country.py](../scripts/validation/Q050_strain_count_by_country.py)

Outputs:

- Database file: [Q050_strain_count_by_country.tsv](database/Q050_strain_count_by_country.tsv)
- Format: TSV with header
- Columns: `country`, `strain_count`
- Data rows: 41

## Q051

Request text:

> How many strains are there per city?

Interpretation:

Resolve each strain's explicit `GeoOrigin` to a locality record and count strains by `City`.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/localities_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q051_strain_count_by_city.py](../scripts/validation/Q051_strain_count_by_city.py)

Outputs:

- Database file: [Q051_strain_count_by_city.tsv](database/Q051_strain_count_by_city.tsv)
- Format: TSV with header
- Columns: `city`, `strain_count`
- Data rows: 194

## Q052

Request text:

> Which habitats have the most associated strains?

Interpretation:

Treat geographic habitats as explicit `GeoOrigin` locality records, count associated strains per `GeoOrigin`, and sort by descending strain count.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/localities_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q052_geographic_habitats_by_associated_strain_count.py](../scripts/validation/Q052_geographic_habitats_by_associated_strain_count.py)

Outputs:

- Database file: [Q052_geographic_habitats_by_associated_strain_count.tsv](database/Q052_geographic_habitats_by_associated_strain_count.tsv)
- Format: TSV with header
- Columns: `geoorigin`, `country`, `city`, `locality`, `strain_count`
- Data rows: 941

## Q053

Request text:

> Which habitats have only one associated strain?

Interpretation:

Treat geographic habitats as explicit `GeoOrigin` locality records and list `GeoOrigin` values associated with exactly one strain.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/localities_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q053_geographic_habitats_with_one_strain.py](../scripts/validation/Q053_geographic_habitats_with_one_strain.py)

Outputs:

- Database file: [Q053_geographic_habitats_with_one_strain.tsv](database/Q053_geographic_habitats_with_one_strain.tsv)
- Format: TSV with header
- Columns: `geoorigin`, `country`, `city`, `locality`, `strain_count`
- Data rows: 559

## Q054

Request text:

> Give me all strains from `Mediterranean Sea`.

Interpretation:

List all strains whose explicit `IsolationHabitat` field is equal to `Mediterranean Sea`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q054_isolation_habitat_mediterranean_sea.py](../scripts/validation/Q054_isolation_habitat_mediterranean_sea.py)

Outputs:

- Database file: [Q054_isolation_habitat_mediterranean_sea.tsv](database/Q054_isolation_habitat_mediterranean_sea.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 1195

## Q055

Request text:

> Give me all strains whose `IsolationHabitat` is equal to `Ex urban garden`.

Interpretation:

List all strains whose explicit `IsolationHabitat` field is equal to `Ex urban garden`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q055_isolation_habitat_ex_urban_garden.py](../scripts/validation/Q055_isolation_habitat_ex_urban_garden.py)

Outputs:

- Database file: [Q055_isolation_habitat_ex_urban_garden.tsv](database/Q055_isolation_habitat_ex_urban_garden.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 61

## Q056

Request text:

> Give me all strains whose `IsolationHabitat` contains `soil`.

Interpretation:

List all strains whose explicit `IsolationHabitat` field contains the text `soil`, using case-insensitive substring matching.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q056_isolation_habitat_contains_soil.py](../scripts/validation/Q056_isolation_habitat_contains_soil.py)

Outputs:

- Database file: [Q056_isolation_habitat_contains_soil.tsv](database/Q056_isolation_habitat_contains_soil.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 514

## Q057

Request text:

> Give me all strains with geographic habitat but without `IsolationHabitat`.

Interpretation:

List all strains where explicit `GeoOrigin` is present and explicit `IsolationHabitat` is absent or empty.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q057_geoorigin_present_isolation_habitat_missing.py](../scripts/validation/Q057_geoorigin_present_isolation_habitat_missing.py)

Outputs:

- Database file: [Q057_geoorigin_present_isolation_habitat_missing.tsv](database/Q057_geoorigin_present_isolation_habitat_missing.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 2646

## Q058

Request text:

> Give me all strains without `GeoOrigin`.

Interpretation:

List all strains where explicit `GeoOrigin` is absent or empty.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q058_geoorigin_missing.py](../scripts/validation/Q058_geoorigin_missing.py)

Outputs:

- Database file: [Q058_geoorigin_missing.tsv](database/Q058_geoorigin_missing.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 335

## Q059

Request text:

> Give me all strains that share the habitat with `TUCC00000735`.

Interpretation:

Interpret shared habitat as the same explicit geographic habitat (`GeoOrigin`) because `TUCC00000735` has no explicit `IsolationHabitat`. The target has `GeoOrigin = L000854`; list all other strains with the same `GeoOrigin`. The target strain itself is excluded from the output.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q059_same_geographic_habitat_as_TUCC00000735.py](../scripts/validation/Q059_same_geographic_habitat_as_TUCC00000735.py)

Outputs:

- Database file: [Q059_same_geographic_habitat_as_TUCC00000735.tsv](database/Q059_same_geographic_habitat_as_TUCC00000735.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 3

## Q060

Request text:

> Give me all strains that share the habitat with `MUT00007136`.

Interpretation:

Interpret shared habitat as the same explicit geographic habitat (`GeoOrigin`). The target has `GeoOrigin = L000569`; list all other strains with the same `GeoOrigin`. The target strain itself is excluded from the output.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q060_same_geographic_habitat_as_MUT00007136.py](../scripts/validation/Q060_same_geographic_habitat_as_MUT00007136.py)

Outputs:

- Database file: [Q060_same_geographic_habitat_as_MUT00007136.tsv](database/Q060_same_geographic_habitat_as_MUT00007136.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 38

## Q061

Request text:

> Give me all strains collected by `Giovanna Cristina Varese`.

Interpretation:

Resolve `Giovanna Cristina Varese` to explicit person ID `P000252`, then list all strains whose explicit `Collector` field contains `P000252`.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/people_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q061_collected_by_giovanna_cristina_varese.py](../scripts/validation/Q061_collected_by_giovanna_cristina_varese.py)

Outputs:

- Database file: [Q061_collected_by_giovanna_cristina_varese.tsv](database/Q061_collected_by_giovanna_cristina_varese.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 840

## Q062

Request text:

> Give me all strains deposited by `Giovanna Cristina Varese`.

Interpretation:

Resolve `Giovanna Cristina Varese` to explicit person ID `P000252`, then list all strains whose explicit `Depositor` field contains `P000252`.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/people_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q062_deposited_by_giovanna_cristina_varese.py](../scripts/validation/Q062_deposited_by_giovanna_cristina_varese.py)

Outputs:

- Database file: [Q062_deposited_by_giovanna_cristina_varese.tsv](database/Q062_deposited_by_giovanna_cristina_varese.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 2489

## Q063

Request text:

> Give me all strains isolated by `Giovanna Cristina Varese`.

Interpretation:

Resolve `Giovanna Cristina Varese` to explicit person ID `P000252`, then list all strains whose explicit `Isolator` field contains `P000252`.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/people_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q063_isolated_by_giovanna_cristina_varese.py](../scripts/validation/Q063_isolated_by_giovanna_cristina_varese.py)

Outputs:

- Database file: [Q063_isolated_by_giovanna_cristina_varese.tsv](database/Q063_isolated_by_giovanna_cristina_varese.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 687

## Q064

Request text:

> How many strains are associated with `P000252`?

Interpretation:

Count distinct strain records whose explicit `Collector`, `Depositor`, or `Isolator` fields contain `P000252`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q064_strain_count_associated_with_P000252.py](../scripts/validation/Q064_strain_count_associated_with_P000252.py)

Outputs:

- Database file: [Q064_strain_count_associated_with_P000252.tsv](database/Q064_strain_count_associated_with_P000252.tsv)
- Format: TSV with header
- Columns: `person_id`, `strain_count`
- Data rows: 1
- Result value: 2739

## Q065

Request text:

> Which people have more than 100 associated strains?

Interpretation:

Count distinct strain records per person across explicit `Collector`, `Depositor`, and `Isolator` fields, then list people with more than 100 associated strains.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/people_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q065_people_with_more_than_100_associated_strains.py](../scripts/validation/Q065_people_with_more_than_100_associated_strains.py)

Outputs:

- Database file: [Q065_people_with_more_than_100_associated_strains.tsv](database/Q065_people_with_more_than_100_associated_strains.tsv)
- Format: TSV with header
- Columns: `person_id`, `person_name`, `strain_count`
- Data rows: 35

## Q066

Request text:

> Give me all people associated with `TUCC00000735`.

Interpretation:

List all people present in the explicit `Collector`, `Depositor`, or `Isolator` fields of strain `TUCC00000735`, with their roles.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/people_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q066_people_associated_with_TUCC00000735.py](../scripts/validation/Q066_people_associated_with_TUCC00000735.py)

Outputs:

- Database file: [Q066_people_associated_with_TUCC00000735.tsv](database/Q066_people_associated_with_TUCC00000735.tsv)
- Format: TSV with header
- Columns: `person_id`, `person_name`, `roles`
- Data rows: 3

## Q067

Request text:

> Give me all people associated with `MUT00007136`.

Interpretation:

List all people present in the explicit `Collector`, `Depositor`, or `Isolator` fields of strain `MUT00007136`, with their roles.

For the database-side validation, the sources are `private/complete/TUCC_2026-07-18.json` and `private/complete/people_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q067_people_associated_with_MUT00007136.py](../scripts/validation/Q067_people_associated_with_MUT00007136.py)

Outputs:

- Database file: [Q067_people_associated_with_MUT00007136.tsv](database/Q067_people_associated_with_MUT00007136.tsv)
- Format: TSV with header
- Columns: `person_id`, `person_name`, `roles`
- Data rows: 2

## Q068

Request text:

> Give me all strains that grow at recommended temperature `25`.

Interpretation:

List all strains whose explicit `RecommendedTempGrowth` field is equal to `25`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q068_recommended_temp_growth_25.py](../scripts/validation/Q068_recommended_temp_growth_25.py)

Outputs:

- Database file: [Q068_recommended_temp_growth_25.tsv](database/Q068_recommended_temp_growth_25.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 6005

## Q069

Request text:

> Give me all strains that grow at recommended temperature `24`.

Interpretation:

List all strains whose explicit `RecommendedTempGrowth` field is equal to `24`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q069_recommended_temp_growth_24.py](../scripts/validation/Q069_recommended_temp_growth_24.py)

Outputs:

- Database file: [Q069_recommended_temp_growth_24.tsv](database/Q069_recommended_temp_growth_24.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 119

## Q070

Request text:

> Give me all strains identified with technique `MALDI-TOF`.

Interpretation:

List all strains whose explicit `IdentificationTechnique` field includes `MALDI-TOF` as a semicolon-separated technique.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q070_identification_technique_maldi_tof.py](../scripts/validation/Q070_identification_technique_maldi_tof.py)

Outputs:

- Database file: [Q070_identification_technique_maldi_tof.tsv](database/Q070_identification_technique_maldi_tof.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 362

## Q071

Request text:

> Which strains have multiple identification techniques?

Interpretation:

Split the explicit `IdentificationTechnique` field on semicolons and list strains with more than one technique, sorted by descending technique count.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q071_strains_with_multiple_identification_techniques.py](../scripts/validation/Q071_strains_with_multiple_identification_techniques.py)

Outputs:

- Database file: [Q071_strains_with_multiple_identification_techniques.tsv](database/Q071_strains_with_multiple_identification_techniques.tsv)
- Format: TSV with header
- Columns: `accessionnumber`, `technique_count`, `identificationtechniques`
- Data rows: 1519

## Q072

Request text:

> Give me all strains with `RiskGroup = 2` and `AvailableForDis = Yes`.

Interpretation:

List all strains whose explicit `RiskGroup` field is equal to `2` and whose explicit `AvailableForDis` field is equal to `Yes`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q072_riskgroup_2_available_for_distribution_yes.py](../scripts/validation/Q072_riskgroup_2_available_for_distribution_yes.py)

Outputs:

- Database file: [Q072_riskgroup_2_available_for_distribution_yes.tsv](database/Q072_riskgroup_2_available_for_distribution_yes.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 795

## Q073

Request text:

> Give me all strains with `UseRestrictions = 1`.

Interpretation:

List all strains whose explicit `UseRestrictions` field is equal to `1`.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q073_use_restrictions_1.py](../scripts/validation/Q073_use_restrictions_1.py)

Outputs:

- Database file: [Q073_use_restrictions_1.tsv](database/Q073_use_restrictions_1.tsv)
- Format: TSV with header
- Columns: `accessionnumber`
- Data rows: 306

## Q074

Request text:

> How many strains are there for each `RiskGroup`?

Interpretation:

Group strains by explicit `RiskGroup` value and count strains per group. Records without an explicit `RiskGroup` are not included in the grouped output.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q074_strain_count_by_riskgroup.py](../scripts/validation/Q074_strain_count_by_riskgroup.py)

Outputs:

- Database file: [Q074_strain_count_by_riskgroup.tsv](database/Q074_strain_count_by_riskgroup.tsv)
- Format: TSV with header
- Columns: `riskgroup`, `strain_count`
- Data rows: 2

## Q075

Request text:

> How many strains are there for each `OrganismType`?

Interpretation:

Group strains by explicit `OrganismType` value and count strains per organism type. Records without an explicit `OrganismType` are not included in the grouped output.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q075_strain_count_by_organism_type.py](../scripts/validation/Q075_strain_count_by_organism_type.py)

Outputs:

- Database file: [Q075_strain_count_by_organism_type.tsv](database/Q075_strain_count_by_organism_type.tsv)
- Format: TSV with header
- Columns: `organismtype`, `strain_count`
- Data rows: 3

## Q076

Request text:

> Which are the 20 most represented genera?

Interpretation:

Count strains by explicit `Genus` value and return the 20 genera with the highest strain counts, sorted by descending count and then genus name.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q076_top_20_genera_by_strain_count.py](../scripts/validation/Q076_top_20_genera_by_strain_count.py)

Outputs:

- Database file: [Q076_top_20_genera_by_strain_count.tsv](database/Q076_top_20_genera_by_strain_count.tsv)
- Format: TSV with header
- Columns: `genus`, `strain_count`
- Data rows: 20

## Q077

Request text:

> Which are the 20 most represented species?

Interpretation:

Count strains by explicit `Genus` and `Species` values and return the 20 species-level pairs with the highest strain counts, sorted by descending count and then taxon name. Records missing either `Genus` or `Species` are not included.

For the database-side validation, the source is `private/complete/TUCC_2026-07-18.json`.

Knowledge-base validation is intentionally not generated.

Script:

- File: [Q077_top_20_species_by_strain_count.py](../scripts/validation/Q077_top_20_species_by_strain_count.py)

Outputs:

- Database file: [Q077_top_20_species_by_strain_count.tsv](database/Q077_top_20_species_by_strain_count.tsv)
- Format: TSV with header
- Columns: `genus`, `species`, `strain_count`
- Data rows: 20
