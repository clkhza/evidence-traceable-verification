
import json
import random
from pathlib import Path

import pandas as pd

# --------------------------------------------------
# 1. Paths and sampling configuration
# --------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]

DATASET_PATH = ROOT / "data" / "dev.json"
MASTER_SHEET_PATH = ROOT / "data" / "ai_annotation_master_sheet.csv"
MANIFEST_PATH = ROOT / "results" / "sample_manifest.csv"

RANDOM_SEED = 42
SAMPLE_SIZE_PER_CATEGORY = 30

TARGET_CATEGORIES = [
    "Supported",
    "Refuted",
    "Conflicting Evidence/Cherrypicking",
    "Not Enough Evidence",
]

# --------------------------------------------------
# 2. Load the AVeriTeC development dataset
# --------------------------------------------------

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
        item_with_index = item.copy()
        item_with_index["dataset_row"] = idx
        verdict_groups[label].append(item_with_index)

print("\nRecords available per category:")

for label, records in verdict_groups.items():
    print(f"{label}: {len(records)}")

# Ensure every category contains at least 30 records
for label, records in verdict_groups.items():
    if len(records) < SAMPLE_SIZE_PER_CATEGORY:
        raise ValueError(
            f"Insufficient records for '{label}': "
            f"found {len(records)}, expected {SAMPLE_SIZE_PER_CATEGORY}."
        )

# --------------------------------------------------
# 4. Perform stratified random sampling
# --------------------------------------------------

rng = random.Random(RANDOM_SEED)
sampled_records = []

for label in TARGET_CATEGORIES:
    sampled = rng.sample(
        verdict_groups[label],
        SAMPLE_SIZE_PER_CATEGORY
    )
    sampled_records.extend(sampled)

    print(f"Sampled {len(sampled)} records for: {label}")

if len(sampled_records) != 120:
    raise ValueError(
        f"Expected 120 sampled records, got {len(sampled_records)}."
    )

# --------------------------------------------------
# 5. Prepare the annotation master sheet
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


def format_sources(sources):
    if isinstance(sources, list):
        return "\n".join(str(source) for source in sources)

    return str(sources) if sources is not None else ""


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

        # Annotation fields
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
        "ai_notes": None,
        "review_status": "pending",
        "reviewer": None,
        "review_date": None,
    }

    rows.append(row)

output_df = pd.DataFrame(rows)

# --------------------------------------------------
# 6. Generate the sampling manifest
# --------------------------------------------------

manifest_df = pd.DataFrame([
    {
        "dataset_row": item["dataset_row"],
        "label": item.get("label"),
        "claim": item.get("claim"),
    }
    for item in sampled_records
])

# --------------------------------------------------
# 7. Export both files
# --------------------------------------------------

MASTER_SHEET_PATH.parent.mkdir(parents=True, exist_ok=True)
MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)

output_df.to_csv(
    MASTER_SHEET_PATH,
    index=False,
    encoding="utf-8"
)

manifest_df.to_csv(
    MANIFEST_PATH,
    index=False,
    encoding="utf-8"
)

# --------------------------------------------------
# 8. Verify the generated sample
# --------------------------------------------------

print("\nSampling verification:")

print(f"Total sampled records: {len(output_df)}")
print(f"Unique dataset rows: {output_df['dataset_row'].nunique()}")

print("\nSample counts by category:")
print(output_df["label"].value_counts().to_string())

assert len(output_df) == 120
assert output_df["dataset_row"].nunique() == 120
assert all(
    output_df["label"].value_counts().get(category, 0) == 30
    for category in TARGET_CATEGORIES
)

print("\nSuccessfully generated:")
print(f"Master sheet: {MASTER_SHEET_PATH}")
print(f"Sampling manifest: {MANIFEST_PATH}")

