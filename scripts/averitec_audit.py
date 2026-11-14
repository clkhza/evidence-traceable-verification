
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
# 2. Load dataset
# --------------------------------------------------

if not DATASET_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATASET_PATH}"
    )

with open(DATASET_PATH, "r", encoding="utf-8") as f:
    dev_data = json.load(f)

if not isinstance(dev_data, list):
    raise ValueError("Expected dev.json to contain a list.")

print(f"Total dataset records: {len(dev_data)}")


# --------------------------------------------------
# 3. Group records by verdict
# --------------------------------------------------

verdict_groups = {category: [] for category in TARGET_CATEGORIES}

for idx, item in enumerate(dev_data):
    label = item.get("label")

    if label in verdict_groups:
        record = item.copy()
        record["dataset_row"] = idx
        verdict_groups[label].append(record)

print("\nAvailable records:")

for category, records in verdict_groups.items():
    print(f"{category}: {len(records)}")

for category, records in verdict_groups.items():
    if len(records) < SAMPLE_SIZE:
        raise ValueError(
            f"Not enough records for {category}: "
            f"{len(records)} available."
        )


# --------------------------------------------------
# 4. Stratified random sampling
# --------------------------------------------------

rng = random.Random(RANDOM_SEED)
sampled_records = []

for category in TARGET_CATEGORIES:
    selected = rng.sample(
        verdict_groups[category],
        SAMPLE_SIZE
    )

    sampled_records.extend(selected)

    print(f"Selected {len(selected)}: {category}")

if len(sampled_records) != 120:
    raise ValueError("The sample must contain exactly 120 records.")


# --------------------------------------------------
# 5. Extract nested questions and answers
# --------------------------------------------------

def format_questions_and_answers(questions):

    if not isinstance(questions, list):
        return ""

    formatted = []

    for question_item in questions:

        question = question_item.get("question", "")
        answers = question_item.get("answers", [])

        if not isinstance(answers, list):
            answers = [answers] if answers else []

        if not answers:
            formatted.append(
                f"Q: {question}\nA: No answer recorded."
            )
            continue

        for answer_item in answers:

            if not isinstance(answer_item, dict):
                continue

            answer = answer_item.get("answer", "")
            answer_type = answer_item.get("answer_type", "")
            source_url = answer_item.get("source_url", "")
            source_medium = answer_item.get("source_medium", "")
            cached_url = answer_item.get("cached_source_url", "")

            formatted.append(
                f"Q: {question}\n"
                f"A: {answer}\n"
                f"Answer type: {answer_type}\n"
                f"Source URL: {source_url}\n"
                f"Cached source URL: {cached_url}\n"
                f"Source medium: {source_medium}"
            )

    return "\n\n".join(formatted)


# --------------------------------------------------
# 6. Extract source URLs
# --------------------------------------------------

def extract_source_urls(questions):

    urls = []

    if not isinstance(questions, list):
        return ""

    for question_item in questions:

        answers = question_item.get("answers", [])

        if not isinstance(answers, list):
            answers = [answers] if answers else []

        for answer_item in answers:

            if not isinstance(answer_item, dict):
                continue

            for field in ["source_url", "cached_source_url"]:
                url = answer_item.get(field)

                if url and url not in urls:
                    urls.append(url)

    return "\n".join(urls)


# --------------------------------------------------
# 7. Create annotation master sheet
# --------------------------------------------------

rows = []

for item in sampled_records:

    questions = item.get("questions", [])

    row = {
        "dataset_row": item.get("dataset_row"),
        "label": item.get("label"),
        "claim": item.get("claim"),
        "claim_date": item.get("claim_date"),
        "speaker": item.get("speaker"),
        "fact_checking_article": item.get("fact_checking_article"),
        "original_claim_url": item.get("original_claim_url"),
        "justification": item.get("justification"),

        "questions_and_answers":
            format_questions_and_answers(questions),

        "source_urls":
            extract_source_urls(questions),

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

        # Annotation metadata
        "ai_notes": None,
        "review_status": "pending",
        "reviewer": None,
        "review_date": None,
    }

    rows.append(row)


# --------------------------------------------------
# 8. Export master sheet
# --------------------------------------------------

output_df = pd.DataFrame(rows)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

output_df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8"
)


# --------------------------------------------------
# 9. Verify sample
# --------------------------------------------------

assert len(output_df) == 120
assert output_df["dataset_row"].nunique() == 120

for category in TARGET_CATEGORIES:
    count = (output_df["label"] == category).sum()

    assert count == SAMPLE_SIZE, (
        f"Incorrect sample count for {category}: {count}"
    )

print("\nSampling completed successfully.")
print(f"Total records: {len(output_df)}")
print(f"Output: {OUTPUT_PATH}")

print("\nRecords per category:")
print(output_df["label"].value_counts().to_string())

print("\nQuestions and answers extracted:")
print(
    output_df["questions_and_answers"]
    .str.len()
    .gt(0)
    .sum()
)

print("\nSource URL fields populated:")
print(
    output_df["source_urls"]
    .str.len()
    .gt(0)
    .sum()
)
