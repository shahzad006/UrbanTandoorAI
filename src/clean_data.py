import pandas as pd

# Excel file location
file_path = "data/Urban_Tandoor_Complete_Menu_Catalog.xlsx"

# Read Excel sheet
df = pd.read_excel(file_path, sheet_name="Menu_Items")

print("Original Data Shape:", df.shape)

# 1. Clean column names
df.columns = df.columns.str.strip()

# 2. Remove extra spaces from text columns
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].map(
        lambda value: value.strip() if isinstance(value, str) else value
    )

# 3. Replace empty spaces with missing values
df = df.replace(r"^\s*$", pd.NA, regex=True)

# 4. Remove completely empty rows
df = df.dropna(how="all")

# 5. Count duplicate rows
duplicates = df.duplicated().sum()

print("\nCleaned Data Shape:", df.shape)
print("Duplicate Rows:", duplicates)

# Save cleaned data
df.to_csv(
    "outputs/cleaned/menu_items_cleaned.csv",
    index=False
)

print("\nData Cleaning Completed!")