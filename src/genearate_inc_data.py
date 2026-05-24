from datetime import datetime
import os
import random
import pandas as pd
from faker import Faker

fake = Faker()


def generate_products_incremental(num_products=1000, file_path="data/raw/products.csv"):
    categories = [
        "Electronics",
        "Clothing",
        "Home & Kitchen",
        "Beauty",
        "Books",
        "Sports",
        "Toys",
    ]
    start_id = 1
    file_exists = os.path.exists(file_path) and os.stat(file_path).st_size > 0

    # 1. Check existing file to find the last product_id
    if file_exists:
        try:
            # Read only the 'product_id' column to save memory
            existing_df = pd.read_csv(file_path, usecols=["product_id"])
            if not existing_df.empty:
                start_id = int(existing_df["product_id"].max()) + 1
        except Exception as e:
            print(f"Error reading existing file, starting from ID 1: {e}")

    # 2. Generate new products starting from the incremental ID
    products = []
    end_id = start_id + num_products

    for product_id in range(start_id, end_id):
        products.append(
            {
                "product_id": product_id,
                "product_name": fake.word().capitalize(),
                "category": random.choice(categories),
                "price": round(random.uniform(10, 1000), 2),
                "added_date": datetime.now(),
                "added_by": "ADMIN",
            }
        )

    # 3. Save to DataFrame
    new_products_df = pd.DataFrame(products)

    # 4. Ensure directory exists before saving
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # 5. Append to CSV (only write headers if the file doesn't exist yet)
    new_products_df.to_csv(
        file_path, mode="a", index=False, header=not file_exists
    )

    print(
        f"Successfully appended {num_products} products (IDs {start_id} to {end_id - 1}) to '{file_path}'."
    )
    return new_products_df


# Execute the incremental generation
products_df = generate_products_incremental(num_products=1000)
