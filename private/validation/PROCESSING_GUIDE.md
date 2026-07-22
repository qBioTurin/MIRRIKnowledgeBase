# PROCESSING_GUIDE — Validation Query Runs

Use this procedure when a single validation query is requested.

The goal is to answer the query using only the knowledge base under `wiki/` and save the result in:

```text
private/validation/knowledgebase/<model-id>/
```

Process only the requested query. Do not finish before creating the file.

## Allowed files

You may read:

* `private/validation/PROCESSING_GUIDE.md`
* `private/validation/index.md`
* `wiki/index.md`
* relevant files under `wiki/`

`private/validation/index.md` contains the query specification, including the required format, columns, and ordering. Do not use it as evidence for the result.

## Forbidden files

Do not read or use:

* `private/validation/database/`
* `private/scripts/`
* `private/complete/`
* `raw/`
* any other file under `private/`, except the allowed files and the current model output directory
* results produced by other models
* external knowledge or web sources

Ignore references to databases, scripts, expected results, or expected row counts in control files.

## Model identifier

The model identifier is available in the environment variable:

```bash
VALIDATION_MODEL_ID
```

Verify that the variable is defined:

```bash
if [ -z "${VALIDATION_MODEL_ID:-}" ]; then
    echo "VALIDATION_MODEL_ID is not set" >&2
    exit 1
fi
```

The output directory is:

```bash
RESULT_DIR="private/validation/knowledgebase/${VALIDATION_MODEL_ID}"
mkdir -p "$RESULT_DIR"
```

Use only paths relative to the repository root.

## Workflow

1. Identify the requested query.
2. Read its specification in `private/validation/index.md`.
3. Read `wiki/index.md`.
4. Search for all relevant information only under `wiki/`.
5. Collect every explicitly supported result.
6. Remove duplicates and apply the required ordering.
7. Generate the result in a temporary file.
8. Validate the temporary file.
9. Move it to the final path only if validation succeeds.
10. Reopen and verify the final file.

Do not stop before verification is complete.

## Result filename

Save the result under:

```text
private/validation/knowledgebase/${VALIDATION_MODEL_ID}/
```

Use a filename such as:

```text
Q001_formofsupply_agar.tsv
```

The descriptive suffix must be:

* lowercase
* ASCII
* underscore-separated
* concise
* derived from the query

## Existing files

An existing file may come from a failed attempt.

If the result file already exists:

* if it is valid, do not rerun the query;
* if it is empty, malformed, or contains only the header, delete it and regenerate it.

Do not modify a valid result.

## Atomic writing

Do not write directly to the final file.

```bash
RESULT_FILE="${RESULT_DIR}/<result-name>.tsv"
TEMP_FILE="${RESULT_FILE}.tmp"

rm -f "$TEMP_FILE"
```

Write the complete result to the temporary file:

```bash
{
    printf 'accessionnumber\n'
    cat "$SORTED_RESULTS"
} > "$TEMP_FILE"
```

After validation succeeds:

```bash
mv "$TEMP_FILE" "$RESULT_FILE"
```

If validation fails, delete the temporary file and correct the problem.

## TSV rules

For queries returning strains:

```tsv
accessionnumber
MUT00000002
MUT00000003
```

Rules:

* use exactly one header row;
* use lowercase column names unless the query specifies otherwise;
* use one result per row;
* remove duplicates;
* use deterministic ordering;
* use Unix line endings;
* do not include Markdown or explanatory text;
* do not include inferred or unsupported values.

For count or grouped queries, use only the columns required by the query.

## Verification

Before finishing, verify that:

* the file exists and is readable;
* the file is not empty;
* the header is correct and appears exactly once;
* every row has the correct number of columns;
* there are no duplicate rows;
* the ordering is correct;
* every row is supported by the wiki;
* no discovered result is missing;
* the filename and output path are correct.

For large result sets, compare the TSV data rows with the collected sorted results:

```bash
diff \
    <(tail -n +2 "$RESULT_FILE") \
    "$SORTED_RESULTS"
```

Also verify the row count:

```bash
expected=$(wc -l < "$SORTED_RESULTS" | tr -d ' ')
actual=$(tail -n +2 "$RESULT_FILE" | wc -l | tr -d ' ')

[ "$expected" -eq "$actual" ]
```

## Command failures

If a command fails:

1. read the error;
2. correct the syntax, path, quoting, or search method;
3. retry with a simpler method;
4. continue from the last completed step.

Do not treat one empty search as proof that no results exist. Try exact strings, alternative terms, and broader or narrower searches, always under `wiki/`.

## Blocked queries

A query is blocked only if:

* the query cannot be identified;
* a required allowed file is missing;
* `VALIDATION_MODEL_ID` is not defined;
* the result cannot be created after corrective attempts.

In that case, create a short trace file in the model output directory describing:

* the missing requirement;
* the attempts made;
* why no allowed alternative exists.

## Final response

On success, return only:

```text
STATUS=SUCCESS
RESULT_FILE=<path>
ROW_COUNT=<data-row-count>
```

On failure:

```text
STATUS=BLOCKED
TRACE_FILE=<path>
```
