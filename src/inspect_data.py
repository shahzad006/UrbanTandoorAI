
import pandas as pd

files = {
    "MENU": "data/Urban_Tandoor_Complete_Menu_Catalog.xlsx",
    "INVENTORY": "data/Urban_Tandoor_Two_Branch_Inventory_Dataset.xlsx"
}

for name, path in files.items():

    print("\n" + "=" * 50)
    print(f"{name} WORKBOOK")
    print("=" * 50)

    excel = pd.ExcelFile(path)

    print("Total Sheets:", len(excel.sheet_names))
    print("Sheet Names:")

    for sheet in excel.sheet_names:
        print("-", sheet)
