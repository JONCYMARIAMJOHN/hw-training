import os
import pandas as pd
import json

# =========================
# 1. Ask file format
# =========================
file_type = input("Enter file type (csv/json): ").strip().lower()

# =========================
# 2. Ask file path
# =========================
file_path = input("Enter full file path: ").strip()

if not os.path.exists(file_path):
    print("File not found!")
    exit()

# =========================
# 3. Read file based on type
# =========================
try:
    if file_type == "csv":
        delimiter = input("Enter delimiter (, | ; \\t): ").strip()

        if delimiter.lower() == "\\t":
            delimiter = "\t"

        df = pd.read_csv(file_path, delimiter=delimiter, dtype=str, keep_default_na=False)

    elif file_type == "json":
        # Handles both list-of-dict JSON and line-delimited JSON
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        df = pd.json_normalize(data)

    else:
        print("Unsupported file type. Use 'csv' or 'json'.")
        exit()

except Exception as e:
    print("Error reading file: {}".format(e))
    exit()

# =========================
# 4. Create output folder
# =========================
file_dir = os.path.dirname(file_path)
file_name = os.path.splitext(os.path.basename(file_path))[0]

output_folder = os.path.join(file_dir, file_name)
os.makedirs(output_folder, exist_ok=True)

print("\nOutput folder created:{}".format(output_folder))

# =========================
# 5. Convert to JSON (standardized output)
# =========================
json_output_path = os.path.join(output_folder, "{}.json".format(file_name))

records = df.replace('', None).to_dict(orient="records")

with open(json_output_path, "w", encoding="utf-8") as f:
    json.dump(records, f, indent=4, ensure_ascii=False)

print("Normalized JSON file created.")

# =========================
# 6. Column-wise value count files
# =========================
print("\nCreating column value summary files...")

for column in df.columns:

    series = df[column].replace('', pd.NA)

    value_counts = (
        series.fillna("<NULL>")
        .value_counts(dropna=False)
    )

    safe_column_name = "".join(
        c if c.isalnum() or c in (' ', '_', '-') else '_'
        for c in column
    )

    txt_path = os.path.join(output_folder, "{}.txt".format(safe_column_name))

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("Column: {}\n".format(column))
        f.write("Unique Values: {}\n\n".format(series.nunique(dropna=True)))
        f.write("Value\tCount\n")
        f.write("-" * 50 + "\n")

        for value, count in value_counts.items():
            f.write(" {}\t{}\n".format(value, count))

print("Column files created.")

# =========================
# 7. Generate report.txt
# =========================
report_path = os.path.join(output_folder, "report.txt")

with open(report_path, "w", encoding="utf-8") as report:

    report.write("=" * 80 + "\n")
    report.write("DATA QA REPORT\n")
    report.write("=" * 80 + "\n\n")

    # Data count
    report.write("Total Records : {}\n\n".format(len(df)))

    # Columns
    report.write("COLUMN NAMES\n")
    report.write("-" * 40 + "\n")
    for col in df.columns:
        report.write("{}\n".format(col))

    report.write("\n")

    # Null summary
    report.write("NULL SUMMARY\n")
    report.write("-" * 40 + "\n")

    for col in df.columns:
        non_null = df[col].replace('', pd.NA).notna().sum()
        null_count = len(df) - non_null

        report.write(
            "{}  "
            "    Non-null : {}  "
            "    Null     : {}  \n"
            .format(col, non_null, null_count)
        )

    # Unique summary
    report.write("UNIQUE SUMMARY\n")
    report.write("-" * 40 + "\n")

    for col in df.columns:
        is_unique = df[col].nunique(dropna=False) == len(df)
        if is_unique:
            uniqueness = "Unique"
        else:
            uniqueness = "Not Unique"

        report.write("{} : {}\n".format(col, uniqueness))

    report.write("\n")

    # Invalid values summary
    report.write("INVALID VALUES SUMMARY\n")
    report.write("-" * 40 + "\n")

    invalid_found = False

    for col in df.columns:

        invalid_mask = (
            df[col].fillna('').astype(str).str.strip().eq('[]') |
            df[col].fillna('').astype(str).str.strip().eq('{}')
        )

        invalid_count = invalid_mask.sum()

        if invalid_count > 0:
            invalid_found = True
            report.write(
                "{}\n"
                "    Invalid Count : {}\n\n"
                .format(col, invalid_count)
            )

    if not invalid_found:
        report.write("No invalid values found.\n")

print("\nQA process completed successfully!")
print("All outputs saved in: {}".format(output_folder))
