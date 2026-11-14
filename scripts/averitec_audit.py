
import json
import random
from pathlib import Path

import pandas as pd


# --------------------------------------------------
# 1. Configuration
# --------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]

DATASET_PATH = ROOT / "data" / "dev.json"
OUTPUT_PATH = ROOT / "data" / "ai_annotation_master_sheet.csv"

RANDOM_SEED = 42
SAMPLE_SIZE = 30

TARGET_CATEGORIES = [
    "Supported",
    "Refuted",
    "Conflicting Evidence/Cherrypicking",
    "Not Enough Evidence",
]


# --------------------------------------------------
# 2. Load the AVeriTeC development dataset
# --------------------------------------------------

if not DATASET_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATASET_PATH}\n"
        "Download dev.json from the original AVeriTeC repository "
        "and place it in the data/ folder."
    )

with open(DATASET_PATH, "r", encoding="utf-8") as f:
    dev_data = json.load(f)

if not isinstance(dev_data, list):
    raise ValueError("Expected dev.json to contain a list of records.")

print(f"Total records in dev.json: {len(dev_data)}")


# --------------------------------------------------
# 3. Group records by verdict category
# --------------------------------------------------

verdict_groups = {category: [] for category in TARGET_CATEGORIES}

for idx, item in enumerate(dev_data):
    label = item.get("label")

    if label in verdict_groups:
        record = item.copy()
        record["dataset_row"] = idx
        verdict_groups[label].append(record)

print("\nAvailable records by category:")

for category, records in verdict_groups.items():
    print(f"{category}: {len(records)}")


# --------------------------------------------------
# 4. Validate category sizes
# --------------------------------------------------

for category, records in verdict_groups.items():
    if len(records) < SAMPLE_SIZE:
        raise ValueError(
            f"Insufficient records for '{category}': "
            f"{len(records)} available; {SAMPLE_SIZE} required."
        )


# --------------------------------------------------
# 5. Perform stratified random sampling
# --------------------------------------------------

rng = random.Random(RANDOM_SEED)
sampled_records = []

for category in TARGET_CATEGORIES:
    sampled = rng.sample(verdict_groups[category], SAMPLE_SIZE)
    sampled_records.extend(sampled)

    print(f"Selected {len(sampled)} records: {category}")

if len(sampled_records) != 120:
    raise ValueError(
        f"Expected 120 records, but selected {len(sampled_records)}."
    )


# --------------------------------------------------
# 6. Format questions and answers
# --------------------------------------------------

def format_questions_and_answers(qas):

    if not isinstance(qas, list):
        return str(qas) if qas is not None else ""

    formatted = []

    for qa in qas:
        if isinstance(qa, dict):
            question = qa.get("question", "")
            answer = qa.get("answer", "")
            qa_type = qa.get("qa_type", "Unknown")

            formatted.append(
                f"Q: {question}\n"
                f"A: {answer} [Type: {qa_type}]"
            )
        else:
            formatted.append(str(qa))

    return "\n".join(formatted)


# --------------------------------------------------
# 7. Format source URLs
# --------------------------------------------------

def format_sources(sources):

    if isinstance(sources, list):
        return "\n".join(str(source) for source in sources)

    return str(sources) if sources is not None else ""


# --------------------------------------------------
# 8. Create the annotation master sheet
# --------------------------------------------------

rows = []

for item in sampled_records:

    qas = item.get("questions_and_answers", [])

    sources = (
        item.get("evidence_urls")
        or item.get("source_urls")
        or []
    )

    row = {
        "dataset_row": item.get("dataset_row"),
        "label": item.get("label"),
        "claim": item.get("claim"),
        "claim_date": item.get("claim_date"),
        "speaker": item.get("speaker"),
        "fact_checking_article": item.get("fact_checking_article"),
        "original_claim_url": item.get("original_claim_url"),
        "justification": item.get("justification"),
        "questions_and_answers": format_questions_and_answers(qas),
        "source_urls": format_sources(sources),

        # Six audit dimensions
        "CC": None,
        "CC_rationale": None,
        "CE": None,
        "CE_rationale": None,
        "AE": None,
        "AE_rationale": None,
        "CS": None,
        "CS_rationale": None,
        "UA": None,
        "UA_rationale": None,
        "JL": None,
        "JL_rationale": None,

        # Review and annotation metadata
        "ai_notes": None,
        "review_status": "pending",
        "reviewer": None,
        "review_date": None,
    }

    rows.append(row)


# --------------------------------------------------
# 9. Export the master sheet
# --------------------------------------------------

output_df = pd.DataFrame(rows)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

output_df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8"
)


# --------------------------------------------------
# 10. Verify the generated sample
# --------------------------------------------------

print("\nSampling verification:")

print(f"Total sampled records: {len(output_df)}")
print(f"Unique dataset rows: {output_df['dataset_row'].nunique()}")

print("\nRecords per verdict category:")
print(output_df["label"].value_counts().to_string())

assert len(output_df) == 120, "Sample must contain exactly 120 records."
assert output_df["dataset_row"].nunique() == 120, "Duplicate dataset rows detected."

for category in TARGET_CATEGORIES:
    count = (output_df["label"] == category).sum()
    assert count == SAMPLE_SIZE, (
        f"Expected {SAMPLE_SIZE} records for {category}, found {count}."
    )

print("\nSuccessfully generated annotation master sheet:")
print(OUTPUT_PATH)
print(f"Rows: {len(output_df)}")
print(f"Columns: {len(output_df.columns)}")
