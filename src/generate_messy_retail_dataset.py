"""
Generate a realistic messy retail-sales CSV of at least 1 GiB.

Run from your Retail-Sales-Analysis project root:
    python src/generate_messy_retail_dataset.py

The script uses chunking so it does not build the entire dataset in RAM.
It requires pandas and numpy in the active Python environment.
"""

from pathlib import Path
import time

import numpy as np
import pandas as pd


# -------------------- SETTINGS --------------------
TARGET_BYTES = 1 * 1024 * 1024 * 1024  # 1 GiB = 1,073,741,824 bytes
CHUNK_ROWS = 50_000
SEED = 42
OUTPUT_FILE = Path("dataset") / "messy_retail_sales_1gb.csv"

rng = np.random.default_rng(SEED)

# -------------------- HELPER DATA --------------------
products = [f"P{i:05d}" for i in range(1, 1501)]
customers = [f"C{i:07d}" for i in range(1, 100_001)]
stores = [f"S{i:04d}" for i in range(1, 151)]
cities = [
    "Rewa", "Bhopal", "Indore", "Jabalpur", "Delhi", "Mumbai",
    "Pune", "Hyderabad", "Bengaluru", "Chennai", "Kolkata",
    "Jaipur", "Lucknow", "Nagpur", "Ahmedabad",
]
categories = [
    "Electronics", "Grocery", "Clothing", "Home & Kitchen",
    "Beauty", "Sports", "Books", "Furniture",
]
payment_modes = ["UPI", "Cash", "Credit Card", "Debit Card", "Net Banking"]
channels = ["Online", "In-store", "Mobile App", "Marketplace"]
regions = ["North", "South", "East", "West", "Central"]
first_names = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai",
    "Ishita", "Ananya", "Diya", "Myra", "Aanya", "Riya",
]
last_names = [
    "Sharma", "Singh", "Verma", "Patel", "Gupta", "Yadav",
    "Khan", "Mishra", "Jain", "Das", "Reddy", "Mehta",
]


def make_chunk(start_order_number: int, n: int) -> pd.DataFrame:
    """Create one chunk and intentionally inject data-quality problems."""
    order_numbers = np.arange(start_order_number, start_order_number + n)
    order_ids = np.array([f"O{x:010d}" for x in order_numbers], dtype=object)

    # Intentional duplicate OrderIDs: around 1.5% reuse an earlier ID in this chunk.
    duplicate_id_mask = rng.random(n) < 0.015
    if n > 1:
        earlier_positions = rng.integers(0, n, size=n)
        valid = earlier_positions < np.arange(n)
        duplicate_id_mask &= valid
        positions = np.where(duplicate_id_mask)[0]
        order_ids[positions] = order_ids[earlier_positions[positions]]

    quantity = rng.integers(1, 11, size=n)
    unit_price = np.round(rng.uniform(25, 25_000, size=n), 2)
    gross_sales = np.round(quantity * unit_price, 2)
    discount_percent = np.round(rng.choice(
        [0, 5, 10, 15, 20, 25, 30], size=n,
        p=[0.20, 0.15, 0.20, 0.15, 0.15, 0.10, 0.05]
    ), 2)
    discount_amount = np.round(gross_sales * discount_percent / 100, 2)
    return_flag = rng.random(n) < 0.08
    return_quantity = np.where(return_flag, rng.integers(1, 4, size=n), 0)
    return_amount = np.round(return_quantity * unit_price, 2)
    net_sales = np.round(gross_sales - discount_amount - return_amount, 2)
    cogs = np.round(gross_sales * rng.uniform(0.45, 0.85, size=n), 2)
    profit = np.round(net_sales - cogs, 2)

    dates = pd.Timestamp("2023-01-01") + pd.to_timedelta(
        rng.integers(0, 1461, size=n), unit="D"
    )

    customer_first = rng.choice(first_names, size=n)
    customer_last = rng.choice(last_names, size=n)
    customer_names = np.char.add(
        np.char.add(customer_first.astype(str), " "),
        customer_last.astype(str),
    )

    df = pd.DataFrame({
        "OrderID": order_ids,
        "OrderDate": dates.strftime("%Y-%m-%d"),
        "CustomerID": rng.choice(customers, size=n),
        "CustomerName": customer_names,
        "ProductID": rng.choice(products, size=n),
        "StoreID": rng.choice(stores, size=n),
        "City": rng.choice(cities, size=n),
        "Region": rng.choice(regions, size=n),
        "Category": rng.choice(categories, size=n),
        "Quantity": quantity,
        "UnitPrice": unit_price,
        "GrossSales": gross_sales,
        "DiscountPercent": discount_percent,
        "DiscountAmount": discount_amount,
        "ReturnFlag": return_flag,
        "ReturnQuantity": return_quantity,
        "ReturnAmount": return_amount,
        "NetSales": net_sales,
        "COGS": cogs,
        "Profit": profit,
        "PaymentMode": rng.choice(payment_modes, size=n),
        "SalesChannel": rng.choice(channels, size=n),
        "OrderMonth": dates.strftime("%Y-%m"),
        "OrderYear": dates.year,
        "SalesRepresentative": [
            f"REP-{x:04d}" for x in rng.integers(1, 1001, size=n)
        ],
    })

    # 1) Missing values: set selected cells to true nulls.
    for col in ["CustomerID", "City", "UnitPrice", "PaymentMode", "Profit"]:
        mask = rng.random(n) < 0.008
        df.loc[mask, col] = np.nan

    # 2) Blank values: empty strings and whitespace-only strings.
    for col in ["CustomerName", "Category", "SalesChannel", "SalesRepresentative"]:
        blank_mask = rng.random(n) < 0.006
        space_mask = (rng.random(n) < 0.004) & ~blank_mask
        df.loc[blank_mask, col] = ""
        df.loc[space_mask, col] = "   "

    # 3) Duplicate complete rows: append copies of a small subset.
    # They are added in the outer loop so the resulting CSV contains exact repeats.

    # Convert Quantity to object so the intentional text value "unknown"
    # can coexist with numeric quantities in the same CSV column.
    df["Quantity"] = df["Quantity"].astype(object)

    # Additional realistic quality issues for cleaning practice.
    bad_date_mask = rng.random(n) < 0.001
    df.loc[bad_date_mask, "OrderDate"] = "2025-99-45"

    bad_quantity_mask = rng.random(n) < 0.001
    df.loc[bad_quantity_mask, "Quantity"] = -rng.integers(1, 6, size=bad_quantity_mask.sum())

    bad_price_mask = rng.random(n) < 0.001
    df.loc[bad_price_mask, "UnitPrice"] = -np.round(
        rng.uniform(10, 5000, size=bad_price_mask.sum()), 2
    )

    inconsistent_category_mask = rng.random(n) < 0.01
    df.loc[inconsistent_category_mask, "Category"] = (
        df.loc[inconsistent_category_mask, "Category"].astype(str).str.lower()
    )

    # A few deliberately incorrect numeric strings to create mixed-type columns.
    mixed_type_mask = rng.random(n) < 0.0005
    df.loc[mixed_type_mask, "Quantity"] = "unknown"

    return df


def main():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    if OUTPUT_FILE.exists():
        raise FileExistsError(
            f"{OUTPUT_FILE} already exists. Rename/delete it before generating again."
        )

    print("Generating messy retail dataset...")
    print(f"Target size: {TARGET_BYTES:,} bytes (1 GiB)")
    print(f"Output: {OUTPUT_FILE.resolve()}")
    print("This may take some time. Keep your computer plugged in if possible.\n")

    start_time = time.time()
    total_rows = 0
    chunk_number = 0
    write_header = True

    while not OUTPUT_FILE.exists() or OUTPUT_FILE.stat().st_size < TARGET_BYTES:
        chunk_number += 1
        chunk = make_chunk(total_rows + 1, CHUNK_ROWS)

        # Inject exact duplicate rows (about 1% of this chunk).
        duplicate_count = max(1, int(CHUNK_ROWS * 0.01))
        duplicate_rows = chunk.sample(
            n=duplicate_count, random_state=SEED + chunk_number
        )
        chunk = pd.concat([chunk, duplicate_rows], ignore_index=True)

        chunk.to_csv(
            OUTPUT_FILE,
            mode="w" if write_header else "a",
            header=write_header,
            index=False,
        )
        write_header = False
        total_rows += CHUNK_ROWS + duplicate_count

        size_gib = OUTPUT_FILE.stat().st_size / (1024 ** 3)
        elapsed = time.time() - start_time
        print(
            f"Chunk {chunk_number:>3} | "
            f"Rows written: {total_rows:,} | "
            f"File size: {size_gib:.3f} GiB | "
            f"Elapsed: {elapsed / 60:.1f} min"
        )

    final_size = OUTPUT_FILE.stat().st_size
    print("\nDATASET GENERATION COMPLETE")
    print(f"File: {OUTPUT_FILE.resolve()}")
    print(f"Rows written: {total_rows:,}")
    print(f"Columns: 25")
    print(f"Final size: {final_size:,} bytes ({final_size / (1024 ** 3):.3f} GiB)")
    print("Injected issues: missing values, blanks/spaces, exact duplicate rows,")
    print("duplicate OrderIDs, invalid dates, negative values, inconsistent text,")
    print("and mixed-type values.")


if __name__ == "__main__":
    main()
