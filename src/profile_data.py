
import pandas as pd
import json
import os

# Excel files
files = {
    "Menu": "data/Urban_Tandoor_Complete_Menu_Catalog.xlsx",
    "Inventory": "data/Urban_Tandoor_Two_Branch_Inventory_Dataset.xlsx"
}

# Create reports folder
os.makedirs("reports", exist_ok=True)

all_reports = []

for file_name, file_path in files.items():

    print("\n" + "=" * 50)
    print(f"DATA PROFILING: {file_name}")
    print("=" * 50)

    excel = pd.ExcelFile(file_path)

    for sheet in excel.sheet_names:

        # Skip instruction and dashboard sheets
        if sheet in ["START_HERE", "Dashboard"]:
            continue

        df = pd.read_excel(file_path, sheet_name=sheet)

        # Basic profiling
        report = {
            "workbook": file_name,
            "sheet_name": sheet,
            "total_rows": int(df.shape[0]),
            "total_columns": int(df.shape[1]),
            "missing_values": int(df.isnull().sum().sum()),
            "duplicate_rows": int(df.duplicated().sum()),
            "column_names": df.columns.tolist(),
            "data_types": {
                col: str(dtype)
                for col, dtype in df.dtypes.items()
            },
            "missing_by_column": {
                col: int(count)
                for col, count in df.isnull().sum().items()
            }
        }

        all_reports.append(report)

        print(f"\nSheet: {sheet}")
        print("Rows:", report["total_rows"])
        print("Columns:", report["total_columns"])
        print("Missing Values:", report["missing_values"])
        print("Duplicate Rows:", report["duplicate_rows"])

# Export JSON report
with open("reports/data_profile.json", "w") as file:
    json.dump(all_reports, file, indent=4)

# Export CSV summary
summary = []

for report in all_reports:
    summary.append({
        "Workbook": report["workbook"],
        "Sheet": report["sheet_name"],
        "Rows": report["total_rows"],
        "Columns": report["total_columns"],
        "Missing Values": report["missing_values"],
        "Duplicate Rows": report["duplicate_rows"]
    })

pd.DataFrame(summary).to_csv(
    "reports/data_profile.csv",
    index=False
)

print("\nData profiling completed!")
print("Reports saved in reports/ folder.")
