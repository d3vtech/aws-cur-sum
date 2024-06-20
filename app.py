import pandas as pd

FILENAME = "data/input.csv"
OUTPUT_FILENAME = "data/sorted_product_totals.csv"

df = pd.read_csv(FILENAME, low_memory=False)

columns = list(df.columns)

useful_coloumns = [
    "lineItem/LineItemType",
    "lineItem/UsageType",
    "lineItem/UsageAmount",
    "lineItem/BlendedRate",
    "lineItem/BlendedCost",
    "product/ProductName",
    "pricing/unit",
]

df = df[useful_coloumns]

product_names = df["product/ProductName"].unique()

product_totals = {
    product: df[df["product/ProductName"] == product]["lineItem/BlendedCost"].sum()
    for product in product_names
}

sorted_product_totals = sorted(product_totals.items(), key=lambda x: x[1], reverse=True)

df = pd.DataFrame(
    sorted_product_totals, columns=["product/ProductName", "lineItem/BlendedCost"]
)

df.to_csv(OUTPUT_FILENAME, index=False)
